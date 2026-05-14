from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_myinfo_menu(driver):

    wait = WebDriverWait(driver, 120)

    # Open application
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Login
    wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")

    driver.find_element(By.NAME, "password").send_keys("admin123")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Click My Info menu
    myinfo = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='My Info']")
        )
    )

    myinfo.click()

    # Validation
    assert "viewPersonalDetails" in driver.current_url
