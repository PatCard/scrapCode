from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Definimos la URL-principal y la ruta al driver de chrome
main_url = 'https://www.google.com/search?q=python' # URL principal
chromedriver = r'C://Users/STD412/selenium/chromedriver.exe'
# Abrimos una ventana con la URL-principal
browser= webdriver.Chrome(chromedriver)
browser.get(main_url)
print ("El titulo de la URL-principal es: %s" %browser.title)
time.sleep(3)
# Hacemos click en el primer enlace y lo abrimos en una pestaña nueva
tab=browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a[1]')
tab.send_keys(Keys.COMMAND + Keys.RETURN)
# Hacemos foco sobre la nueva pestaña
browser.switch_to.window(browser.window_handles[1])
# --- Ahora estamos trabajando en la URL-secundaria
# --- Haz lo que necesites en esa URL-secundaria
print("El titulo de la URL-secundaria es: %s" %browser.title)
time.sleep(3)
# Cerrar la nueva pestaña de URL-secundaria
browser.close()
# Cambiar el foco, para volver a la URL-principal
browser.switch_to.window(browser.window_handles[0])
print("El titulo de la URL (principal) es: %s" %browser.title)
time.sleep(3)
# Cerramos navegador para terminas la sesion
print("Cerramos navegador")
browser.close()