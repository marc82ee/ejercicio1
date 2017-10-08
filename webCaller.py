import requests
import yaml
import unittest

from browser import Browser
from browser import Page
from jproperties import Properties
from urlparse import urlparse

rest_url = "https://jsonplaceholder.typicode.com/posts"

'''
Main function that executes the 4 basic steps needed
'''
def main():
 
    # 1 Read an parse the input from the yaml file
    pages = load_yaml("pages.yaml")

    for page in pages:
        browser_opener = Browser.factory(page.browser, page.method)

        # 2 Open URL
        if (page.method == "get"):
            try:
                browser_opener.get(page.url)
                page.title = browser_opener.title
                page.domain = str(urlparse(page.url).hostname)
                print page.domain
            except Exception as ex:
                print "Exception during opener initalization:%s" % ex.message 
        elif (page.method == "post"):
            browser_opener.request('POST',page.url)
            page.title = browser_opener.title
            page.domain = str(urlparse(page.url).hostname)
        browser_opener.close()

        # 3 Store info to properties file
        prop = Properties()
        prop["url"] = page.url
        prop["domain"] = page.domain
        prop["title"] = page.title

        with open("pages.properties", "a") as f:
            prop.store(f, encoding="utf-8")
        
        # 4 Make request to external API
        payload = {'url': page.url, 'title': page.title}
        try:
            if (page.method == "get"):
                req = requests.get(rest_url, params=payload)
            elif (page.method == "post"):
                req = requests.post(rest_url, params=payload)
            print req.status_code
            print req.text
        except requests.exceptions.RequestException as e: 
            print "Error happened here: %s" %e.message
        
''' 
Function to load the info coming from the yaml fuile 
'''
def load_yaml(file_name):

    # Arrays to store indexes and info loaded from .yaml
    web_pages = []
    page_keys = []
    with open("pages.yaml", 'r') as stream:
        pages_dict = yaml.load(stream)
   
   # Iterate through the info loaded and store the keys
    for page in pages_dict:
        for key, value in page.iteritems():
            print("key: {0} | value: {0} ".format(key, value))
            page_keys.append(key)
    
    # Create page objects to store the info coming from yaml
    i = 0
    for key in page_keys:
        page = Page(name=key, url=pages_dict[i][key]['url'], browser=pages_dict[i][key]['browser'], method=pages_dict[i][key]['method'])
        web_pages.append(page)
        i+=1

    return web_pages

if __name__ == "__main__":
    main()