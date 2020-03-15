import pytest
from rest_framework.test import APIClient


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
