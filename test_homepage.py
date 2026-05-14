from config import BASE_URL

def test_home_page(driver):

    driver.get(BASE_URL)

    assert "OrangeHRM" in driver.title
