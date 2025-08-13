from playwright.sync_api import Page , expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.email_input = "input[type='email']"
        self.password_input = "input[type='password']"
        self.login_btn = "input[type='submit']"
        self.dashboard_text = "//h3[text()='Automation']" # Automation text
        self.Register_page_title = "//a[text()='Register']"

    def goto(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self, email, password ):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.locator(self.login_btn).click()
        self.page.wait_for_timeout(3000)

    def verify_login_success(self):
        text = self.page.locator(self.dashboard_text).text_content()
        assert "Automation" in text


    def verify_login_failure(self):
        text = self.page.locator(self.Register_page_title).text_content()
        assert "Register" in text



