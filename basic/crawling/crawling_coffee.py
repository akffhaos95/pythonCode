import urllib, requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./basic/crawling/data/chromedriver.exe')
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(5)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(3)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[3].click()
time.sleep(3)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li2 = gugun.find_elements_by_tag_name('li')
li2[3].click()
time.sleep(3)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
entire = soup.find('ul', class_='quickSearchResultBoxSidoGugun')
li_list = entire.find_all('li')
for li in li_list:
    print(li.find('strong').text)
    print(li.find('p').text)

# stores = soup.select('li.quickResultLstCon')
# for store in stores:
#    print(store.text)