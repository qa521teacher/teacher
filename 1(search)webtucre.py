# -----Подключение библиотек----------
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#---------Основной блок кода---------------
link = "https://webtucre.ru/testovaya-stranicza-6/"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

print("1) Ищем элемент строки поиска")
search_string = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/main/article/div/div/div/section[2]/div/div[1]/div/div/div/form/div/input")
print("2) Строка поиска найдена, курсор находится в строке")
print("3) Вносим в строку поиска слово 'Selenium'")
time.sleep(1)
search_string.send_keys("Selenium")
print("4) Слово Selenium успешно напечатано!")
print("5) Ищеем элемент кнопка поиска=button")
button = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/main/article/div/div/div/section[2]/div/div[1]/div/div/div/form/div/button")
print("6) Клик по кнопке поиска")
button.click()
print("Клик выполнен, открылась новая страница")
time.sleep(1)
print("Блок поиска элементов-локаторов завершен, переходим к блоку проверки!")

#--------Блок проверки-------
proverka = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/main/div/article[1]/div/div/header/h2/a").text
print(proverka)
proverka1 = "Selenium1"
if proverka == proverka1:
    print("Тест проверку прошел, УРА! Мы действительно нашли слово 'Selenium'")
else:
    print("Тест проверку не прошел, такого слова на странице нет!!!")
# browser.quit
time.sleep(5)
