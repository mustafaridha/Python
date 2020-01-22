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
import datetime
while True:
    now = datetime.datetime.now()
    loggingFile = input("Please enter the output file name: ")
    formatter = logging.Formatter('%(message)s')
    destCity = input("Destination City: ")
    destST = input("Destination State (EX: NE): ")
    destZip = input("Destination ZIP: ")
    shipClass = input("Class (EX: 50,55...): ")
    pltAmount = input("Number of Pallets: ")
    weight = input("Weight (LBS): ")
    shipMonth = input("Pickup Month (EX: 01): ")
    shipDay = input("Pickup Day (EX: 01): ")
    shipYear = input("Pickup Year (EX: 2019): ")

    def setup_logger(name, log_file, level=logging.INFO):
        """Function setup as many loggers as you want"""

        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
    def rlQuote():
        print("Starting RL Quote")
        rate = 0
        transit = 0
        quote = 0
        try:
            url = "https://api.rlcarriers.com/1.0.2/RateQuoteService.asmx"
            headers = {'Content-Type': 'text/xml', 'CharSet' : 'UTF-8'}
            body = """<?xml version='1.0' encoding='UTF-8'?>
            <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:rlc='http://www.rlcarriers.com/'>
                    <soapenv:Header/>
                        <soapenv:Body>
                            <rlc:GetRateQuote>
                                <rlc:APIKey>MtZzMmEDVhZzUyMTQtNzFjMi00YzAwLWE3NWMjQ4Y4YzNDIWC</rlc:APIKey>
                                <rlc:request>
                                  <rlc:QuoteType>Domestic</rlc:QuoteType>
                         <rlc:CODAmount>0</rlc:CODAmount>
                         <rlc:Origin>
                           <rlc:City>Lincoln</rlc:City>
                           <rlc:StateOrProvince>NE</rlc:StateOrProvince>
                           <rlc:ZipOrPostalCode>68507</rlc:ZipOrPostalCode>
                           <rlc:CountryCode>USA</rlc:CountryCode>
                         </rlc:Origin>
                         <rlc:Destination>
                           <rlc:City>{0}</rlc:City>
                           <rlc:StateOrProvince>{1}</rlc:StateOrProvince>
                           <rlc:ZipOrPostalCode>{2}</rlc:ZipOrPostalCode>
                           <rlc:CountryCode>USA</rlc:CountryCode>
                         </rlc:Destination>
                               <rlc:Items>
                                <rlc:Item>
                           <rlc:Class>{3}</rlc:Class>
                           <rlc:Weight>{4}</rlc:Weight>
                         </rlc:Item>
                        </rlc:Items>
                        <rlc:DeclaredValue>1</rlc:DeclaredValue>
                        <rlc:Accessorials>
                        <rlc:Accessorial>ResidentialDelivery</rlc:Accessorial>
                        </rlc:Accessorials>
                        <rlc:OverDimensionPcs>0</rlc:OverDimensionPcs>
                        <rlc:Pallets>
                         <rlc:Pallet>
                           <rlc:Code>0001</rlc:Code>
                           <rlc:Weight>{5}</rlc:Weight>
                           <rlc:Quantity>{6}</rlc:Quantity>
                         </rlc:Pallet>
                        </rlc:Pallets>
                       </rlc:request>
                     </rlc:GetRateQuote>
                      </soapenv:Body>
                </soapenv:Envelope>
            """.format(destCity, destST, destZip, shipClass, weight, weight, pltAmount)

            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            env = ET.fromstring(resText)
            rateQuote = 0
            i = 0
            netBool = False
            stdBool = False
            for bodys in env:
                for qResponse in bodys:
                    for rateQ in qResponse:
                        for Result in rateQ:
                            for Charges in Result:
                                if Charges.tag == "{http://www.rlcarriers.com/}ServiceLevels":
                                    for service in Charges:
                                        for level in service:
                                            if level.tag == "{http://www.rlcarriers.com/}Title":
                                                if level.text == "Standard Service":
                                                    stdBool = True
                                                else:
                                                    stdBool = False
                                            if level.tag == "{http://www.rlcarriers.com/}QuoteNumber" and stdBool == True:
                                                quote = level.text
                                if Charges.tag == "{http://www.rlcarriers.com/}Charges":
                                    for charge in Charges:
                                        for items in charge:
                                            if items.tag == "{http://www.rlcarriers.com/}Title":
                                                if items.text == 'Net Charge':
                                                    netBool = True
                                            if items.tag == "{http://www.rlcarriers.com/}Amount" and netBool == True:
                                                rate = items.text
            logger = setup_logger('rlRate', 'rlRate.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished RL Quote")
            return(rate, quote)
        except:
            print("Failed RL Quote")
            return(rate, quote)
    def rlTransit():
        print("Starting RL Transit")
        rate = 0
        transit = 0
        try:
            url = "https://api.rlcarriers.com/1.0.2/TransitTimesService.asmx"
            headers = {'Content-Type': 'text/xml', 'CharSet' : 'UTF-8', 'SOAPAction' : 'http://www.rlcarriers.com/GetTransitTimes'}
            body = """<?xml version='1.0' encoding='utf-8'?>
                        <soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
                            <soap:Body>
                                <GetTransitTimes xmlns='http://www.rlcarriers.com/'>
                                <APIKey>MtZzMmEDVhZzUyMTQtNzFjMi00YzAwLWE3NWMjQ4Y4YzNDIWC</APIKey>
                                <input>
                                    <CustomerData>test</CustomerData>
                                    <DateOfPickup>{0}</DateOfPickup>
                                    <OriginPoint>
                                        <City xmlns='http://tempuri.org/'>Lincoln</City>
                                        <StateOrProvince xmlns='http://tempuri.org/'>NE</StateOrProvince>
                                        <ZipOrPostalCode xmlns='http://tempuri.org/'>68507</ZipOrPostalCode>
                                        <CountryCode xmlns='http://tempuri.org/'>USA</CountryCode>
                                    </OriginPoint>
                                    <Destinations>
                                        <DestinationPoint xmlns='http://tempuri.org/'>
                                            <ServicePoint xsi:nil='false'>
                                                <City xmlns='http://tempuri.org/'>{1}</City>
                                                <StateOrProvince xmlns='http://tempuri.org/'>{2}</StateOrProvince>
                                                <ZipOrPostalCode xmlns='http://tempuri.org/'>{3}</ZipOrPostalCode>
                                                <CountryCode xmlns='http://tempuri.org/'>USA</CountryCode>
                                            </ServicePoint>
                                        </DestinationPoint>
                                    </Destinations>
                                </input>
                                </GetTransitTimes>
                            </soap:Body>
                        </soap:Envelope>""".format("{0}/{1}/{2}".format(shipMonth,shipDay,shipYear), destCity, destST, destZip)
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                for bodys in top:
                    for resp in bodys:
                        for result in resp:
                            for timeTransit in result:
                                if timeTransit.tag == "{http://www.rlcarriers.com/}Result":
                                    for child in timeTransit:
                                        if child.tag == "{http://tempuri.org/}Destinations":
                                            for destinations in child:
                                                for destination in destinations:
                                                    if destination.tag == "{http://tempuri.org/}ServiceDays":
                                                        transit = destination.text
            logger = setup_logger('rlTransit', 'rlTransit.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished RL Transit")
            return(transit)
        except:
            print("Failed RL Transit")
            return(transit)

    def usfAPI():
        print("Starting USF API")
        rate = 0
        transit = 0
        try:
            url = "https://api.hollandregional.com/api/RateQuote/doRateQuote?accessKey=3Dln8P4frdDQ56WzaWixUw==&accountId=421188&originZipCode=68507&destZipCode={0}&direction=Shipper&chargeType=Prepaid&numberofPallets={1}&shipmentClass1={2}&shipmentWeight1={3}".format(destZip, pltAmount, shipClass, weight)
            headers = {'Content-Type': 'application/json'}
            body = ""
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                if env.tag == "RateQuote":
                    for RateQ in env:
                        if RateQ.tag == "TOTAL_COST":
                            rate = RateQ.text
                        if RateQ.tag == "SERVICEDAYS":
                            transit = RateQ.text
            logger = setup_logger('usf', 'usf.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished USF API")
            return(rate, transit)
        except:
            print("Failed USF API")
            return(rate, transit)
    def abfAPI():
        print("Starting ABF API")
        rate = 0
        transit = 0
        quote = 0
        try:
            url = "https://www.abfs.com/xml/aquotexml.asp?DL=2&ID=X4YNRT71&ShipCity=Lincoln&ShipState=NE&ShipZip=68507&ShipCountry=US&ConsCity={0}&ConsState={1}&ConsZip={2}&ConsCountry=US&Wgt1={3}&Class1={4}&UnitNo1={5}&UnitType1=PLT&ShipAff=Y&ShipMonth={6}&ShipDay={7}&ShipYear={8}".format(destCity, destST, destZip, weight, shipClass, pltAmount, shipMonth, shipDay, shipYear)
            headers = {'Content-Type': 'application/json'}
            body = ""
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                if env.tag == "QUOTEID":
                    quote = env.text
                if env.tag == "CHARGE":
                    rate = env.text
                if env.tag == "ADVERTISEDTRANSIT":
                    transit = env.text
            logger = setup_logger('abf', 'abf.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished ABF API")
            return(rate, transit, quote)
        except:
            print("Failed ABF API")
            return(rate, transit, quote)
    def upsAPI():
        print("Starting UPS API")
        rate = 0
        transit = 0
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe", chrome_options=chrome_options)
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
            elem.send_keys(destZip)
            elem = driver.find_element_by_id("cContent_Right_shipDate")
            elem.clear()
            elem.send_keys("{0}/{1}/{2}".format(shipMonth, shipDay, shipYear))
            driver.find_element_by_id("cContent_Right_requestQuoteNumber").click()
            elem = driver.find_element_by_id("cContent_Right_cmdNmfc1_ddClassNum")
            elem.send_keys(shipClass)
            elem = driver.find_element_by_id("cContent_Right_cmdNmfc1_txtcommodityWeight")
            elem.send_keys(weight)
            elem = driver.find_element_by_id("cContent_Right_btnSubmit")
            elem.send_keys(Keys.RETURN)
            elem = driver.find_element_by_xpath("//*[@id='cContent_Right_lblServiceDays']")
            transit = elem.text
            elem = driver.find_element_by_xpath("//*[@id='cContent_Right_lblltltotalAmount']")
            rate = elem.text
            elem = driver.find_element_by_xpath("//*[@id='cContent_Right_lblQuoteNbr']")
            quote = elem.text
            driver.quit()
            logger = setup_logger('ups', 'ups.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("Response:\n")
            logger.info("rate: {0}, Quote Number: {1}, Transit: {2} \n".format(rate, quote, transit))
            logger.info("End\n")
            print("Finished UPS API")
            return(rate,transit, quote)
        except:
            driver.close()
            print("Failed UPS API")
            return(rate,transit, "error")
    def yrcAPI():
        print("Starting YRC API")
        rate = 0
        transit = 0
        quoteNum = 0
        try:
            url = "https://api.yrc.com/node/api/ratequote"
            headers = {'Content-Type': 'application/json'}
            body = """{{"login" : {{ "username":"del1604", "password":"rexxon1000", "busId":"69009593429", "busRole":"Shipper", "paymentTerms":"Prepaid"}},
             "details" : {{ "serviceClass":"ALL", "typeQuery":"MATRX", "pickupDate":"{0}{1}{2}"}} ,
             "originLocation": {{ "city":"Lincoln", "state": "NE", "postalCode": "68507", "country": "USA"}},
             "destinationLocation": {{ "city":"{3}", "state": "{4}", "postalCode": "{5}", "country":"USA"}},
             "listOfCommodities": {{ "commodity" :[{{ "nmfcClass" : {6}, "handlingUnits" : {7}, "packageCode": "PLT", "weight": {8}}}]}},
             "serviceOpts": {{ }}}}""".format(shipYear, shipMonth, shipDay, destCity, destST, destZip, shipClass, pltAmount, weight)
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = json.loads(resText)
            if 'pageRoot' in top:
                root = top['pageRoot']
                bodys = root['bodyMain']
                quote = bodys['rateQuote']
                quoteNum = quote['referenceId']
                matrix = quote['quoteMatrix']
                table = matrix['table']
                for child in table:
                    transit = child['transitOptions']
                    for date in transit:
                        transit = date['transitDays']
                        rate = date['totalCharges']
                        break
                    break
            logger = setup_logger('yrc', 'yrc.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished YRC API")
            return(rate, transit, quoteNum)
        except:
            print("Failed YRC API")
            return(rate, transit, quoteNum)
    def estesRateAPI():
        print("Starting ESTES Rate API")
        rate = 0
        transit = 0
        quoteNum = 0
        try:
            url = "https://www.estes-express.com/tools/rating/ratequote/v3.0/services/RateQuoteService?wsdl"
            headers = {'Content-Type': 'text/xml', 'CharSet' : 'UTF-8', 'SOAPAction' : 'http://ws.estesexpress.com/ratequote/getQuote'}
            body = """<?xml version='1.0' encoding='UTF-8'?>
                <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:rat='http://ws.estesexpress.com/ratequote' xmlns:rat1='http://ws.estesexpress.com/schema/2017/07/ratequote'>
                        <soapenv:Header>
                     <rat:auth>
                                <rat:user>rexxon</rat:user>
                       <rat:password>rexxon1000</rat:password>
                     </rat:auth>
                        </soapenv:Header>
                        <soapenv:Body>
                     <rat1:rateRequest>
                       <rat1:requestID>test</rat1:requestID>
                       <rat1:account>3604412</rat1:account>
                       <rat1:originPoint>
                         <rat1:countryCode>US</rat1:countryCode>
                         <rat1:postalCode>68507</rat1:postalCode>
                         <rat1:city>Lincoln</rat1:city>
                         <rat1:stateProvince>NE</rat1:stateProvince>
                       </rat1:originPoint>
                       <rat1:destinationPoint>
                         <rat1:countryCode>US</rat1:countryCode>
                         <rat1:postalCode>{0}</rat1:postalCode>
                         <rat1:city>{1}</rat1:city>
                         <rat1:stateProvince>{2}</rat1:stateProvince>
                       </rat1:destinationPoint>
                       <rat1:payor>S</rat1:payor>
                       <rat1:terms>PPD</rat1:terms>
                       <rat1:equipmentType>Trailer</rat1:equipmentType>
                       <rat1:baseCommodities>
                         <rat1:commodity>
                           <rat1:class>{3}</rat1:class>
                           <rat1:weight>{4}</rat1:weight>
                         </rat1:commodity>
                       </rat1:baseCommodities>
                     </rat1:rateRequest>
                        </soapenv:Body>
                </soapenv:Envelope>""".format(destZip, destCity, destST, shipClass, weight)
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                if env.tag == "{http://schemas.xmlsoap.org/soap/envelope/}Body":
                    for bodys in env:
                        for rateQuote in bodys:
                            if rateQuote.tag == "{http://ws.estesexpress.com/schema/2017/07/ratequote}quote":
                                for quote in rateQuote:
                                    if quote.tag == "{http://ws.estesexpress.com/schema/2017/07/ratequote}quoteNumber":
                                        quoteNum = quote.text
                                    if quote.tag == "{http://ws.estesexpress.com/schema/2017/07/ratequote}pricing":
                                        for pricing in quote:
                                            for price in pricing:
                                                if price.tag == "{http://ws.estesexpress.com/schema/2017/07/ratequote}standardPrice":
                                                    rate = price.text
            logger = setup_logger('estesRate', 'estesRate.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("End\n")
            print("Finished ESTES Rate API")
            return(rate, quoteNum)
        except:
            print("Failed ESTES Rate API")
            return(rate, quoteNum)
    def estesTransitAPI():
        print("Starting ESTES Transit API")
        rate = 0
        transit = 0
        try:
            url = "http://www.estes-express.com/transittime/services/TransitTimeService?wsdl"
            headers = {'Content-Type': 'text/xml', 'CharSet' : 'UTF-8', 'SOAPAction' : 'http://ws.estesexpress.com/transittime/calc'}
            body = """<?xml version='1.0' encoding='UTF-8'?>
             	<soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:tran='http://ws.estesexpress.com/transittime' xmlns:tran1='http://ws.estesexpress.com/schema/transittime'>
             			<soapenv:Header>
                     <tran:auth>
             					<tran:user>rexxon</tran:user>
                       <tran:password>rexxon1000</tran:password>
                     </tran:auth>
             			</soapenv:Header>
             			<soapenv:Body>
                     <tran1:serviceRequest>
                       <tran1:requestID>test</tran1:requestID>
                       <tran1:version>
                         <tran1:versionNumber>1.1</tran1:versionNumber>
                       </tran1:version>
                       <tran1:originPoint>
                         <tran1:postalCode>68507</tran1:postalCode>
                         <tran1:city>Lincoln</tran1:city>
                         <tran1:stateProvince>NE</tran1:stateProvince>
                         <tran1:countryCode>US</tran1:countryCode>
                       </tran1:originPoint>
                       <tran1:destinationPoint>
                         <tran1:postalCode>{0}</tran1:postalCode>
                         <tran1:city>{1}</tran1:city>
                         <tran1:stateProvince>{2}</tran1:stateProvince>
                         <tran1:countryCode>US</tran1:countryCode>
                       </tran1:destinationPoint>
                       <tran1:shipDate>{3}</tran1:shipDate>
                       </tran1:serviceRequest>
             			</soapenv:Body>
             	</soapenv:Envelope>""".format(destZip, destCity, destST, "{0}-{1}-{2}".format(shipYear, shipMonth, shipDay))
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                if env.tag == "{http://schemas.xmlsoap.org/soap/envelope/}Body":
                    for bodys in env:
                        for serviceResult in bodys:
                            if serviceResult.tag == "{http://ws.estesexpress.com/schema/transittime}transitTimes":
                                for transitTimes in serviceResult:
                                    if transitTimes.tag == "{http://ws.estesexpress.com/schema/transittime}transitTimeList":
                                        for list in transitTimes:
                                            for transitTime in list:
                                                if transitTime.tag == "{http://ws.estesexpress.com/schema/transittime}serviceDays":
                                                    transit = transitTime.text
            logger = setup_logger('estesTransit', 'estesTransit.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished ESTES Transit API")
            return(transit)
        except:
            print("Failed ESTES Transit API")
            return(transit)
    def xpoToken():
        print("Starting XPO Token")
        try:
            url = "https://api.ltl.xpo.com/token?grant_type=password&username=rexxon2&password=rexxon1000"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic MkhxNUd1ZERGMVhlOXgyd3Z0ME1MY3hCRzE4YTozX3FLYU1XcER3Q1hYZ2RhMWdlV1p0Tm1YNVVh'}
            body = ""
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = json.loads(resText)
            root = top['access_token']
            logger = setup_logger('xpoToken', 'xpoToken.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished XPO Token")
            return(root)
        except:
            print("Failed XPO Token")
            return(root)

    def xpoAPI():
        print("Starting XPO API")
        rate = 0
        transit = 0
        quote = 0
        try:
            token = xpoToken()
            url = "https://api.ltl.xpo.com/rating/1.0/ratequotes/"
            headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
            body = """{{"shipmentInfo":{{
                                    "paymentTermCd":"P",
                                    "accessorials":[],
                                    "commodity":[{{
                                              "grossWeight":{{
                                                    "weight":{0},
                                                    "weightUom":"LBS"
                                              }},
                                              "nmfcClass":{1},
                                              "hazmatInd":false,
                                              "pieceCnt":{2}
                            }}],
                            "consignee":{{
                                        "address":{{
                                                    "postalCd":"{3}"
                                        }}
                            }},
                            "shipper":{{
                                          "acctInstId":"239216608"
                            }},
                            "shipmentDate":"{4}",
                            "palletCnt":{5}
                      }}
                      }}""".format(weight, shipClass, pltAmount, destZip, "{0}-{1}-{2}".format(shipYear, shipMonth, shipDay), pltAmount)
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = json.loads(resText)
            if 'data' in top:
                root = top['data']
                rateQuote = root['rateQuote']
                quote = rateQuote['confirmationNbr']
                totCharge = rateQuote['totCharge']
                rate = totCharge[0]
                rate = rate['amt']
                transitTime = root['transitTime']
                transit = transitTime['transitDays']
            logger = setup_logger('xpo', 'xpo.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished XPO API")
            return(rate, transit, quote)
        except:
            print("Failed XPO API")
            return(rate, transit, quote)
    def daytonAPI():
        print("Starting Dayton API")
        rate = 0
        transit = 0
        quote = 0
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe", chrome_options=chrome_options)
            driver.get("https://www.daytonfreight.com/")
            driver.maximize_window()
            driver.find_element_by_link_text("Rate Estimate").click()
            elem = driver.find_element_by_id("username")
            elem.send_keys("rexxon1000")
            elem = driver.find_element_by_id("password")
            elem.send_keys("del1604")
            elem = driver.find_element_by_xpath("//*[@id='page-content']/form/div/div/div/div[6]/div/input[2]")
            elem.send_keys(Keys.RETURN)
            time.sleep(2)
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-entry/ng-form/div[1]/div[1]/date-picker/div/div/input")
            elem.click()
            elem.clear()
            elem.send_keys("{0}/{1}/{2}".format(shipMonth, shipDay, shipYear))
            driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-entry/ng-form/div[2]/div[1]/terms-selector/div[2]/select/option[2]").click()
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-entry/ng-form/div[2]/div[2]/div/rate-addresses/div/div[2]/div/input")
            elem.send_keys(destZip)
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-entry/ng-form/div[3]/shipment-items/div[4]/div[1]/div[1]/select")
            elem.send_keys(shipClass)
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-entry/ng-form/div[3]/shipment-items/div[4]/div[1]/div[2]/input")
            elem.send_keys(weight)
            elem = driver.find_element_by_id("submit")
            elem.send_keys(Keys.RETURN)
            time.sleep(3)
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-results/div[1]/div[1]/div/h3")
            quote = elem.text
            time.sleep(1)
            count = len(driver.find_elements_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-results/div[1]/div[4]/div[2]/table/tbody/tr"))
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-results/div[1]/div[4]/div[2]/table/tbody/tr[{0}]/td[2]/b".format(count))
            rate = elem.text
            time.sleep(1)
            elem = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/rate-wrapper/rate-results/div[1]/div[7]/div/transit-times-results/div/div[1]/div[1]/div[3]/div[1]/div/p[1]")
            transit = elem.text
            logger = setup_logger('dayton', 'dayton.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("Response:\n")
            logger.info("rate: {0}, Quote Number: {1}, Transit: {2} \n".format(rate, quote, transit))
            logger.info("End\n")
            driver.quit()
            print("Finished Dayton API")
            return(rate, transit, quote)
        except:
            driver.close()
            print("Failed Dayton API")
            return(rate, transit, quote)
    def mmeAPI():
        print("Starting MME API")
        rate = 0
        transit = 0
        quote = 0
        pickupDate = 0
        eDeliveryDate = 0
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe", chrome_options=chrome_options)
            driver.get("https://www.mmeinc.com/index.php")
            driver.maximize_window()
            driver.find_element_by_link_text("ExpressTRAX Login").click()
            elem = driver.find_element_by_name("user")
            elem.click()
            elem.send_keys("242309")
            elem = driver.find_element_by_name("pass")
            elem.clear()
            elem.send_keys("bestorq1")
            elem = driver.find_element_by_name("sublogin")
            elem.send_keys(Keys.RETURN)
            driver.get("https://www.mmeinc.com/transittime.php")
            elem = driver.find_element_by_id("OriZip")
            elem.click()
            elem.send_keys("68507")
            time.sleep(2)
            elem = driver.find_element_by_id("DesZip")
            elem.click()
            elem.send_keys(destZip)
            time.sleep(2)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_element_by_id("PUDate")
            elem.click()
            elem.clear()
            elem.send_keys("{0}/{1}/{2}".format(shipMonth,shipDay,shipYear))
            elem = driver.find_element_by_name("Submit")
            time.sleep(1)
            elem.click()
            pickupDate = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[5]/div/table[2]/tbody/tr[3]/td[1]").text
            eDeliveryDate = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[5]/div/table[2]/tbody/tr[3]/td[2]").text
            transit = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[5]/div/table[2]/tbody/tr[3]/td[3]").text
            driver.get("https://www.mmeinc.com/etrate.php")
            elem = driver.find_element_by_id("PUDate")
            elem.click()
            elem.clear()
            elem.send_keys("{0}/{1}/{2}".format(shipMonth,shipDay,shipYear))
            elem = driver.find_element_by_id("OriZip")
            elem.click()
            elem.send_keys("68507")
            time.sleep(2)
            elem = driver.find_element_by_id("DesZip")
            elem.click()
            elem.send_keys(destZip)
            time.sleep(2)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_element_by_id("W00")
            elem.click()
            elem.send_keys(weight)
            time.sleep(2)
            if shipClass == "50":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[1]").click()
            elif shipClass == "55":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[2]").click()
            elif shipClass == "60":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[3]").click()
            elif shipClass == "65":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[4]").click()
            elif shipClass == "70":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[5]").click()
            elif shipClass == "77.5":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[6]").click()
            elif shipClass == "85":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[7]").click()
            elif shipClass == "92.5":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[8]").click()
            elif shipClass == "100":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[9]").click()
            elif shipClass == "110":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[10]").click()
            elif shipClass == "125":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[11]").click()
            elif shipClass == "150":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[12]").click()
            elif shipClass == "175":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[13]").click()
            elif shipClass == "200":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[14]").click()
            elif shipClass == "250":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[15]").click()
            elif shipClass == "300":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[16]").click()
            elif shipClass == "400":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[17]").click()
            elif shipClass == "500":
                driver.find_element_by_xpath("//*[@id='ClArr[0]']/option[18]").click()
            else:
                print("Invalid Ship Class Please Try Again")
                driver.close()
                return
            time.sleep(2)
            driver.find_element_by_id("AcceptTerms").click()
            time.sleep(2)
            elem = driver.find_element_by_xpath("//*[@id='customer']/div[5]/div[2]/div[2]/div[1]/input[6]")
            elem.click()
            quote = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[5]/div/div[1]/div[1]").text
            count = len(driver.find_elements_by_xpath("//*[@id='RateTable']/tbody/tr"))
            rate = driver.find_element_by_xpath("//*[@id='RateTable']/tbody/tr[{0}]/td[3]".format(count)).text
            logger = setup_logger('mme', 'mme.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("Response:\n")
            logger.info("Transit = Pickup Date: {0}, Estimated Delivery Date: {1}, Days: {2} \n".format(pickupDate, eDeliveryDate, transit))
            logger.info("Rate = {0}\n".format(rate))
            logger.info("End\n")
            driver.quit()
            print("Finished MME API")
            return(rate,transit,quote,pickupDate,eDeliveryDate)
        except:
            driver.close()
            print("Failed MME API")
            return(rate,transit,quote,pickupDate,eDeliveryDate)
    def cccAPI():
        print("Starting CCC API")
        rate = 0
        transit = 0
        quote = 0
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe", chrome_options=chrome_options)
            driver.get("http://crosscountrycourier.com/")
            driver.maximize_window()
            elem = driver.find_element_by_id("ctl00_TxtLogin")
            elem.click()
            elem.send_keys("rexxon")
            elem = driver.find_element_by_id("ctl00_password")
            elem.click()
            elem.send_keys("rexxon1000")
            elem = driver.find_element_by_id("ctl00_submitSignIn")
            elem.send_keys(Keys.RETURN)
            driver.find_element_by_link_text("Quick Quote").click()
            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_DestZipcode")
            elem.send_keys(destZip)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_txtWeight")
            elem.send_keys(weight)
            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_txtPackageCnt")
            elem.send_keys(pltAmount)
            driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_cMiddle_QuickList1_DDPackageType']/option[10]").click()
            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_FRTclass")
            elem.send_keys(shipClass)
            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_ButAddItem")
            elem.send_keys(Keys.RETURN)
            try:
                elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_ButQuoteThis")
                elem.send_keys(Keys.RETURN)
                rate = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_LabelCost").text
                quote = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_QuoteNum").text
                eDeliveryDate = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_LabelDeliveryDate").text
                pickupDate = "{0}/{1}/{2}".format(shipMonth,shipDay,shipYear)
                d1 = datetime.datetime.strptime(eDeliveryDate, "%m/%d/%Y")
                d2 = datetime.datetime.strptime(pickupDate, "%m/%d/%Y")
                transit = abs((d1-d2).days)
                logger = setup_logger('ccc', 'ccc.txt')
                logger.info("Start: {0}\n".format(str(now)))
                logger.info("Response:\n")
                logger.info("rate: {0}, Quote Number: {1}, Transit: {2} \n".format(rate, quote, transit))
                logger.info("End\n")
                driver.quit()
                print("Finished CCC API")
                return(rate,transit,quote)
            except NoSuchElementException:
                elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_cMiddle_QuickList1_WarningMessage").text
                elem = elem.replace(",", "")
                print("There was an error with the input, couldn't get rate please visit crosscountrycourier.com to get your rate")
                logger = setup_logger('cccErr', 'cccErr.txt')
                logger.info("Start: {0}\n".format(str(now)))
                logger.info("Response:\n")
                logger.info("Error: {0} \n".format(elem))
                logger.info("End\n")
                driver.quit()
                print("Finished CCC API")
                return(rate,transit,quote)
        except:
            driver.close()
            print("Failed CCC API")
            return(rate,transit,quote)
    def usroadAPI():
        print("Starting US Road API")
        rate = 0
        transit = 0
        quote = 0
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe", chrome_options=chrome_options)
            driver.get("http://usroad.com/")
            driver.maximize_window()
            driver.find_element_by_link_text("Sign In").click()
            time.sleep(4)
            elem = driver.find_element_by_id("userName")
            elem.send_keys("BES695")
            elem = driver.find_element_by_id("password")
            elem.send_keys("L6152")
            elem = driver.find_element_by_name("action")
            elem.send_keys(Keys.RETURN)
            time.sleep(4)
            elem = driver.find_element_by_id("txtOrigin")
            elem.send_keys("68507")
            elem = driver.find_element_by_id("txtDestination")
            elem.send_keys(destZip)
            elem = driver.find_element_by_id("transitSearchButton")
            elem.send_keys(Keys.RETURN)
            time.sleep(4)
            firstText = driver.find_element_by_id("shipmentTransitSection").text
            secondText = firstText.split(".")
            transit = secondText[0]
            elem = driver.find_element_by_id("txtOrigin2")
            elem.clear()
            elem.send_keys("68507")
            elem = driver.find_element_by_id("txtDestination2")
            elem.clear()
            elem.send_keys(destZip)
            elem = driver.find_element_by_id("handUnits1")
            elem.send_keys(pltAmount)
            elem = driver.find_element_by_id("weight1")
            elem.send_keys(weight)
            elem = driver.find_element_by_id("class1")
            elem.send_keys(shipClass)
            elem = driver.find_element_by_id("rateButton")
            elem.send_keys(Keys.RETURN)
            time.sleep(4)
            try:
                count = len(driver.find_elements_by_xpath("//*[@id='shipmentCostSectionResults']/table/tbody/tr"))
                rateVar = driver.find_elements_by_xpath("//*[@id='shipmentCostSectionResults']/table/tbody/tr[{0}]/td[2]".format(count))
                quoteList = driver.find_elements_by_xpath("//*[@id='shipmentCostSectionResults']/table/tbody/tr[{0}]/td[1]".format(count))
                rate = rateVar[0].text
                first = quoteList[0].text
                second = first.split("#")
                third = second[1].split(":")
                quote = third[0]
                logger = setup_logger('usRoad', 'usRoad.txt')
                logger.info("Start: {0}\n".format(str(now)))
                logger.info("Response:\n")
                logger.info("rate: {0}, Quote Number: {1}, Transit: {2} \n".format(rate, quote, transit))
                logger.info("End\n")
                driver.quit()
                print("Finished US Road API")
                return(rate,transit,quote)
            except NoSuchElementException:
                print("There was an error with the input, couldn't get rate please try again")
                driver.quit()
                print("Finished US Road API")
                return(rate,transit,quote)
        except:
            driver.close()
            print("Failed US Road API")
            return(rate,transit,quote)
    def ODRateAPI():
        print("Starting Old Dominion Rate API")
        rate = 0
        transit = 0
        quoteNum = 0
        try:
            url = "https://www.odfl.com/wsRate_v6/RateService?wsdl"
            headers = {'Content-Type': 'text/xml'}
            body = """<?xml version='1.0'?>
                <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:myr='http://myRate.ws.odfl.com/'>
                   <soapenv:Header/>
                   <soapenv:Body>
                      <myr:getLTLRateEstimate>
                         <arg0>
                  		  <destinationCountry>USA</destinationCountry>
                  		  <destinationPostalCode>{0}</destinationPostalCode>
                  		  <destinationCity>{1}</destinationCity>
                            <destinationState>{2}</destinationState>
                		  <freightItems>
                  			<ratedClass>{3}</ratedClass>
                  			<weight>{4}</weight>
                  		  </freightItems>
                  		  <odfl4MePassword>Bestorq1</odfl4MePassword>
                            <odfl4MeUser>rexxon1000</odfl4MeUser>
                            <odflCustomerAccount>13287033</odflCustomerAccount>
                  		  <originCountry>USA</originCountry>
                  	       <originPostalCode>68507</originPostalCode>
                  	       <originCity>Lincoln</originCity>
                            <originState>NE</originState>
                  		  <requestReferenceNumber>true</requestReferenceNumber>
                         </arg0>
                      </myr:getLTLRateEstimate>
                   </soapenv:Body>
                </soapenv:Envelope>""".format(destZip, destCity, destST, shipClass, weight)
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                if env.tag == "{http://schemas.xmlsoap.org/soap/envelope/}Body":
                    for body in env:
                        for estimate in body:
                            for ret in estimate:
                                if ret.tag == "destinationCities":
                                    for service in ret:
                                        if service.tag == "serviceDays":
                                            transit = service.text
                                if ret.tag == "referenceNumber":
                                    quoteNum = ret.text
                                if ret.tag == "rateEstimate":
                                    for rateEstimate in ret:
                                        if rateEstimate.tag == "netFreightCharge":
                                            rate = rateEstimate.text
            logger = setup_logger('oldDominion', 'oldDominion.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished Old Dominion Rate API")
            return(rate, transit, quoteNum)
        except:
            print("Failed Old Dominion Rate API")
            return(rate, transit, quoteNum)
    def SAIARateAPI():
        print("Starting SAIA Rate API")
        rate = 0
        transit = 0
        quoteNum = 0
        try:
            url = "http://www.saiasecure.com/webservice/ratequote/soap.asmx"
            headers = {'Content-Type': 'text/xml', 'CharSet' : 'UTF-8', 'SOAPAction' : 'http://www.saiasecure.com/WebService/ratequote/Create'}
            body = """<?xml version='1.0' encoding='utf-8'?>
                    <soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
                        <soap:Body>
                            <Create xmlns='http://www.saiasecure.com/WebService/ratequote/'>
                                <request>
                                    <Details>
                                        <DetailItem>
                                            <Weight>{0}</Weight>
                                            <Class>{1}</Class>
                                        </DetailItem>
                                    </Details>
                                <Accessorials>
                                    <AccessorialItem>
                                        <Code>SingleShipment</Code>
                                    </AccessorialItem>
                                </Accessorials>
                                <UserID>rexxon</UserID>
                                <Password>rexxon1000</Password>
                                <TestMode>N</TestMode>
                                <BillingTerms>Prepaid</BillingTerms>
                                <AccountNumber>0779439</AccountNumber>
                                <Application>Outbound</Application>
                                <OriginCity>Lincoln</OriginCity>
                                <OriginState>NE</OriginState>
                                <OriginZipcode>68507</OriginZipcode>
                                <DestinationCity>{2}</DestinationCity>
                                <DestinationState>{3}</DestinationState>
                                <DestinationZipcode>{4}</DestinationZipcode>
                                <WeightUnits>LBS</WeightUnits>
                            </request>
                        </Create>
                    </soap:Body>
                    </soap:Envelope>""".format(weight,shipClass, destCity, destST, destZip)
            response = requests.post(url,data=body,headers=headers)
            resText = response.text
            top = ET.fromstring(resText)
            for env in top:
                for bodys in env:
                    for create in bodys:
                        for createResults in create:
                            if createResults.tag == "{http://www.saiasecure.com/WebService/ratequote/}QuoteNumber":
                                quoteNum = createResults.text
                            if createResults.tag == "{http://www.saiasecure.com/WebService/ratequote/}TotalInvoice":
                                rate = createResults.text
                            if createResults.tag == "{http://www.saiasecure.com/WebService/ratequote/}StandardServiceDays":
                                transit = createResults.text
            logger = setup_logger('SAIA', 'SAIA.txt')
            logger.info("Start: {0}\n".format(str(now)))
            logger.info("URL = {0}\n".format(url))
            logger.info("Request: \n")
            logger.info("{0}\n".format(body))
            logger.info("Response:\n")
            logger.info("{0}\n".format(resText))
            logger.info("End\n")
            print("Finished SAIA Rate API")
            return(rate, transit, quoteNum)
        except:
            print("Failed SAIA Rate API")
            return(rate, transit, quoteNum)
    usRoad = usroadAPI()
    ccc = cccAPI()
    mme = mmeAPI()
    rlRate = rlQuote()
    rlT = rlTransit()
    usf = usfAPI()
    abf = abfAPI()
    ups = upsAPI()
    yrc = yrcAPI()
    estesR = estesRateAPI()
    estesT = estesTransitAPI()
    xpo = xpoAPI()
    dayton = daytonAPI()
    od = ODRateAPI()
    saia = SAIARateAPI()
    print("\nRL Rate = ", rlRate[0], ", RL Transit Time: ", rlT, "Day(s)")
    print("USF Rate = $", usf[0], ", USF Transit = ", usf[1], "Day(s)")
    print("ABF Rate = $", abf[0], ", ABF Transit = ", abf[1])
    print("UPS Rate = $", ups[0], ", UPS Transit = ", ups[1], "Days")
    print("YRC Rate = $", float(yrc[0])/100, ", YRC Transit = ", yrc[1], "Day(s)")
    print("ESTES Rate = $", estesR[0], ", ESTES Transit = ", estesT, "Day(s)")
    print("Old Dominion Rate = $", od[0], ", Old Dominion Transit = ", od[1], "Day(s)")
    print("XPO Rate = $", xpo[0], ", XPO Transit = ", xpo[1], "Day(s)")
    print("Dayton Rate = $", dayton[0], ", Dayton Transit = ", dayton[1], "Day(s)")
    print("MME Rate = ", mme[0], ", MME Transit = ", mme[1], "Day(s)")
    print("CCC Rate = ", ccc[0], ", CCC Transit = ", ccc[1], "")
    print("US Road Rate = $", usRoad[0], ", US Road Transit = ", usRoad[1])
    print("SAIA Rate = $", saia[0], ", US Road Transit = ", saia[1], "Day(s)", "\n")
    logger = setup_logger('tracking', loggingFile+".csv")
    logger.info("Quote Number,Company,Quote Rate,Transit Time,Destination City,Destination State,Destination ZIP,Ship Class,Number of Pallets,Weight,Ship Date")
    for retry in range(5):
        choice = input("Company Choice (RL, USF, ABF, UPS, YRC, ESTES, XPO, DAYTON, MME, CCC, US, OD, SAIA or ALL)?: ")
        if choice == "RL" or choice == "rl":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(rlRate[1],"RL", rlRate[0], "{0} Day(s)".format(rlT), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "USF" or choice == "usf":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format("","USF", "${0}".format(usf[0]), "{0} Day(s)".format(usf[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "ABF" or choice == "abf":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(abf[2],"ABF", "${0}".format(abf[0]), abf[1], destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "UPS" or choice == "ups":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(ups[2],"UPS", "${0}".format(ups[0]), "{0} Day(s)".format(ups[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "YRC" or choice == "yrc":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(yrc[2],"YRC", "${0}".format(float(yrc[0])/100), "{0} Day(s)".format(yrc[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "ESTES" or choice == "estes":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(estesR[1],"ESTES", "${0}".format(estesR[0]), "{0} Day(s)".format(estesT), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "XPO" or choice == "xpo":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(xpo[2],"XPO", "${0}".format(xpo[0]), "{0} Day(s)".format(xpo[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "DAYTON" or choice == "dayton":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(dayton[2],"DAYTON", "${0}".format(dayton[0]), "{0} Day(s)".format(dayton[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "MME" or choice == "mme":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(mme[2],"MME", "{0}".format(mme[0]), "{0} Day(s)".format(mme[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "CCC" or choice == "ccc":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(ccc[2],"CCC", "{0}".format(ccc[0]), "{0} Day(s)".format(ccc[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "US" or choice == "us":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(usRoad[2],"US ROAD", "${0}".format(usRoad[0]), "{0} Day(s)".format(usRoad[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "OD" or choice == "od":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(od[2],"Old Dominion", "${0}".format(od[0]), "{0} Day(s)".format(od[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "SAIA" or choice == "saia":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(saia[2],"SAIA", "${0}".format(saia[0]), "{0} Day(s)".format(saia[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        elif choice == "ALL" or choice == "all":
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(rlRate[1],"RL", rlRate[0], "{0} Day(s)".format(rlT), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format("","USF", "${0}".format(usf[0]), "{0} Day(s)".format(usf[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(abf[2],"ABF", "${0}".format(abf[0]), abf[1], destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(ups[2],"UPS", "${0}".format(ups[0]), "{0} Day(s)".format(ups[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(yrc[2],"YRC", "${0}".format(float(yrc[0])/100), "{0} Day(s)".format(yrc[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(estesR[1],"ESTES", "${0}".format(estesR[0]), "{0} Day(s)".format(estesT), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(xpo[2],"XPO", "${0}".format(xpo[0]), "{0} Day(s)".format(xpo[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(dayton[2],"DAYTON", "${0}".format(dayton[0]), "{0} Day(s)".format(dayton[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(mme[2],"MME", "{0}".format(mme[0]), "{0} Day(s)".format(mme[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(ccc[2],"CCC", "{0}".format(ccc[0]), "{0} Day(s)".format(ccc[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(usRoad[2],"US ROAD", "${0}".format(usRoad[0]), "{0} Day(s)".format(usRoad[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(od[2],"Old Dominion", "${0}".format(od[0]), "{0} Day(s)".format(od[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            logger.info("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}/{11}/{12}".format(saia[2],"SAIA", "${0}".format(saia[0]), "{0} Day(s)".format(saia[1]), destCity, destST, destZip, shipClass, pltAmount, weight, shipMonth, shipDay, shipYear))
            break
        else:
            print("Invalid input, Please try again.")
    else:
        print("Too many tries. Restarting...")
