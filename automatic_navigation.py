import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://google.com/")

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        #como buena práctica se recomienda limpiar los campos
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)