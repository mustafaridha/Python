import os
import time
from datetime import date, timedelta
import smtplib
today = date.today()
yesterday = today - timedelta(days = 1)
now = time.time() - 60*60*24*2
oneDay = now
TEXT = "\n"
f2 = False
f3 = False
f5 = False
f6 = False
f7 = False
f8 = False
f9 = False
f10 = False
f11 = False
f12 = False
f13 = False
f14 = False
f15 = False
h1 = False
h2 = False
h3 = False
h4 = False
h5 = False
h6 = False
h7 = False
h8 = False
h9 = False
l1 = False
l2 = False
l3 = False
l4 = False
l5 = False
for root, dirs, files in os.walk("//bestorq-dc/Operations/Forklift Maintenance/Inspections"):
    for filename in files:
        if filename.find("Forklift") >= 0:
            if filename.find("#2") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f2 = True
            elif filename.find("#3") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f3 = True
            elif filename.find("#5") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f5 = True
            elif filename.find("#6") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f6 = True
            elif filename.find("#7") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f7 = True
            elif filename.find("#8") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f8 = True
            elif filename.find("#9") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f9 = True
            elif filename.find("#10") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f10 = True
            elif filename.find("#11") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f11 = True
            elif filename.find("#12") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f12 = True
            elif filename.find("#13") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f13 = True
            elif filename.find("#14") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f14 = True
            elif filename.find("#15") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    f15 = True
        elif filename.find("Harness") >= 0:
            if filename.find("#1") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h1 = True
            elif filename.find("#2") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h2 = True
            elif filename.find("#3") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h3 = True
            elif filename.find("#4") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h4 = True
            elif filename.find("#5") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h5 = True
            elif filename.find("#6") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h6 = True
            elif filename.find("#7") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h7 = True
            elif filename.find("#8") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h8 = True
            elif filename.find("#9") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    h9 = True
        elif filename.find("Lanyard") >= 0:
            if filename.find("#1") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    l1 = True
            elif filename.find("#2") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    l2 = True
            elif filename.find("#3") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    l3 = True
            elif filename.find("#4") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    l4 = True
            elif filename.find("#5") >= 0:
                file_path   = root + '/' + filename
                created     = os.path.getctime(file_path)
                if created >= oneDay:
                    l5 = True
TEXT = TEXT + "Forklifts : \n\n"
if f2 == False:
    TEXT = TEXT + "Forklift #2 does not have an inspection on " + str(yesterday) + "\n\n"
if f3 == False:
    TEXT = TEXT + "Forklift #3 does not have an inspection on " + str(yesterday) + "\n\n"
if f5 == False:
    TEXT = TEXT + "Forklift #5 does not have an inspection on " + str(yesterday) + "\n\n"
if f6 == False:
    TEXT = TEXT + "Forklift #6 does not have an inspection on " + str(yesterday) + "\n\n"
if f7 == False:
    TEXT = TEXT + "Forklift #7 does not have an inspection on " + str(yesterday) + "\n\n"
if f8 == False:
    TEXT = TEXT + "Forklift #8 does not have an inspection on " + str(yesterday) + "\n\n"
if f9 == False:
    TEXT = TEXT + "Forklift #9 does not have an inspection on " + str(yesterday) + "\n\n"
if f10 == False:
    TEXT = TEXT + "Forklift #10 does not have an inspection on " + str(yesterday) + "\n\n"
if f11 == False:
    TEXT = TEXT + "Forklift #11 does not have an inspection on " + str(yesterday) + "\n\n"
if f12 == False:
    TEXT = TEXT + "Forklift #12 does not have an inspection on " + str(yesterday) + "\n\n"
if f13 == False:
    TEXT = TEXT + "Forklift #13 does not have an inspection on " + str(yesterday) + "\n\n"
if f14 == False:
    TEXT = TEXT + "Forklift #14 does not have an inspection on " + str(yesterday) + "\n\n"
if f15 == False:
    TEXT = TEXT + "Forklift #15 does not have an inspection on " + str(yesterday) + "\n\n"
TEXT = TEXT + "Harnesses : \n\n"
if h1 == False:
    TEXT = TEXT + "Harness #1 does not have an inspection on " + str(yesterday) + "\n\n"
if h2 == False:
    TEXT = TEXT + "Harness #2 does not have an inspection on " + str(yesterday) + "\n\n"
if h3 == False:
    TEXT = TEXT + "Harness #3 does not have an inspection on " + str(yesterday) + "\n\n"
if h4 == False:
    TEXT = TEXT + "Harness #4 does not have an inspection on " + str(yesterday) + "\n\n"
if h5 == False:
    TEXT = TEXT + "Harness #5 does not have an inspection on " + str(yesterday) + "\n\n"
if h6 == False:
    TEXT = TEXT + "Harness #6 does not have an inspection on " + str(yesterday) + "\n\n"
if h7 == False:
    TEXT = TEXT + "Harness #7 does not have an inspection on " + str(yesterday) + "\n\n"
if h8 == False:
    TEXT = TEXT + "Harness #8 does not have an inspection on " + str(yesterday) + "\n\n"
if h9 == False:
    TEXT = TEXT + "Harness #9 does not have an inspection on " + str(yesterday) + "\n\n"
TEXT = TEXT + "Lanyards : \n\n"
if l1 == False:
    TEXT = TEXT + "Lanyard #1 does not have an inspection on " + str(yesterday) + "\n\n"
if l2 == False:
    TEXT = TEXT + "Lanyard #2 does not have an inspection on " + str(yesterday) + "\n\n"
if l3 == False:
    TEXT = TEXT + "Lanyard #3 does not have an inspection on " + str(yesterday) + "\n\n"
if l4 == False:
    TEXT = TEXT + "Lanyard #4 does not have an inspection on " + str(yesterday) + "\n\n"
if l5 == False:
    TEXT = TEXT + "Lanyard #5 does not have an inspection on " + str(yesterday) + "\n\n"


SERVER = "smtp-mail.outlook.com"
FROM = "mustafa@bestorq.com"
TO = ["mustafa@bestorq.com", "dusty@bestorq.com"] # must be a list

SUBJECT = "Missing Inspections for " + str(yesterday)

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
