import re
from playwright.sync_api import Page

from pages.home_page import HomePage


def test_home_title(page: Page, base_url: str):
    """Verify home page title contains expected text."""
    home = HomePage(page, base_url)
    home.navigate()
    home.expect_title_contains(re.compile("Playwright"))


def test_get_started_navigation(page: Page, base_url: str):
    home = HomePage(page, base_url)
    home.navigate()
    home.click_get_started()
    home.expect_installation_visible()
