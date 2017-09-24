from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='E:/phantomjs/bin/phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()
print(savedCookies)

driver2 = webdriver.PhantomJS(executable_path='E:/phantomjs/bin/phantomjs')
driver2.get("http://pythonscraping.com")
print(driver2.get_cookies())
driver2.delete_all_cookies()
print(driver2.get_cookies())

for cookie in savedCookies:
    driver2.add_cookie(cookie)
print(driver2.get_cookies())

driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
print(driver2.get_cookies())