import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class MercadoLibre(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        choose_country = driver.find_element(By.ID, 'CO')
        choose_country.click()

        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        driver.implicitly_wait(3)
        #Mas tarde
        location = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[2]/span')
        location.click()
        driver.implicitly_wait(3)

        #Cookies
        location = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]')        
        location.click()
        driver.implicitly_wait(10)
        
        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        location.click()
        #driver.implicitly_wait(30)
        sleep(3)
        
        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        condition.click()
        #driver.implicitly_wait(3)
        sleep(3)

        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__display-values')
        order_menu.click()
        sleep(3)
        higher_price = driver.find_element(By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        higher_price.click()
        sleep(3)

        '''driver.execute_script("arguments[0].click();", pick_news)
        driver.implicitly_wait(3)'''

        '''driver.execute_script("arguments[0].click();", pick_location)
        driver.implicitly_wait(3)

        pick = driver.find_element_by_class_name('andes-dropdown__trigger')
        driver.execute_script("arguments[0].click();", pick)
        driver.implicitly_wait(10)

        pick_expensive_price = driver.find_elements_by_class_name('andes-list__item-primary')
        pick_expensive_price[2].click()'''

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles, prices)
        '''for x in range(len(articles)):
            print(prices[x]+' -> '+articles[x])'''

    '''@classmethod
    def tearDownClass(cls):
        cls.driver.close()'''

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'ML_report'))