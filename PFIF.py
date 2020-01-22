import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd
import pandas as pd
import numpy as np
while True:
    loggingFile = ""
    email = ""
    xlsFile = ""
    loggingFile = input("Please enter the log file name : ")
    logging.basicConfig(format='%(message)s',filename=loggingFile+".csv",level=logging.INFO)
    logging.info("Item Number, Website Price, PFIF Price")
    email = input("Please enter the customer email: ")
    xlsFile = input("Please enter the input file name : ")
    driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
    driver.get("https://bestorq.com/employee.asp")
    driver.maximize_window()
    elem = driver.find_element_by_id("FormPass")
    elem.clear()
    elem.send_keys("treats11")
    elem.send_keys(Keys.RETURN)
    driver.find_element_by_id("enterOrder").click()
    elem = driver.find_element_by_id("cust_email")
    elem.clear()
    elem.send_keys(email)
    elem.send_keys(Keys.RETURN)
    driver.find_element_by_id("multCorrect").click()
    book  = xlrd.open_workbook(xlsFile+".xlsx")
    sheet = book.sheet_by_index(1)
    num_cols = sheet.nrows
    part3lx = True
    part3LG = True
    part3L = True
    partSPZ = True
    partSPZX = True
    partSPA = True
    partSPAX = True
    partSPBBand = True
    partSPBX = True
    partSPB = True
    partSPCBand = True
    partSPC = True
    partSPCX = True
    partxl = True
    partb142 = True
    partB165 = True
    partCB165 = True
    partB170 = True
    partB175 = True
    partw30pk = True
    part1760 = True
    part1778 = True
    partXH = True
    partXXH = True
    partHD = True
    partH = True
    part3M = True
    part5MD = True
    part5M = True
    part8MD = True
    part8M = True
    part14MD = True
    part14M = True
    part20M = True
    partAX = True
    partAA = True
    partALG = True
    partA = True
    partBXBand = True
    partBX = True
    partBB = True
    partBLG = True
    partBBAND = True
    partB = True
    partCX = True
    partCC = True
    partCBAND = True
    partC = True
    partLD = True
    partL = True
    partDBAND = True
    partD = True
    partE = True
    part3VX = True
    part3VXBand = True
    part3VK = True
    part3VBand = True
    part3V = True
    part5VX = True
    part5VXBand = True
    part5VK = True
    part5VBand = True
    part5V = True
    part8VX = True
    part8VK = True
    part8VBand = True
    part8V = True
    partJpart = True


    for i in range(6,num_cols):
        item = sheet.cell_value(rowx=i, colx=2)
        price = sheet.cell_value(rowx=i,colx=5)
        price = round(price,2)
        print(item)
        if "3L" in item:
            if "X" in item:
                if part3lx == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[18]/td[3]/select/option[1]")
                    if elem.text != item[3:]:
                        elem = driver.find_element_by_name("pn3LX")
                        elem.send_keys(item[3:])
                    elem = driver.find_element_by_id("price80")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("3LXprice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("3LXreset")
                    elem.send_keys(Keys.RETURN)
                    part3lx = False
            elif "LG" in item:
                if part3LG == True:
                    driver.find_element_by_id("lawn").click()
                    ind = item.find("LG")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[53]/td[3]/select/option[1]")
                    if elem.text != item[2:ind]:
                        elem = driver.find_element_by_name("pn3LLG")
                        elem.send_keys(item[2:ind])
                    elem = driver.find_element_by_id("price52")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("3LLGPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("3LLGreset")
                    elem.send_keys(Keys.RETURN)
                    part3LG = False
            else:
                if part3L == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[9]/td[3]/select/option[1]")
                    if elem.text != item[2:]:
                        elem = driver.find_element_by_name("pn3L")
                        elem.send_keys(item[2:])
                    elem = driver.find_element_by_id("price9")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("3Lprice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("3Lreset")
                    elem.send_keys(Keys.RETURN)
                    part3L = False

        elif "SPZ" in item:
            if "X" in item:
                if partSPZX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[38]/td[3]/select/option[1]")
                    if elem.text != item[4:]:
                        elem = driver.find_element_by_name("pnSPZX")
                        elem.send_keys(item[4:])
                    elem = driver.find_element_by_id("price37")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPZXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPZXreset")
                    elem.send_keys(Keys.RETURN)
                    partSPZX = False
            else:
                if partSPZ == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[37]/td[3]/select/option[1]")
                    if elem.text != item[3:]:
                        elem = driver.find_element_by_name("pnSPZ")
                        elem.send_keys(item[3:])
                    elem = driver.find_element_by_id("price36")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPZPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPZreset")
                    elem.send_keys(Keys.RETURN)
                    partSPZ = False
        elif "SPA" in item:
            if "X" in item:
                if partSPAX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[40]/td[3]/select/option[1]")
                    if elem.text != item[4:]:
                        elem = driver.find_element_by_name("pnSPAX")
                        elem.send_keys(item[4:])
                    elem = driver.find_element_by_id("price39")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPAXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPAXreset")
                    elem.send_keys(Keys.RETURN)
                    partSPAX = False
            else:
                if partSPA == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[39]/td[3]/select/option[1]")
                    if elem.text != item[3:]:
                        elem = driver.find_element_by_name("pnSPA")
                        elem.send_keys(item[3:])
                    elem = driver.find_element_by_id("price38")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPAPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPAreset")
                    elem.send_keys(Keys.RETURN)
                    partSPA = False
        elif "SPB" in item:
            if "/" in item:
                if partSPBBand == True:
                    driver.find_element_by_id("b").click()
                    ind = item.find("/")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[45]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnSPBRibs")
                        elem.send_keys(item[0:ind])
                    ind = item.find("B") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[45]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pnSPBBand")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price44")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPBBANDPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPBBANDreset")
                    elem.send_keys(Keys.RETURN)
                    partSPBBand = False
            elif "X" in item:
                if partSPBX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[42]/td[3]/select/option[1]")
                    if elem.text != item[4:]:
                        elem = driver.find_element_by_name("pnSPBX")
                        elem.send_keys(item[4:])
                    elem = driver.find_element_by_id("price41")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPBXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPBXreset")
                    elem.send_keys(Keys.RETURN)
                    partSPBX = False
            else:
                if partSPB == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[41]/td[3]/select/option[1]")
                    if elem.text != item[3:]:
                        elem = driver.find_element_by_name("pnSPB")
                        elem.send_keys(item[3:])
                    elem = driver.find_element_by_id("price40")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPBPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPBreset")
                    elem.send_keys(Keys.RETURN)
                    partSPB = False
        elif "SPC" in item:
            if "/" in item:
                if partSPCBand == True:
                    driver.find_element_by_id("b").click()
                    ind = item.find("/")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[46]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnSPCRibs")
                        elem.send_keys(item[0:ind])
                    ind = item.find("C") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[46]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pnSPCBand")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price45")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPCBANDPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPCBANDreset")
                    elem.send_keys(Keys.RETURN)
                    partSPCBand = False
            elif "X" in item:
                if partSPCX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[44]/td[3]/select/option[1]")
                    if elem.text != item[4:]:
                        elem = driver.find_element_by_name("pnSPCX")
                        elem.send_keys(item[4:])
                    elem = driver.find_element_by_id("price43")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPCXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPCXreset")
                    elem.send_keys(Keys.RETURN)
                    partSPCX = False
            else:
                if partSPC == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[43]/td[3]/select/option[1]")
                    if elem.text != item[3:]:
                        elem = driver.find_element_by_name("pnSPC")
                        elem.send_keys(item[3:])
                    elem = driver.find_element_by_id("price42")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("SPCPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("SPCreset")
                    elem.send_keys(Keys.RETURN)
                    partSPC = False
        elif "XL" in item and "M" not in item:
            if partxl == True:
                driver.find_element_by_id("time").click()
                ind = item.find("X")
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[65]/td[3]/select[1]/option[1]")
                if elem.text != item[0:ind]:
                    elem = driver.find_element_by_name("pnXL")
                    elem.send_keys(item[0:ind])
                ind = item.find("L") + 1
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[65]/td[3]/select[2]/option[1]")
                if elem.text != item[ind:]:
                    elem = driver.find_element_by_name("widthXL")
                    elem.send_keys(item[ind:])
                elem = driver.find_element_by_id("price64")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("XLPrice")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                if float(priceString) != float(price):
                    logging.info("{0},{1},{2}".format(item, priceString, price))
                elem = driver.find_element_by_name("XLreset")
                elem.send_keys(Keys.RETURN)
                partxl = False
        elif "61CCB142" in item:
            if partb142 == True:
                driver.find_element_by_id("other").click()
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[49]/td[3]/select/option[1]")
                elem = driver.find_element_by_id("price48")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("CCBPrice")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                if float(priceString) != float(price):
                    logging.info("{0},{1},{2}".format(item, priceString, price))
                elem = driver.find_element_by_name("CCBreset")
                elem.send_keys(Keys.RETURN)
                partb142 = False
        elif "XH" in item:
            if "XX" in item:
                if partXXH == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("X")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[69]/td[3]/select[1]/option")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnXXH")
                        elem.send_keys(item[0:ind])
                    ind = item.find("H") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[69]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthXXH")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price82")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("XXHPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("XXHreset")
                    elem.send_keys(Keys.RETURN)
                    partXXH = False
            else:
                if partXH == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("X")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[68]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnXH")
                        elem.send_keys(item[0:ind])
                    ind = item.find("H") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[68]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthXH")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price67")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("XHPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("XHreset")
                    elem.send_keys(Keys.RETURN)
                    partXH = False
        elif "H" in item and "X" not in item:
            if "D" in item:
                if partHD == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("D") + 1
                    ind2 = item.find("H")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[71]/td[3]/select[1]/option[1]")
                    if elem.text != item[ind:ind2]:
                        elem = driver.find_element_by_name("pnDH")
                        elem.send_keys(item[ind:ind2])
                    ind = item.find("H") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[71]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthDH")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price69")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("DHPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("DHreset")
                    elem.send_keys(Keys.RETURN)
                    partHD = False
            else:
                if partH == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("X")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[67]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnH")
                        elem.send_keys(item[0:ind])
                    ind = item.find("H") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[67]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthH")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price66")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("HPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("Hreset")
                    elem.send_keys(Keys.RETURN)
                    partH = False
        elif "3M" in item and "XL" not in item:
            if part3M == True:
                driver.find_element_by_id("time").click()
                ind = item.find("-3")
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[72]/td[3]/select[1]/option[1]")
                if elem.text != item[0:ind]:
                    elem = driver.find_element_by_name("pn3M")
                    elem.send_keys(item[0:ind])
                ind = item.find("M-") + 2
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[72]/td[3]/select[2]/option[1]")
                if elem.text != item[ind:]:
                    elem = driver.find_element_by_name("width3M")
                    elem.send_keys(item[ind:])
                elem = driver.find_element_by_id("price70")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("3MPrice")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                if float(priceString) != float(price):
                    logging.info("{0},{1},{2}".format(item, priceString, price))
                elem = driver.find_element_by_name("3Mreset")
                elem.send_keys(Keys.RETURN)
                part3M = False
        elif "5M" in item and "XL" not in item:
            if "D" in item:
                if part5MD == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("D") + 1
                    ind2 = item.find("-5")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[77]/td[3]/select[1]/option[1]")
                    if elem.text != item[ind:ind2]:
                        elem = driver.find_element_by_name("pnD5M")
                        elem.send_keys(item[ind:ind2])
                    ind = item.find("M-") + 2
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[77]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthD5M")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price74")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("D5MPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("D5Mreset")
                    elem.send_keys(Keys.RETURN)
                    part5MD = False
            else:
                if part5M == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("-5")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[73]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pn5M")
                        elem.send_keys(item[0:ind])
                    ind = item.find("M-") + 2
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[73]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("width5M")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price71")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("5MPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("5Mreset")
                    elem.send_keys(Keys.RETURN)
                    part5M = False
        elif "8M" in item and "XL" not in item and "7w12pk" not in item and "2w30pk" not in item:
            if "D" in item:
                if part8MD == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("D") + 1
                    ind2 = item.find("-8")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[78]/td[3]/select[1]/option[1]")
                    if elem.text != item[ind:ind2]:
                        elem = driver.find_element_by_name("pnD8M")
                        elem.send_keys(item[ind:ind2])
                    ind = item.find("M-") + 2
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[78]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthD8M")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price75")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("D8MPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("D8Mreset")
                    elem.send_keys(Keys.RETURN)
                    part8MD = False
            else:
                if part8M == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("-8")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[74]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pn8M")
                        elem.send_keys(item[0:ind])
                    ind = item.find("M-") + 2
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[74]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("width8M")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price72")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("8MPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("8Mreset")
                    elem.send_keys(Keys.RETURN)
                    part8M = False
        elif "14M" in item and "XL" not in item and "7w12pk" not in item:
            if "D" in item:
                if part14MD == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("D") + 1
                    ind2 = item.find("-14")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[79]/td[3]/select[1]/option[1]")
                    if elem.text != item[ind:ind2]:
                        elem = driver.find_element_by_name("pnD14M")
                        elem.send_keys(item[ind:ind2])
                    ind = item.find("M-") + 2
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[79]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthD14M")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price76")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("D14MPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("D14Mreset")
                    elem.send_keys(Keys.RETURN)
                    part14MD = False
            else:
                if part14M == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("-14")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[75]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pn14M")
                        elem.send_keys(item[0:ind])
                    ind = item.find("M-") + 2
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[75]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("width14M")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price73")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("14MPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("14Mreset")
                    elem.send_keys(Keys.RETURN)
                    part14M = False
        elif "20M" in item and "XL" not in item:
            if part20M == True:
                driver.find_element_by_id("time").click()
                ind = item.find("-20")
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[76]/td[3]/select[1]/option[1]")
                if elem.text != item[0:ind]:
                    elem = driver.find_element_by_name("pn14M")
                    elem.send_keys(item[0:ind])
                ind = item.find("M-") + 2
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[76]/td[3]/select[2]/option[1]")
                if elem.text != item[ind:]:
                    elem = driver.find_element_by_name("width14M")
                    elem.send_keys(item[ind:])
                elem = driver.find_element_by_id("price83")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("20MPrice")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                if float(priceString) != float(price):
                    logging.info("{0},{1},{2}".format(item, priceString, price))
                elem = driver.find_element_by_name("20Mreset")
                elem.send_keys(Keys.RETURN)
                part20M = False
        elif "A" in item:
            if "X" in item:
                if partAX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[12]/td[3]/select/option[1]")
                    if elem.text != item[2:]:
                        elem = driver.find_element_by_name("pnAX")
                        elem.send_keys(item[2:])
                    elem = driver.find_element_by_id("price12")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("AXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("AXreset")
                    elem.send_keys(Keys.RETURN)
                    partAX = False
            elif "AA" in item:
                if partAA == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[31]/td[3]/select/option[1]")
                    if elem.text != item[2:]:
                        elem = driver.find_element_by_name("pnAA")
                        elem.send_keys(item[2:])
                    elem = driver.find_element_by_id("price30")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("AAPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("AAreset")
                    elem.send_keys(Keys.RETURN)
                    partAA = False
            elif "LG" in item:
                if partALG == True:
                    driver.find_element_by_id("lawn").click()
                    ind = item.find("LG")
                    ind2 = item.find("A") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[51]/td[3]/select/option[1]")
                    if elem.text != item[ind2:ind]:
                        elem = driver.find_element_by_name("pnALG")
                        elem.send_keys(item[ind2:ind])
                    elem = driver.find_element_by_id("price50")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("ALGPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("ALGreset")
                    elem.send_keys(Keys.RETURN)
                    partALG = False
            else:
                if partA == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[1]/td[3]/select/option[1]")
                    if "or" in item:
                        ind = item.find("or")
                        if elem.text != item[1:ind]:
                            elem = driver.find_element_by_name("pnA")
                            elem.send_keys(item[1:ind])
                    else:
                        if elem.text != item[1:]:
                            elem = driver.find_element_by_name("pnA")
                            elem.send_keys(item[1:])
                    elem = driver.find_element_by_id("price1")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("APrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("Areset")
                    elem.send_keys(Keys.RETURN)
                    partA = False
        elif "B" in item:
            if "X" in item:
                if "/" in item:
                    if partBXBand == True:
                        driver.find_element_by_id("b").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[20]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pnBXRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("X") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[20]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pnBXband")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price19")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("BXBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("BXBANDreset")
                        elem.send_keys(Keys.RETURN)
                        partBXBand = False
                else:
                    if item[2:] != "195":
                        if partBX == True:
                            driver.find_element_by_id("raw").click()
                            elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[13]/td[3]/select/option[1]")
                            if elem.text != item[2:]:
                                elem = driver.find_element_by_name("pnBX")
                                elem.send_keys(item[2:])
                            elem = driver.find_element_by_id("price13")
                            elem.send_keys(Keys.RETURN)
                            elem = driver.find_element_by_id("BXPrice")
                            priceString = elem.text
                            priceString = priceString.replace(",", "")
                            priceString = priceString.replace("$","")
                            if float(priceString) != float(price):
                                logging.info("{0},{1},{2}".format(item, priceString, price))
                            elem = driver.find_element_by_name("BXreset")
                            elem.send_keys(Keys.RETURN)
                            partBX = False
                    else:
                        driver.find_element_by_id("raw").click()
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[13]/td[3]/select/option[1]")
                        if elem.text != item[2:]:
                            elem = driver.find_element_by_name("pnBX")
                            elem.send_keys(item[2:])
                        elem = driver.find_element_by_id("price13")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("BXPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("BXreset")
                        elem.send_keys(Keys.RETURN)
            elif "BB" in item:
                if partBB == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[32]/td[3]/select[1]/option[1]")
                    if elem.text != item[2:]:
                        elem = driver.find_element_by_name("pnBB")
                        elem.send_keys(item[2:])
                    elem = driver.find_element_by_id("price31")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("BBPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("BBreset")
                    elem.send_keys(Keys.RETURN)
                    partBB = False
            elif "LG" in item:
                if partBLG == True:
                    driver.find_element_by_id("lawn").click()
                    ind = item.find("LG")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[52]/td[3]/select/option[1]")
                    if elem.text != item[1:ind]:
                        elem = driver.find_element_by_name("pnBLG")
                        elem.send_keys(item[1:ind])
                    elem = driver.find_element_by_id("price51")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("BLGPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("BLGreset")
                    elem.send_keys(Keys.RETURN)
                    partBLG = False
            elif "/" in item:
                if partBBAND == True:
                    driver.find_element_by_id("b").click()
                    ind = item.find("/")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[19]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnBRibs")
                        elem.send_keys(item[0:ind])
                    ind = item.find("B") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[19]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pnBBand")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price18")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("BBANDPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("BBANDreset")
                    elem.send_keys(Keys.RETURN)
                    partBBAND = False
            else:
                if partB == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[2]/td[3]/select/option[1]")
                    if "or" in item:
                        ind = item.find("or")
                        if elem.text != item[1:ind]:
                            elem = driver.find_element_by_name("pnB")
                            elem.send_keys(item[1:ind])
                    else:
                        if elem.text != item[1:]:
                            elem = driver.find_element_by_name("pnB")
                            elem.send_keys(item[1:])
                    elem = driver.find_element_by_id("price2")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("BPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("Breset")
                    elem.send_keys(Keys.RETURN)
                    partB = False
        elif "C" in item:
            if "X" in item:
                if partCX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[14]/td[3]/select/option[1]")
                    ind = item.find("X") + 1
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pnCX")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price14")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("CXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("CXreset")
                    elem.send_keys(Keys.RETURN)
                    partCX = False
            elif "CC" in item:
                if partCC == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[33]/td[3]/select/option[1]")
                    if elem.text != item[2:]:
                        elem = driver.find_element_by_name("pnCC")
                        elem.send_keys(item[2:])
                    elem = driver.find_element_by_id("price32")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("CCPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("CCreset")
                    elem.send_keys(Keys.RETURN)
                    partCC = False
            elif "/" in item:
                if partCBAND == True:
                    driver.find_element_by_id("b").click()
                    ind = item.find("/")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[21]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnCRibs")
                        elem.send_keys(item[0:ind])
                    ind = item.find("C") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[21]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pnCBand")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price20")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("CBANDPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("CBANDreset")
                    elem.send_keys(Keys.RETURN)
                    partCBAND = False
            else:
                if partC == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[3]/td[3]/select/option[1]")
                    if elem.text != item[1:]:
                        elem = driver.find_element_by_name("pnC")
                        elem.send_keys(item[1:])
                    elem = driver.find_element_by_id("price3")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("CPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("Creset")
                    elem.send_keys(Keys.RETURN)
                    partC = False
        elif "L" in item and "M" not in item:
            if "D" in item:
                if partLD == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("D") + 1
                    ind2 = item.find("L")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[70]/td[3]/select[1]/option[1]")
                    if elem.text != item[ind:ind2]:
                        elem = driver.find_element_by_name("pnDL")
                        elem.send_keys(item[ind:ind2])
                    ind = item.find("L") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[70]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthDL")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price68")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("DLPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("DLreset")
                    elem.send_keys(Keys.RETURN)
                    partLD = False
            else:
                if partL == True:
                    driver.find_element_by_id("time").click()
                    ind = item.find("L")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[66]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnL")
                        elem.send_keys(item[0:ind])
                    ind = item.find("L") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[66]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("widthL")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price65")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("LPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("Lreset")
                    elem.send_keys(Keys.RETURN)
                    partL = False
        elif "D" in item:
            if "/" in item:
                if partDBAND == True:
                    driver.find_element_by_id("b").click()
                    ind = item.find("/")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[22]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pnDRibs")
                        elem.send_keys(item[0:ind])
                    ind = item.find("D") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[22]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pnDBand")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price21")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("DBANDPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("DBANDreset")
                    elem.send_keys(Keys.RETURN)
                    partDBAND = False
            else:
                if partD == True:
                    driver.find_element_by_id("wrapped").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[4]/td[3]/select/option[1]")
                    if elem.text != item[1:]:
                        elem = driver.find_element_by_name("pnD")
                        elem.send_keys(item[1:])
                    elem = driver.find_element_by_id("price4")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("DPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("Dreset")
                    elem.send_keys(Keys.RETURN)
                    partD = False
        elif "E" in item:
            if partE == True:
                driver.find_element_by_id("wrapped").click()
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[5]/td[3]/select/option[1]")
                if elem.text != item[1:]:
                    elem = driver.find_element_by_name("pnE")
                    elem.send_keys(item[1:])
                elem = driver.find_element_by_id("price5")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("EPrice")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                if float(priceString) != float(price):
                    logging.info("{0},{1},{2}".format(item, priceString, price))
                elem = driver.find_element_by_name("Ereset")
                elem.send_keys(Keys.RETURN)
                partE = False
        elif "3V" in item:
            if "X" in item:
                if "/" in item:
                    if part3VXBand == True:
                        driver.find_element_by_id("b").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[24]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn3VXRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("X") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[24]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn3VXBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price23")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("3VXBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("3VXBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part3VXBand = False
                else:
                    if part3VX == True:
                        driver.find_element_by_id("raw").click()
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[15]/td[3]/select/option[1]")
                        if elem.text != item[3:]:
                            elem = driver.find_element_by_name("pn3VX")
                            elem.send_keys(item[3:])
                        elem = driver.find_element_by_id("price15")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("3VXPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("3VXreset")
                        elem.send_keys(Keys.RETURN)
                        part3VX = False
            elif "K" in item:
                if part3VK == True:
                        driver.find_element_by_id("kevlar").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[28]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn3VKRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("K") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[28]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn3VKBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price27")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("3VKBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("3VKBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part3VK = False
            else:
                if "/" in item:
                    if part3VBand == True:
                        driver.find_element_by_id("b").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[23]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn3VRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("V") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[23]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn3VBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price22")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("3VBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("3VBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part3VBand = False
                else:
                    if part3V == True:
                        driver.find_element_by_id("wrapped").click()
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[6]/td[3]/select/option[1]")
                        if elem.text != item[2:]:
                            elem = driver.find_element_by_name("pn3V")
                            elem.send_keys(item[2:])
                        elem = driver.find_element_by_id("price6")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("3VPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("3Vreset")
                        elem.send_keys(Keys.RETURN)
                        part3V = False
        elif "5V" in item:
            if "X" in item:
                if "/" in item:
                    if part5VXBand == True:
                        driver.find_element_by_id("b").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[25]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn5VXRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("X") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[25]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn5VXBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price24")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("5VXBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("5VXBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part5VXBand = False
                else:
                    if item[3:] != "2000":
                        if part5VX == True:
                            driver.find_element_by_id("raw").click()
                            elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[16]/td[3]/select/option[1]")
                            if elem.text != item[3:]:
                                elem = driver.find_element_by_name("pn5VX")
                                elem.send_keys(item[3:])
                            elem = driver.find_element_by_id("price16")
                            elem.send_keys(Keys.RETURN)
                            elem = driver.find_element_by_id("5VXPrice")
                            priceString = elem.text
                            priceString = priceString.replace(",", "")
                            priceString = priceString.replace("$","")
                            if float(priceString) != float(price):
                                logging.info("{0},{1},{2}".format(item, priceString, price))
                            elem = driver.find_element_by_name("5VXreset")
                            elem.send_keys(Keys.RETURN)
                            part5VX = False
                    else:
                        driver.find_element_by_id("raw").click()
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[16]/td[3]/select/option[1]")
                        if elem.text != item[3:]:
                            elem = driver.find_element_by_name("pn5VX")
                            elem.send_keys(item[3:])
                        elem = driver.find_element_by_id("price16")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("5VXPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("5VXreset")
                        elem.send_keys(Keys.RETURN)
            elif "K" in item:
                if part5VK == True:
                        driver.find_element_by_id("kevlar").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[29]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn5VKRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("K") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[29]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn5VKBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price28")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("5VKBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("5VKBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part5VK = False
            else:
                if "/" in item:
                    if part5VBand == True:
                        driver.find_element_by_id("b").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[26]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn5VRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("V") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[26]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn5VBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price25")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("5VBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("5VBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part5VBand = False
                else:
                    if part5V == True:
                        driver.find_element_by_id("wrapped").click()
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[7]/td[3]/select/option[1]")
                        if elem.text != item[2:]:
                            elem = driver.find_element_by_name("pn5V")
                            elem.send_keys(item[2:])
                        elem = driver.find_element_by_id("price7")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("5VPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("5Vreset")
                        elem.send_keys(Keys.RETURN)
                        part5V = False
        elif "2w30pk" in item:
            if partw30pk == True:
                print
                driver.find_element_by_id("other").click()
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[50]/td[3]/select/option[1]")
                elem = driver.find_element_by_id("price49")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("MILLPrice")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                elem = driver.find_element_by_name("MILLreset")
                elem.send_keys(Keys.RETURN)
                partw30pk = False
        elif "8V" in item:
            if "X" in item:
                if part8VX == True:
                    driver.find_element_by_id("raw").click()
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[17]/td[3]/select/option[1]")
                    if elem.text != item[3:]:
                        elem = driver.find_element_by_name("pn8VX")
                        elem.send_keys(item[3:])
                    elem = driver.find_element_by_id("price17")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("8VXPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("8VXreset")
                    elem.send_keys(Keys.RETURN)
                    part8VX = False
            elif "K" in item:
                if part8VK == True:
                    driver.find_element_by_id("kevlar").click()
                    ind = item.find("/")
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[30]/td[3]/select[1]/option[1]")
                    if elem.text != item[0:ind]:
                        elem = driver.find_element_by_name("pn8VKRibs")
                        elem.send_keys(item[0:ind])
                    ind = item.find("K") + 1
                    elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[30]/td[3]/select[2]/option[1]")
                    if elem.text != item[ind:]:
                        elem = driver.find_element_by_name("pn8VKBand")
                        elem.send_keys(item[ind:])
                    elem = driver.find_element_by_id("price29")
                    elem.send_keys(Keys.RETURN)
                    elem = driver.find_element_by_id("8VKBANDPrice")
                    priceString = elem.text
                    priceString = priceString.replace(",", "")
                    priceString = priceString.replace("$","")
                    if float(priceString) != float(price):
                        logging.info("{0},{1},{2}".format(item, priceString, price))
                    elem = driver.find_element_by_name("8VKBANDreset")
                    elem.send_keys(Keys.RETURN)
                    part8VK = False
            else:
                if "/" in item:
                    if part8VBand == True:
                        driver.find_element_by_id("b").click()
                        ind = item.find("/")
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[27]/td[3]/select[1]/option[1]")
                        if elem.text != item[0:ind]:
                            elem = driver.find_element_by_name("pn8VRibs")
                            elem.send_keys(item[0:ind])
                        ind = item.find("V") + 1
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[27]/td[3]/select[2]/option[1]")
                        if elem.text != item[ind:]:
                            elem = driver.find_element_by_name("pn8VBand")
                            elem.send_keys(item[ind:])
                        elem = driver.find_element_by_id("price26")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("8VBANDPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("8VBANDreset")
                        elem.send_keys(Keys.RETURN)
                        part8VBand = False
                else:
                    if part8V == True:
                        driver.find_element_by_id("wrapped").click()
                        elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[8]/td[3]/select/option[1]")
                        if elem.text != item[2:]:
                            elem.send_keys(item[2:])
                        elem = driver.find_element_by_id("price8")
                        elem.send_keys(Keys.RETURN)
                        elem = driver.find_element_by_id("8VPrice")
                        priceString = elem.text
                        priceString = priceString.replace(",", "")
                        priceString = priceString.replace("$","")
                        if float(priceString) != float(price):
                            logging.info("{0},{1},{2}".format(item, priceString, price))
                        elem = driver.find_element_by_name("8Vreset")
                        elem.send_keys(Keys.RETURN)
                        part8V = False
        elif "J" in item:
            if partJpart == True:
                driver.find_element_by_id("v").click()
                ind = item.find("J")
                elem = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[34]/td[3]/select/option[1]")
                if elem.text != item[0:ind]:
                    elem = driver.find_element_by_name("pnJ5")
                    elem.send_keys(item[0:ind])
                ind = item.find("J") + 1
                elem = driver.find_element_by_name("RibsJ5")
                if elem.text != item[ind:]:
                    elem.send_keys(item[ind:])
                elem = driver.find_element_by_id("price33")
                elem.send_keys(Keys.RETURN)
                elem = driver.find_element_by_id("J5Price")
                priceString = elem.text
                priceString = priceString.replace(",", "")
                priceString = priceString.replace("$","")
                if float(priceString) != float(price):
                    logging.info("{0},{1},{2}".format(item, priceString, price))
                elem = driver.find_element_by_name("J5reset")
                elem.send_keys(Keys.RETURN)
                partJpart = False
    print("\nFinished Processing input, please refer to ", loggingFile , " for incorrect prices")
    driver.quit()
