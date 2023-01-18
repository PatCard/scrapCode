import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        #driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
    
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('Cuantos elementos desea agregar?: '))
        elements_removed = int(input('cuantos elementos desea remover?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        
        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH,'//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("Intentas remover mas elementos de los que ingresaste")
                break

        if total_elements > 0:
            print(f"Hay {total_elements} elementos en pantalla")
        else:
            print("Hay cero elementos en pantalla")

        sleep(3)    


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)