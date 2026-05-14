from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_text = (
        By.XPATH,
        "//h6[normalize-space()='Dashboard']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def is_dashboard_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.dashboard_text)
        ).is_displayed()

    def click_menu(self, menu_name):

        menu_xpath = f"//span[normalize-space()='{menu_name}']"

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, menu_xpath)
            )
        ).click()