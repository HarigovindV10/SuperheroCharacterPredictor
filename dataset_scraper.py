import requests
import urllib.request
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import selenium
import re

def main():

    print("\nOpening the webpage...\n")

    driver = webdriver.Chrome("/Users/harigovindvalsakumar/Downloads/chromedriver")
    driver.get('https://in.pinterest.com/elwink82/dc-characters/')

    time.sleep(3)

    print("Scrolling the webpage...\n")

    elem = driver.find_element_by_tag_name("body")

    for _ in range(100):

        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    time.sleep(2)

    print("Downloading and saving images...\n")

    images = driver.find_elements_by_tag_name('img')

    no_of_images = len(images)

    for image_source in range(len(images)):

        if ((image_source + 1)%100 == 0):

            print("{} / {} Complete...\n".format(image_source + 1, no_of_images))

        url = images[image_source].get_attribute("src")

        file_name = images[image_source].get_attribute("alt")

        file_name = file_name.replace("\\","")

        file_name = file_name.replace("/","")

        file_name = file_name.replace(" ","_")

        urllib.request.urlretrieve(url, "./Datasets/" + file_name[0:20] + ".jpg")



    #window_after = driver.window_handles[0]
    #driver.switch_to.window(window_after)

    """master_tag = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div")
    master_tag_children = master_tag.find_elements_by_xpath(".//*")

    no_master_tag_children = 0

    master_tag_regex = r'.*data-hook="content_row.*"/>'

    for k in master_tag_children:

        #print(k.get_attribute("textContent"))
        matchObj = re.match(master_tag_regex,k.get_attribute("textContent"))
        print(k.get_attribute("textContent"))

        if matchObj:

            no_master_tag_children += 1

    print("nmtg",no_master_tag_children)


    for i in range(no_master_tag_children):

        if i == 1:

            content_row_path = "/html/body/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div[" + str(i+1) + "]/div[1]"

            content_row = driver.find_element_by_xpath(content_row_path)

        else:

            content_row_path = "/html/body/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div[" + str(i+1) + "]/div"

            content_row = driver.find_element_by_xpath(content_row_path)

        no_of_images = 0#len(content_row.find_elements_by_xpath(".//*"))

        content_row_elements = (content_row.find_elements_by_xpath(".//*"))

        img_tag_regex = r'<img.*/>'

        for k in content_row_elements:

            #print(k.get_attribute("textContent"))
            matchObj = re.match(img_tag_regex,k.get_attribute("textContent"))

            if matchObj:

                no_of_images += 1

        print("noi", no_of_images)

        no_of_images /= 4
        #print("crw",content_row_path)

        for j in range(int(no_of_images)):

            img_tag = driver.find_element_by_xpath(content_row_path + "/div["  + str(j+1) +  "]/div/div").get_attribute("textContent")

            #print("it",img_tag.get_attribute("textContent"))

            src_index = img_tag.index("src")

            alt_index = img_tag.index("alt")

            class_index = img_tag.index("class")

            img_source = img_tag[src_index + 5 : len(img_tag) - 3]

            file_name = img_tag[alt_index + 5 : class_index -2]

            print(img_source, "\n", file_name)

            urllib.request.urlretrieve(img_source, "./Datasets/" + file_name + ".jpg")"""


    """url = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div/img").get_attribute("src")

    file_name = driver.find_elements_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[1]/div/div[1]")

    urllib.request.urlretrieve(url, "./Datasets/" + file_name[0].text + ".jpg")

    next_arrow = driver.find_element_by_xpath("//div[@data-hook = 'arrowR']")

    next_arrow.click()

    time.sleep(0.2)"""

    print("Download complete...\n")

    print("Closing browser instance...\n")

    driver.quit()

if __name__ == "__main__":

    main()
