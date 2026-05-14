from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config.config import *


def test_claim_request(driver):

    wait = WebDriverWait(driver, 30)

    # Open application
    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    # Wait for dashboard after login
    dashboard = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[text()='Dashboard']")
        )
    )

    # Verify dashboard displayed
    assert dashboard.is_displayed()
