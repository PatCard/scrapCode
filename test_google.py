#Funciona con google_page.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from google_page import Google

class GoogleTest(unittest.TestCase):

    @classmethod#Decoradores para correr en una sola instancia del navegador
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_search(self):
        google = Google(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)