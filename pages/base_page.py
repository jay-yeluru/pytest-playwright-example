from playwright.sync_api import Page


class BasePage:
    """Simple base page that wraps a Playwright ``Page`` instance.

    Concrete page objects should inherit from this class so they have easy
    access to ``self.page`` and any shared helper methods.
    """

    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "") -> None:
        """Navigate to ``base_url + path``.

        ``path`` may be a full URL or a relative segment.
        """
        if path.startswith("http"):
            url = path
        else:
            url = f"{self.base_url}{path}"
        self.page.goto(url)
