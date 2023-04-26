from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = False
#options.add_argument("window_size = 1920x1080")
path = 'C:\PROJECT\chromedriver path\chromedriver.exe'
url = 'https://www.audible.de/search'
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
driver.maximize_window()

book_title = []
book_author = []
book_lenth = []
# pagination
pagination = driver.find_element(
    By.XPATH, '//ul[contains(@class,"agingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
print(pages)
last_page = int(pages[-2].text)
current_page = 1
while current_page <= last_page:
    time.sleep(2)
    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    products = container.find_elements(By.XPATH,
                                       './/li[contains(@class, "productListItem")]')
    for product in products:
        book_title.append(product.find_element(By.XPATH,
                                               './/h3[contains(@class,"bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH,
                                                './/li[contains(@class,"authorLabel")]').text)
        book_lenth.append(product.find_element(By.XPATH,
                                               './/li[contains(@class,"runtimeLabel")]').text)
    current_page = current_page+1

    try:
        next_page = driver.find_element(
            By.XPATH, './/span[contains(@class,"nextButton")]')
        next_page.click()
    except:
        pass


driver.quit()
df_books = pd.DataFrame(
    {'title': book_title, 'author': book_author, 'lenth': book_lenth})
df_books.to_csv('Book_audio.csv', index=False)
