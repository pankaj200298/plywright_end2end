# conftest.py
import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
import allure

# -----------------------
# Playwright page fixture
# -----------------------
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

# ------------------------------------
# Pytest hook for screenshots on fail
# ------------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook to capture screenshot on test failure.
    """
    outcome = yield
    result = outcome.get_result()

    # Only capture screenshot for 'call' phase (actual test body)
    if result.when == "call" and result.failed:
        page_obj = item.funcargs.get("page", None)
        if page_obj:
            # Create screenshots directory if not exists
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join(
                "screenshots", f"{item.name}_{timestamp}.png"
            )

            try:
                page_obj.screenshot(path=screenshot_path, full_page=True)
                print(f"\n[!] Screenshot saved to: {screenshot_path}")

                # Optional: Attach to Allure report
                if "allure" in item.config.pluginmanager.list_plugin_distinfo():
                    allure.attach.file(
                        screenshot_path,
                        name=f"{item.name}_failure_screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )

            except Exception as e:
                print(f"[!] Could not take screenshot: {e}")
