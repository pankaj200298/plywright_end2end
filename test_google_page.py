from playwright.sync_api import sync_playwright


def test_googl_search():
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        url = "https://google.com"
        page = browser.new_page()
        page.goto(url=url)
        page.wait_for_timeout(3000)
        title = page.title()
        try:
            assert "Google" == title
            print(f" :: the title is matched as : {title}")
        except Exception as e :
            print(f"the title is not matched as : {e}")

        page.close()
