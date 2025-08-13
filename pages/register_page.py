from  playwright.sync_api import  Page , expect

class RegisterPage:

    def __init__(self, page:Page):
        self.page = page

        # locators will be here

        self.register_btn = "//a[@class='btn1']"
        self.first_name_input = "//input[@type='firstName']"
        self.last_name_input =  "//input[@type='lastName']"
        self.email_input =  "//input[@type='email']"
        self.mobile_no_input = "//input[@type='text']"
        self.occupation_select = "//select[@formcontrolname='occupation']"
        self.male_radio = "//input[@value='Male']"
        self.password_input = "//input[@id='userPassword']"
        self.pass_conform_input = "//input[@formcontrolname='confirmPassword']"
        self.condition_checkbox = "//input[@type='checkbox']"
        self.submit_btn = "//input[@type='submit']"
        self.success_msg_output = "//h1[@class='headcolor']"

    def navigate_to_register(self):
        self.page.locator(self.register_btn).click()

    def fill_personal_details(self, first_name, last_name, email, phone_no):
        self.page.locator(self.first_name_input).fill(first_name)
        self.page.locator(self.last_name_input).fill(last_name)
        self.page.locator(self.email_input).fill(email)
        self.page.locator(self.mobile_no_input).fill(phone_no)

    def select_occupation(self, label):
        self.page.select_option(self.occupation_select, label=label)

    def select_gender(self, gender= "Male"):
        if gender.lower() == "male" :
            self.page.locator(self.male_radio).check()
            expect  (self.page.locator(self.male_radio)).to_be_visible()

    def set_password(self, password):
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.pass_conform_input).fill(password)

    def term_condition(self):
        self.page.locator(self.condition_checkbox).check()
        expect (self.page.locator(self.condition_checkbox)).to_be_checked()

    def submit_form(self):
        self.page.locator(self.submit_btn).click()

    def verify_success_msg(self, actual_text = "Account Created Successfully" ):
        text_get = self.page.locator(self.success_msg_output).text_content()
        assert actual_text in text_get , f"the actual text is {actual_text} and got the text is {text_get}"









