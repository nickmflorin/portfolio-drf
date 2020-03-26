from datetime import datetime, timedelta

from factory.fuzzy import FuzzyNaiveDateTime


__all__ = ('BasicDateTimeField', 'NowDateTimeField')


class BasicDateTimeField(FuzzyNaiveDateTime):
    """
    Selects a random date between today and two years ago from today, if the
    default start_value is not specified.
    """
    def __init__(self, start_value=None, *args, **kwargs):

        end_value = datetime.now()
        if not start_value:
            start_value = end_value - timedelta(days=365 * 2)

        super(BasicDateTimeField, self).__init__(start_value, end_value, *args, **kwargs)


class NowDateTimeField(BasicDateTimeField):
    """
    Override the .fuzz() method for generating random dates to always return
    the current datetime.
    """
    def fuzz(self):
        return datetime.now()
