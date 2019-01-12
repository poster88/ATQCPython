import pytest
from fixture.application import Application


@pytest.fixture(scope="session", autouse=False)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
