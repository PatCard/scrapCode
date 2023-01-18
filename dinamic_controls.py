import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        #driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, "Dynamic Controls").click()

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")
        checkbox.click()

        remove_add_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
        remove_add_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))
        enable_disable_button.click() 

        text_area = driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
        text_area.send_keys("Hola")

        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)