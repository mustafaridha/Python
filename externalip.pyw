import win32com.client as com
import logging
import time
import datetime
import smtplib
import schedule
import socket
import logging
import urllib.request
now = datetime.datetime.now()
url = "http://ip.42.pl/raw"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
my_ip = response.read().decode('utf-8')

if my_ip != "216.229.7.5":
    TEXT = "{0}: The External IP Address is not 216.229.7.5, it is {1}.".format(now, my_ip)
    SERVER = "smtp-mail.outlook.com"
    FROM = "mustafa@bestorq.com"
    TO = ["mustafa@bestorq.com", "phil.obermeyer1@gmail.com"]

    SUBJECT = "External IP Address Changed"

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
