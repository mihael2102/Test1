import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from src.test.python.ui.automation.BaseTest import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


def Send_Email_XML(filepath, content):

    fromaddr = Config.email_address
    to = Config.email_address
    cc = ""
    bcc = ""
    # instance of MIMEMultipart
    msg = MIMEMultipart('alternative')

    # storing the senders email address
    msg['From'] = fromaddr
    rcpt = cc.split(",") + bcc.split(",") + [to]
    # storing the receivers email address
    msg['To'] = to
    msg['Cc'] = cc
    msg['Bcc'] = bcc
    subject_name_test = filepath.replace('result\\TEST-', '')
    subject_name_test = subject_name_test.replace('.xml', '')
    subject_name_test = subject_name_test.replace('_', ' ')
    # storing the subject
    msg['Subject'] = "Warning:'" + subject_name_test + "' is failed"

    # string to store the body of the mail
    content_fail_err = content.decode("utf-8")
    temp = content_fail_err.find('Open first tabs page')
    index = temp
    content_fail_err = content_fail_err[index:]
    content_fail_err = content_fail_err[1:]

    content_fail_err = content_fail_err.replace(']]>	</system-err', '')
    content_fail_err = content_fail_err.replace('</testsuite>', '')
    content_fail_err = content_fail_err.replace('>', '')

    body = content_fail_err

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # attach the screenshot:
    # screenshot_path = "C:/screenshots/" + Config.test + "/" + global_var.current_brand_name + "/scr.png"
    # if os.path.exists(screenshot_path):
    #     img_data = open(screenshot_path, "rb").read()
    #     screenshot = MIMEImage(img_data, name=os.path.basename(screenshot_path))
    #     msg.attach(screenshot)

    # open the file to be sent
    filepath = filepath.replace("\\","/")
    filename = filepath
    # attachment = open("D:/automation-newforexqa/%s" % filepath, "rb")

###FOR JENKINS
    attachment = open(Config.file_path_3 % filepath, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, Config.email_password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rcpt, text)

    # terminating the session
    s.quit()

def Send_Email_XLS(filepath):

    fromaddr = Config.email_address
    to = "michael.oryshchenko@pandats.com"
    cc = ""
    bcc = ""
    # instance of MIMEMultipart
    msg = MIMEMultipart('alternative')

    # storing the senders email address
    msg['From'] = fromaddr
    rcpt = cc.split(",") + bcc.split(",") + [to]
    # storing the receivers email address
    msg['To'] = to
    msg['Cc'] = cc
    msg['Bcc'] = bcc
    # storing the subject
    msg['Subject'] = Config.mail_subject

    # string to store the body of the mail
    body = Config.mail_subject

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = filepath
    # attachment = open("D:/automation-newforexqa/%s" % filepath, "rb")

    ###FOR JENKINS
    attachment = open(Config.file_path_3 % filepath, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, Config.email_password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rcpt, text)

    # terminating the session
    s.quit()

def Send_ALL_XLS(filepath):

    fromaddr = Config.email_address
    to = "michael.oryshchenko@pandats.com"
    cc = ""
    bcc = ""
    # instance of MIMEMultipart
    msg = MIMEMultipart('alternative')

    # storing the senders email address
    msg['From'] = fromaddr
    rcpt = cc.split(",") + bcc.split(",") + [to]
    # storing the receivers email address
    msg['To'] = to
    msg['Cc'] = cc
    msg['Bcc'] = bcc
    # storing the subject
    msg['Subject'] = Config.mail_subject

    # string to store the body of the mail
    body = Config.mail_subject

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = filepath
    # attachment = open("D:/automation-newforexqa/%s" % filepath, "rb")

    ###FOR JENKINS
    attachment = open("%s" % filepath, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, Config.email_password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rcpt, text)

    # terminating the session
    s.quit()
