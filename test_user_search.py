from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_user(driver):

    wait = WebDriverWait(driver, 600)

    # Open Application
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Login
    wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")

    driver.find_element(By.NAME, "password").send_keys("admin123")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for dashboard
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[text()='Dashboard']")
        )
    )

    # Click Admin Menu
    admin_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Admin']")
        )
    )

    admin_menu.click()

    # Validation
    assert "admin" in driver.current_url.lower()
