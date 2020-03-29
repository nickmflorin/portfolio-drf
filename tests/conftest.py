import pytest
from rest_framework.test import APIClient

from tests.factories import factories


@pytest.fixture
def api_client(monkeypatch):
    """
    Custom API Client that we will use to monkeypatch around edge cases if we
    need it.  We will most likely need to do this so this is a good starting
    point.
    """
    class CustomApiClient(APIClient):
        pass

    return CustomApiClient()


def inject_factory_fixtures():
    """
    This method will dynamically create factory fixtures for all of the
    factories present in the factories module.

    If we have a factory:
    >>> class SomeFactory():
    >>>     ...

    Then, a fixture will be generated with the name `some` which can be used
    as:

    >>> def test_something(create_some):
    >>>     model = create_some(attr1='foo', attr2='bar')
    """
    def model_factory_fixture_generator(factory_cls):
        @pytest.fixture(scope='module')
        def factory_fixture():
            def factory_generator(**kwargs):
                return factory_cls(**kwargs)
            return factory_generator
        return factory_fixture

    for factory_name in factories.__dict__['__all__']:
        factory_cls = factories.__dict__[factory_name]
        name = f"create_{factory_name.split('Factory')[0].lower()}"
        globals()[name] = model_factory_fixture_generator(factory_cls)


inject_factory_fixtures()
