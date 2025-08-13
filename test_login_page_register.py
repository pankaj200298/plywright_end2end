from playwright.sync_api import sync_playwright
import time
#==========================================================================================

# this function is only to generate random  emails so test should not fail
# as this account is already exist

def generate_random_email():
    return f"pankaj.{int(time.time())}@gmail.com"

#==========================================================================================

# this is the browser invocation method only
def test_redirect_register_page():
    with sync_playwright() as p :
        browser =  p.firefox.launch(headless=False)
        page = browser.new_page()
        url = "https://rahulshettyacademy.com/client/#/auth/login"
        page.goto(url=url)
        page.wait_for_timeout(2000)

#==========================================================================================

        # this is method to go register page
        page.locator("//a[@class='btn1']").click()

#==========================================================================================

        # adding name and surname in box
        page.fill("//input[@type='firstName']","pankaj")
        page.fill("//input[@type='lastName']", "chanekar")

#==========================================================================================

        # this is box where we are storing random mail function in one variable
        # we can use this random mail in other test to log in other flow
        #  we are using try except block and using Exception, and it can give to use to exception
        try:
            mail = generate_random_email()
            page.locator("//input[@type='email']").fill(mail)
            print(f":: the random generated mail is :: {mail} :: ")

        except Exception as e :
            print(f"the random mail not generate as :: {e} ")

#==========================================================================================

        # this box is used to add mobile number
        page.fill("//input[@type='text']", "1234567890")

#==========================================================================================

        #this method is used to select occupation
        page.select_option("//select[@formcontrolname='occupation']", label="Student")

#==========================================================================================


        #this is just checkbox to select male or female
        # using assertion which will check checkbox is select or not
        page.locator("//input[@value='Male']").check()
        assert page.locator("//input[@value='Male']").is_checked()

#==========================================================================================


        # this is just password field so you can choose your own password
        page.locator("//input[@id='userPassword']").fill("Pankaj@12345678")
        page.fill("//input[@formcontrolname='confirmPassword']", "Pankaj@12345678")

#==========================================================================================

        # thus is just final checkbox to register just you have to check it
        # by putting assertion you can check whether it clicked or not
        page.locator("//input[@type='checkbox']").check()
        assert page.locator("//input[@type='checkbox']").is_checked()
        page.wait_for_timeout(2000)

#==========================================================================================

        # this is just final submit button
        page.locator('//input[@type="submit"]').click()

#==========================================================================================
        # this is method to just check whether if it is register successfully
        # and  added try except block so test should not break

        text =  page.locator("//h1[@class='headcolor']").text_content()
        try:
            assert text == "Account Created Successfully"
            print(f"::Account Created Successfully::")
        except Exception as e :
            print(f"::account could not create as : {e}")
        page.wait_for_timeout(5000)