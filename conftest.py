import pytest


@pytest.fixture(scope="session")
def base_url():
    """The URL that the tests will navigate to.

    Having a fixture makes it easy to override the target in CI or for
    localization without changing the test logic.
    """
    return "https://playwright.dev"
