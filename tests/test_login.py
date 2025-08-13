
import pytest
from pages.login_page import LoginPage
from utils.store_data import load_user_data


# @pytest.mark.login
def test_login_with_registered_user(page):
    user_data = load_user_data()

    if not user_data :
        pytest.skip("skipping the login because user data not found ")

    #"email" : email, "password" : password}
    email = user_data["email"]
    password = user_data["password"]

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(email=email, password=password)
    login_page.verify_login_success()

