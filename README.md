# Python Playwright POM Example

This repository demonstrates a simple Page Object Model (POM) based end-to-end
automation framework using the latest Python Playwright packages and
`pytest`/`pytest-playwright` plugin.

## Structure

```
pytest-playwright-example/
├── pages/             # page object definitions
│   ├── base_page.py
│   └── home_page.py
├── tests/             # pytest test modules
│   └── test_example.py
├── conftest.py        # fixtures (base_url, etc.)
├── pytest.ini         # pytest configuration and markers
├── requirements.txt   # dependencies
└── README.md          # this file
```

## Getting Started

1. **Create a virtual environment** and install dependencies (a Python 3.10+ interpreter is recommended, older versions will still work with the pinned requirements):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Install browser binaries** used by Playwright:

   ```bash
   playwright install
   ```

3. **Run tests**:

   ```bash
   # default single/browser run:
   python -m pytest -q

   # specify one or more browsers explicitly:
   python -m pytest -q --browser chromium
   python -m pytest -q --browser chromium,firefox,webkit
   ```

   You can also instrument individual tests to accept a `browser_name`
   argument, which pytest-playwright will automatically populate based on the
   value(s) passed on the command line or configuration.

   Output will appear in the console. A simple HTML report can be generated
   by adding `--html=reports/report.html` (create the `reports` directory first) or
   specify a browser-specific path such as `--html=reports/report-firefox.html`.

## Example Page Object

```python
class HomePage(BasePage):
    def navigate(self):
        self.goto("/")

    def click_get_started(self):
        self.page.get_by_role("link", name="Get started").click()
```

## Extending the Framework

- Add new page classes under `pages/` with methods encapsulating user
  interactions.
- Put business-level tests in `tests/` that consume the page objects.
- Use fixtures in `conftest.py` to share common data (URLs, credentials, etc.).

## Notes

- This example uses **sync API** from Playwright. For async tests, adjust
  imports and fixtures accordingly.
- `pytest-playwright` provides `page`, `browser`, and other fixtures out of
  the box.

---

## Continuous Integration (GitHub Actions)

A workflow is provided at `.github/workflows/ci.yml` that demonstrates a
matrix build over the three Playwright engines. It:

1. Checks out the repo and sets up Python 3.10.
2. Caches `pip` packages for speed.
3. Creates a virtualenv and installs requirements.
4. Runs `playwright install` to fetch browsers.
5. Executes `pytest` with `--browser` set from the matrix; an HTML report is
   archived as an artifact on every run.

You can adapt the job to publish results, post comments, or run only a
subset of browsers based on the path/branch.

---

Feel free to adapt and expand this template for your own end-to-end test
suites.
