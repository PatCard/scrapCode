import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com")

	def test_search_tee(self):
		driver = self.driver
		search_field = driver.find_element(By.NAME,'q')
		search_field.clear() #limpia el campo de búsqueda en caso de que haya algún texto. 
		
		search_field.send_keys('tee') #simulamos la escritura del teclado para poner "tee"
		search_field.submit() #envía los datos ('tee') para que la página muestre los resultados de "tee"
		
	def test_search_salt_shaker(self):
		driver = self.driver
		search_field = driver.find_element(By.NAME,'q')
		
		search_field.send_keys('salt shaker') #escribimos 'salt shaker' en la barra de búsqueda
		search_field.submit() #envíamos la petición

		#hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
		products = driver.find_elements(By.XPATH,'//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#vamos a preguntar si la cantidad de resultados es igual a 1
		self.assertEqual(1, len(products))
		
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)                