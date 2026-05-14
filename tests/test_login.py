import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utilities.csv_reader import get_login_data
from config.config import BASE_URL

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


test_data = get_login_data("../data/login_data.csv")


@pytest.mark.parametrize("username,password,expected", test_data)
def test_login(driver, username, password, expected):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login(username, password)

    if expected == "valid":

        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Dashboard']")
            )
        )

        dashboard = DashboardPage(driver)

        assert dashboard.is_dashboard_displayed()

    else:

        assert "Invalid credentials" in login.get_error_message()
