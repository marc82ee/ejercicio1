from selenium import webdriver
from seleniumrequests import Firefox, Chrome

class Browser(object):

    def factory(type, method):
        if method == "post":
            return Chrome()
        if type == "firefox": 
            return webdriver.Firefox()
        elif type == "chrome": 
            return webdriver.Chrome()
        assert 0, "Bad browser creation: " + type
 
    factory = staticmethod(factory)


class Page:
    def __init__(self, name, url, method, browser, domain=None, title=None):
        self.name = name
        self.url = url
        self.domain = domain
        self.title = title
        self.browser = browser
        self.method = method