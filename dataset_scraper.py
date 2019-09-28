import requests
import urllib.request
import sys
from bs4 import BeautifulSoup as soup
from bs4.element import Tag
import re
#from selenium import webdriver

def get_source( link ):
    r = requests.get( link )
    if r.status_code == 200:
        return soup( r.content , "html.parser")
    else:
        sys.exit( "[~] Invalid Response Received." )

def filter( html ):
    imgs = html.find_all("div",{"role" : "img"})
    #print(imgs)
    if imgs:
        return imgs
    else:
        sys.exit("[~] No images detected on the page.")

def main():
    #driver = webdriver.Chrome("/Users/harigovindvalsakumar/Downloads/chromedriver")
    #driver.get('https://www.deviantart.com/search?q=dc')

    #html = get_source(driver.page_source)
    html = get_source( "https://www.deviantart.com/search?q=dc")
    tags = filter( html )
    imt = []
    for image_tags in tags:
        imt.append(image_tags.find("img"))
    print(len(imt))
    f = open("testfile.txt", "w")
    f.write(str(len(imt)))
    for img_url in imt:
        url = img_url["src"]
        urllib.request.urlretrieve(url, "./Datasets/" + img_url["alt"] + ".jpg")

if __name__ == "__main__":
    main()
