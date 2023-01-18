import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):

  def setUp(self):
    #self.driver = webdriver.Chrome(executable_path = r"C://Users/STD412/selenium/chromedriver.exe")
    self.driver = webdriver.Chrome()
    driver = self.driver
    driver.get("http://demo-store.seleniumacademy.com/")
    driver.maximize_window()

  def test_search_text_field(self):
    search_field = self.driver.find_element(By.ID, "search")

  def test_search_text_field_by_name(self):
    search_field = self.driver.find_element(By.NAME, "q")

  def test_search_text_field_by_class_name(self):
    search_field = self.driver.find_element(By.CLASS_NAME, "input-text")
    #para buscar
    #document.getElementsByClassName('input-text')

  def test_search_button_enable(self):
    button = self.driver.find_element(By.CLASS_NAME, "button")
    
  def test_count_of_promo_banner_images(self):
    banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
    banners = banner_list.find_elements(By.TAG_NAME, "img")
    #for elem in banner_list:
      #print(banners[elem])
    print("banner_list = ", banner_list)
    print("banners = ", banners)
    self.assertEqual(3, len(banners), "Hola ola")
    #for banner_list in banner_list.find_elements(By.TAG_NAME, "img"):

    #print([banner_list.text for banner_list in banner_list.find_elements(By.TAG_NAME, "img")])


  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
  unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='hello-report'))