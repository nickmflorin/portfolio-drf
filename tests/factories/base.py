# -*- coding: utf-8 -*-
from __future__ import absolute_import

from copy import deepcopy
from factory.django import DjangoModelFactory

from .fields import BasicDateTimeField


class PortfolioModelFactory(DjangoModelFactory):
    """
    Incoporates useful utils and behavior into the generic `DjangoModelFactory`.
    """
    date_created = BasicDateTimeField()
    date_modified = BasicDateTimeField()

    @classmethod
    def create(cls, *args, **kwargs):
        prepared_kwargs = cls._prepare(*args, **kwargs)
        cleaned_kwargs = cls.clean(*args, **prepared_kwargs)

        created = super(PortfolioModelFactory, cls).create(*args, **cleaned_kwargs)
        return cls.post_create(created, **cleaned_kwargs)

    @classmethod
    def post_create(cls, model, **kwargs):
        """
        Useful if there is some conditional updating we want to perform to the
        factory created object after it is created.
        """
        return model

    @classmethod
    def _prepare(cls, *args, **kwargs):
        """
        Called right from `.create()`.  It does the following:

        Looks for all classmethod(s) that begin with `prepare_`, calls the
        method and includes the returned options in the kwargs that are passed
        to the factory.
        """
        preparations = cls.preparations()
        prepared_kwargs = deepcopy(kwargs)

        for preparation in preparations:
            updated_kwargs = preparation(*args, **prepared_kwargs)
            if updated_kwargs:
                prepared_kwargs.update(**updated_kwargs)

        return prepared_kwargs

    @classmethod
    def clean(cls, *args, **kwargs):
        """
        Remove additional keyword arguments that are used for logic in
        .create(), but cannot be passed into the model factory.
        """
        return deepcopy(kwargs)

    @classmethod
    def defaults(cls, *args, **kwargs):
        return {}

    @classmethod
    def preparations(cls):
        """
        Looks for all classmethod(s) that begin with "prepare_" and returns
        the methods so that they can be called by `_.prepare()`.

        We will override this for factories where the order of preparation methods
        is important.
        """
        methods = []
        for attr in dir(cls):
            method = getattr(cls, attr)
            if callable(method) and method.__name__.startswith('prepare_'):
                methods.append(method)
        return methods

    class Meta:
        abstract = True
