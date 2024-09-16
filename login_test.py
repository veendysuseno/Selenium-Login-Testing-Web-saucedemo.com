import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("haitest")
        driver.find_element(By.NAME, "login-button").click()
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        ).text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        # Add assertion to verify successful login
        WebDriverWait(driver, 10).until(
            EC.url_changes("https://www.saucedemo.com/")
        )
        self.assertNotIn("error", driver.current_url)

    def test_empty_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME, "login-button").click()
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        ).text
        self.assertIn("Epic sadface: Username is required", error_message)

if __name__ == '__main__':
    unittest.main()
