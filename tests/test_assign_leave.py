from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_assign_leave(driver):

    wait = WebDriverWait(driver, 60)

    driver.get("https://opensource-demo.orangehrmlive.com")

    # Login
    wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")

    driver.find_element(By.NAME, "password").send_keys("admin123")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Click Leave Menu
    leave_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Leave']")
        )
    )

    leave_menu.click()

    # Verify Leave Page
    assert "leave" in driver.current_url.lower()
