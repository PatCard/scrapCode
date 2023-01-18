import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class helloWorld(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    ##self.driver = webdriver.Chrome(executable_path = r'C://Users/STD412/selenium/chromedriver.exe')
    cls.driver = webdriver.Chrome()
    driver = cls.driver
    driver.implicitly_wait(10)

  def test_hello_world(self):
    driver = self.driver
    driver.get('https://www.emol.com')

  def test_visit_wikipedia(self):
    driver = self.driver
    driver.get('https://www.lun.com')

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

if __name__ == "__main__":
  unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='hello-report'))