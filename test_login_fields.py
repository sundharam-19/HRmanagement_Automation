from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL


def test_login_fields(driver):

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 40)

    username = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "username")
        )
    )

    password = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "password")
        )
    )

    assert username.is_displayed()
    assert password.is_displayed()
