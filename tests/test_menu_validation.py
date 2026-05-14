import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_menu_items(driver):

    # Open OrangeHRM
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Login
    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")

    driver.find_element(By.NAME, "password").send_keys("admin123")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for dashboard
    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Admin']")
        )
    )

    menus = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard"
    ]

    for menu in menus:
        element = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//span[normalize-space()='{menu}']")
            )
        )

        assert element.is_displayed()

