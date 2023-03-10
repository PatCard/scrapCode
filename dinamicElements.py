import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class DynamicElement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()     

    def test_name_elements(self):
        driver = self.driver
        options = []
        menu = 5
        tries = 1

        while len(options) < 4:
            options.clear()

            for i in range(menu):
                try:
                    #print(f"i = {i}")
                    option_name = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                    #sleep.time(3)
                    print(option_name)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries += 1
                    driver.refresh()

        print(f"Finished in {tries} tries")

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)