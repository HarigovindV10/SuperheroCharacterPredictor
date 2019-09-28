import requests
import urllib.request
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import selenium

def main():

    print("\nOpening the webpage...\n")

    driver = webdriver.Chrome("/Users/harigovindvalsakumar/Downloads/chromedriver")
    driver.get('https://www.deviantart.com/search?q=dc')

    time.sleep(1)

    intial_tag = driver.find_element_by_xpath("//div[@data-hook='content_row-1']")
    intial_tag.find_elements_by_xpath(".//*")[0].click()

    time.sleep(3)

    print("Downloading and saving images...\n")

    for _ in range(1000):

        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)

        url = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div/img").get_attribute("src")

        file_name = driver.find_elements_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[1]/div/div[1]")

        urllib.request.urlretrieve(url, "./Datasets/" + file_name[0].text + ".jpg")

        next_arrow = driver.find_element_by_xpath("//div[@data-hook = 'arrowR']")

        next_arrow.click()

        time.sleep(0.2)

    print("Download complete...\n")

    print("Closing browser instance...\n")

    driver.quit()

if __name__ == "__main__":

    main()
