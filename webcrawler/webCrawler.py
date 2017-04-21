import webbrowser
from selenium import webdriver
from selenium import *
import time
import requests

url = 'http://www.phptravels.net/admin'
values = {
    'email': 'admin@phptravels.com',
    'password': 'demoadmin'
}
r = requests.post(url, data=values)
print r.content



# # Fill in your details here to be posted to the login form.
# payload = {
#     'email': 'admin@phptravels.com',
#     'password': 'demoadmin'
# }

# # Use 'with' to ensure the session context is closed after use.
# with requests.Session() as s:
#     p = s.post('http://www.phptravels.net/admin', data=payload)
#     # print the html returned or something more intelligent to see if it's a successful login page.
#     print p.text

#     # An authorised request.
#     r = s.get('A protected web page url')
#     print r.text

# chromedriver = 'C:\\chromedriver.exe'
# browser = webdriver.Chrome(chromedriver)
# browser.get('http://www.example.com')

# webbrowser.open("http://www.phptravels.net/admin")

# username = selenium.find_element_by_id("email")
# password = selenium.find_element_by_id("password")
# time.delay(3)
# username.send_keys("admin@phptravels.com")
# time.delay(2)
# password.send_keys("demoadmin")
# time.delay(2)
# selenium.find_element_by_name("Login").click()