# SAUCEDEMO UI Tests

Python/Selenium Page Object Model test project for SauceDemo. The inventory
page is the product dashboard shown after a successful login.

## Project structure

```text
config/                 Environment and browser configuration
pages/                  Selenium Page Objects
tests/                  Login, dashboard, and checkout test cases
utils/                  JSON data reader and test logger
test_data/users.json    Test account data
reports/screenshots/    Screenshots captured when a test fails
requirements.txt        Python test dependencies
pytest.ini              Pytest discovery configuration
```

The equivalent relative XPath for each page-object element is documented in
[docs/relative_xpath_reference.md](docs/relative_xpath_reference.md).

## Run tests

Install dependencies and run the test suite:

```powershell
python -m pip install -r requirements.txt
python -m pytest
```

Chrome is used by default. Set `SAUCEDEMO_HEADLESS=true` to run headlessly,
`SAUCEDEMO_BASE_URL` to override the application URL, or
`SAUCEDEMO_WAIT_TIMEOUT` to configure the explicit-wait timeout in seconds.
