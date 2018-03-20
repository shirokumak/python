import time
from selenium import webdriver

browser = webdriver.Chrome()

url="https://www.victoriassecret.com/bras/shop-all-bras"
browser.get(url)
time.sleep(5)

h2s=browser.find_elements_by_class_name("product-card-wrapper")
if h2s:
    print("要素ありました")
    for h2 in h2s:

        print(h2.text)
    url=    h2.find_element_by_css_selector('h3 > a').get_attribute('href')



else:
    print("要素ありませんでした")

#link = browser.find_element_by_class_name("bras")
#link.click()