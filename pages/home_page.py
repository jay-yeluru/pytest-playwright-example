from playwright.sync_api import expect

from .base_page import BasePage


class HomePage(BasePage):
    """Page object representing the Playwright documentation home page."""

    # locators
    _get_started_link = "role=link[name=\"Get started\"]"
    _installation_heading = "role=heading[name=\"Installation\"]"

    def navigate(self) -> None:
        """Open the home page using the configured base URL."""
        self.goto("/")

    def click_get_started(self) -> None:
        self.page.locator(self._get_started_link).click()

    def expect_installation_visible(self) -> None:
        expect(self.page.locator(self._installation_heading)).to_be_visible()

    def expect_title_contains(self, text: str) -> None:
        expect(self.page).to_have_title(text)
