import win32com.client as com
import logging
import time
import datetime
import smtplib
import schedule
now = datetime.datetime.now()
formatter = logging.Formatter('%(message)s')
def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
def TotalSize(drive):
    """ Return the TotalSize of a shared drive [GB]"""
    try:
        fso = com.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(drive)
        return drv.TotalSize/2**30
    except:
        return 0

def FreeSpace(drive):
    """ Return the FreeSpace of a shared drive [GB]"""
    try:
        fso = com.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(drive)
        return drv.FreeSpace/2**30
    except:
        return 0
workstations = ['BESTORQ22', 'BESTORQWEB', 'Bestorq-DC', 'BestSQL', 'BestPhones']
TEXT = "\n"
for compName in workstations:
    drive = '\\\\' + compName + '\\c$'
    if compName == "BESTORQ22":
        drive2 = '\\\\' + compName + '\\e$'
        drive3 = '\\\\' + compName + '\\f$'
        drive4 = '\\\\' + compName + '\\g$'
        TEXT = TEXT + compName + ": \n\n" + 'TotalSize of %s = %f GB' % (drive, TotalSize(drive)) + ', FreeSpace on %s = %f GB' % (drive, FreeSpace(drive)) + "\n\n"
        TEXT = TEXT +'TotalSize of %s = %f GB' % (drive2, TotalSize(drive2))+ ', FreeSpace on %s = %f GB' % (drive2, FreeSpace(drive2)) + "\n\n"
        TEXT = TEXT +'TotalSize of %s = %f GB' % (drive3, TotalSize(drive3)) + ', FreeSpace on %s = %f GB' % (drive3, FreeSpace(drive3)) + "\n\n"
        TEXT = TEXT +'TotalSize of %s = %f GB' % (drive4, TotalSize(drive4)) + ', FreeSpace on %s = %f GB' % (drive4, FreeSpace(drive4)) + "\n\n"
    elif compName == "BESTORQWEB":
        drive2 = '\\\\' + compName + '\\d$'
        TEXT = TEXT + compName + ": \n\n" + 'TotalSize of %s = %f GB' % (drive, TotalSize(drive)) + ', FreeSpace on %s = %f GB' % (drive, FreeSpace(drive)) + "\n\n"
        TEXT = TEXT +'TotalSize of %s = %f GB' % (drive2, TotalSize(drive2)) + ', FreeSpace on %s = %f GB' % (drive2, FreeSpace(drive2)) + "\n\n"
    elif compName == "Bestorq-DC":
        drive2 = '\\\\' + compName + '\\s$'
        TEXT = TEXT + compName + ": \n\n" + 'TotalSize of %s = %f GB' % (drive, TotalSize(drive)) + ', FreeSpace on %s = %f GB' % (drive, FreeSpace(drive)) + "\n\n"
        TEXT = TEXT +'TotalSize of %s = %f GB' % (drive2, TotalSize(drive2))+ ', FreeSpace on %s = %f GB' % (drive2, FreeSpace(drive2)) + "\n\n"
    else:
        TEXT = TEXT + compName + ": \n\n" + 'TotalSize of %s = %f GB' % (drive, TotalSize(drive)) + ', FreeSpace on %s = %f GB' % (drive, FreeSpace(drive)) + "\n\n"

SERVER = "smtp-mail.outlook.com"
FROM = "mustafa@bestorq.com"
TO = ["mustafa@bestorq.com", "phil@bestorq.com"] # must be a list

SUBJECT = "Drive Sizes"

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
logger = setup_logger('driveSizes', 'driveSizes.txt')
logger.info("{0}: {1}\n".format(str(now), TEXT))
