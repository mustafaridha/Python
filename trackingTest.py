import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import xlrd
import csv
import pandas as pd
import time
from datetime import datetime
import numpy as np
import requests
import xml.etree.ElementTree as ET
import json
rate = 0
transit = 0
driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.get("https://ltl.upsfreight.com/home/")
driver.maximize_window()
elem = driver.find_element_by_xpath("//*[@id='app_login_btnLog']")
elem.send_keys(Keys.RETURN)
driver.find_element_by_xpath("/html/body").click()
time.sleep(3)
elem = driver.find_element_by_id("email")
elem.clear()
elem.send_keys("rexxon1000")
elem = driver.find_element_by_id("pwd")
elem.clear()
elem.send_keys("del1604")
elem = driver.find_element_by_id("submitBtn")
elem.send_keys(Keys.RETURN)
driver.find_element_by_link_text("Rates").click()
elem = driver.find_element_by_id("cContent_Right_OrgZip")
elem.send_keys("68507")
elem = driver.find_element_by_id("cContent_Right_DestZip")
elem.send_keys("66062")
elem = driver.find_element_by_id("cContent_Right_shipDate")
elem.clear()
elem.send_keys("01/10/2020")
driver.find_element_by_id("cContent_Right_requestQuoteNumber").click()
elem = driver.find_element_by_id("cContent_Right_cmdNmfc1_ddClassNum")
elem.send_keys("55")
elem = driver.find_element_by_id("cContent_Right_cmdNmfc1_txtcommodityWeight")
elem.send_keys("125")
elem = driver.find_element_by_id("cContent_Right_btnSubmit")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_xpath("//*[@id='cContent_Right_lblServiceDays']")
transit = elem.text
elem = driver.find_element_by_xpath("//*[@id='cContent_Right_lblltltotalAmount']")
rate = elem.text
elem = driver.find_element_by_xpath("//*[@id='cContent_Right_lblQuoteNbr']")
quote = elem.text
