import re
from pathlib import Path

import pytest
from selenium.common.exceptions import WebDriverException

from config.capabilities import create_chrome_driver
from utils.logger import get_logger


LOGGER = get_logger(__name__)
SCREENSHOTS_DIR = Path(__file__).resolve().parents[1] / "reports" / "screenshots"


@pytest.fixture
def driver():
    browser = create_chrome_driver()
    try:
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    browser = item.funcargs.get("driver")
    if browser is None:
        return

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid) + ".png"
    screenshot_path = SCREENSHOTS_DIR / filename
    try:
        if not browser.save_screenshot(str(screenshot_path)):
            LOGGER.error("Failed to save test failure screenshot to %s", screenshot_path)
    except WebDriverException:
        LOGGER.exception("Could not capture test failure screenshot")