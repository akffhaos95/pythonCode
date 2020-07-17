import urllib, requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

id = 'akffhaos95'
pw = 'rlaalstjr'

driver = webdriver.Chrome('./basic/crawling/data/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)

# id = driver.find_element_by_name('id').send_keys(log.id)
# pw = driver.find_element_by_name('pw').send_keys(log.pw)
# submit = driver.find_element_by_id('log.login')
# submit.click()

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(3)


#네이버 페이 잔액확인
# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# point = soup.select('dl.my_npoint strong')
# print(point[0].string)
# time.sleep(3)

#메일 리스트 확인
driver.get('https://mail.naver.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title, content = [], []
#보낸 이
title2 = soup.select('div.mTitle')
for i in title2:
    term = i.text.index('에 분류됨메일')
    title.append(i.text[5:term])
#제목
content2 = soup.select('div.subject')
for i in content2:
    content.append(i.select('a')[0].text[11:])

for i in range(len(title)):
    print(title[i] + " ----- " + content[i])
time.sleep(3)

# req = driver.page_source
# soup = BeautifulSoup(req, 'html.parser')
# entire = soup.find('ul', class_='quickSearchResultBoxSidoGugun')
# li_list = entire.find_all('li')
# for li in li_list:
#     print(li.find('strong').text)
#     print(li.find('p').text)

# stores = soup.select('li.quickResultLstCon')
# for store in stores:
#    print(store.text)