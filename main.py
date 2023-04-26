from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.by import By

options = Options()
path = 'C:\PROJECT\chromedriver path\chromedriver.exe'
url = 'https://www.audible.de/search'
chrome_driver_path = path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
driver.maximize_window()
container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
products = container.find_elements(By.XPATH,
                                   './/li[contains(@class, "productListItem")]')
book_title = []
book_author = []
book_lenth = []
for product in products:
    book_title.append(product.find_element(By.XPATH,
                                           './/h3[contains(@class,"bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH,
                                            './/li[contains(@class,"authorLabel")]').text)
    book_lenth.append(product.find_element(By.XPATH,
                                           './/li[contains(@class,"runtimeLabel")]').text)


driver.quit()
df_books = pd.DataFrame(
    {'title': book_title, 'author': book_author, 'lenth': book_lenth})
df_books.to_csv('Books.csv', index=False)
