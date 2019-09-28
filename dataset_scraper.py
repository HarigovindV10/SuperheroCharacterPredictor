import requests
import urllib.request
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def main():

    print("\nOpening the webpage...\n")

    driver = webdriver.Chrome("/Users/harigovindvalsakumar/Downloads/chromedriver")
    driver.get('https://www.deviantart.com/search?q=dc')
    time.sleep(1)

    print("Scrolling the webpage...\n")

    elem = driver.find_element_by_tag_name("body")

    for _ in range(300):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    div_elements = driver.find_elements_by_xpath("//div[contains(@role, 'img')]")

    imt = []
    file_names = []

    for i in div_elements:
        imt.append(i.find_element_by_xpath("//img").get_attribute("src"))
        file_names.append(i.find_element_by_xpath("//img").get_attribute("alt"))

    print("Downloading files and saving them....\n")

    for img_url,file_name in zip(imt,file_names):
        url = img_url
        urllib.request.urlretrieve(url, "./Datasets/" + file_name + ".jpg")

    print("Dowload complete...\n")

    print("Closing browser instance....\n")

    driver.quit()

if __name__ == "__main__":
    main()
