import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import xlrd
import time
import requests
import xml.etree.ElementTree as ET
import json
import win32com.client as com
import datetime
import smtplib
import schedule
rate = 0
transit = 0
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.get("https://www.nike.com/w/nike-by-you-paul-george-shoes-5vxxbz6ealhzy7ok")
driver.maximize_window()
elem = driver.find_element_by_xpath("//*[@id='Wall']/div/div[6]/div[2]/main/section/div/div/div/figure/div/div[1]/div[1]")
if elem.text == "Coming Soon":
    TEXT = "Shoe status is \n" + elem.text
    SERVER = "smtp-mail.outlook.com"
    FROM = "mustafa@bestorq.com"
    TO = ["mualz2007@yahoo.com"] # must be a list
    
    SUBJECT = "PG4 For you"

    PASSWORD = "Ridha6955"

    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM, PASSWORD)
    server.sendmail(FROM, TO, message)
    server.quit()
