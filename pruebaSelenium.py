from selenium import webdriver
#driver = webdriver.Chrome(executable_path = r'C://Users/STD412/selenium/chromedriver.exe')
driver = webdriver.Chrome()
driver.get("https://www.platzi.com")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip())