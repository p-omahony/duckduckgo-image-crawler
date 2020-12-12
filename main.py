from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from os import popen
import time

keywords, destination_path, limit = input('keywords : '), input('destination path : '), int(input('limit : '))

start_url, end_url, middle_url = "https://duckduckgo.com/?q=", "&iar=images&iax=images&ia=images", keywords.replace(' ', '+')
url = start_url+middle_url+end_url

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

images = driver.find_elements_by_xpath("//img[@class='tile--img__img  js-lazyload']")
c=0
for image in images[:limit] :
    image.click()
    time.sleep(1)
    link = driver.find_element_by_xpath("//a[@class='c-detail__btn c-detail__btn--bottom btn js-image-detail-link']").get_attribute('href')
    if '.jpg' in link :
        popen('wget '+link+' -O '+destination_path+'/'+keywords.replace(' ','_')+str(c)+'.jpg -q -o /dev/null')
        c+=1

driver.quit()
