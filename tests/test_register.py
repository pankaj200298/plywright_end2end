import pytest
from playwright.sync_api import sync_playwright
from  utils.data_generator import generate_random_name,generate_random_mail, generate_random_lastname, generate_random_mobile_no
from pages.register_page import RegisterPage
from utils.store_data import save_user_data


def test_register_page(page):

    # details to fill the form
    first_name = generate_random_name()
    last_name = generate_random_lastname()
    email = generate_random_mail()
    mo_no = generate_random_mobile_no()
    password = "Pankaj@12345"
    occupation = "Engineer"

# Pankaj@123
# pankaj20@gmail.com
# title = Let's Shop

    url = "https://rahulshettyacademy.com/client/#/auth/login"
    page.goto(url=url)

    # calling the RegisterPage class
    register_page = RegisterPage(page)

    # doing action to perform operations

    # calling navigate function
    register_page.navigate_to_register()

    #filling personal details
    register_page.fill_personal_details(first_name=first_name, last_name=last_name, email=email, phone_no=mo_no)

    #select gender
    register_page.select_gender()

    #selct occupation
    register_page.select_occupation(label=occupation)

    #seting the password
    register_page.set_password(password=password)

    #accepting the term and condition
    register_page.term_condition()

    #submiting the form by clicking submit button
    register_page.submit_form()

    #verifing the account creating successfully
    register_page.verify_success_msg()

    # saving the credential for login test
    save_user_data(email=email, password= password)











