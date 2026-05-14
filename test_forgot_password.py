from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_forgot_password(driver):

    wait = WebDriverWait(driver, 30)

    # Open Application
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Click Forgot Password
    forgot_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'forgot')]//p")
        )
    )

    forgot_link.click()

    # Verify Reset Password page
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[text()='Reset Password']")
        )
    )

    assert "requestPasswordResetCode" in driver.current_url
