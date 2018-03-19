url = 'https://www.victoriassecret.com/accessories/all-bags'

from selenium import webdriver
browser = webdriver.Chrome()


browser.implicitly_wait(1)

browser.get(url)

links = browser.find_elements_by_css_selector('.product-card-wrapper > a')
print(links)