import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def Send_Email_XML(filepath, content):

    fromaddr = "jonathan.albalak@pandats.com"
    # to = "Niv.s@pandats.com"
    # to = "ann.poimenova@gmail.com"
    to = "jonathan.albalak@pandats.com"
    cc = "jonathan.albalak@pandats.com"
    bcc = "jonathan.albalak@pandats.com"
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

    # open the file to be sent
    filepath = filepath.replace("\\","/")
    filename = filepath
    # attachment = open("D:/automation-newforexqa/%s" % filepath, "rb")

###FOR JENKINS
    attachment = open("C:/Program Files (x86)/Jenkins/workspace/API Old Forex/%s" % filepath, "rb")

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
    s.login(fromaddr, "9U&AU=bm")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rcpt, text)

    # terminating the session
    s.quit()

def Send_Email_XLS(filepath):

    fromaddr = "jonathan.albalak@pandats.com"
    to = "Niv.s@pandats.com"
    # to = "michael.oryshchenko@pandats.com"
    # to = "ann.poimenova@gmail.com"
    cc = "yarin.b@pandats.com"
    bcc = "michael.oryshchenko@pandats.com"
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
    msg['Subject'] = "OF - All Brands - API"

    # string to store the body of the mail
    body = "OF - All Brands - API"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = filepath
    # attachment = open("D:/automation-newforexqa/%s" % filepath, "rb")

    ###FOR JENKINS
    attachment = open("C:/Program Files (x86)/Jenkins/workspace/API Old Forex/%s" % filepath, "rb")

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
    s.login(fromaddr, "9U&AU=bm")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rcpt, text)

    # terminating the session
    s.quit()

def Send_ALL_XLS(filepath):

    fromaddr = "jonathan.albalak@pandats.com"
    to = "Niv.s@pandats.com"
    # to = "michael.oryshchenko@pandats.com"
    # to = "ann.poimenova@gmail.com"
    cc = "yarin.b@pandats.com"
    bcc = "michael.oryshchenko@pandats.com"
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
    msg['Subject'] = "OF - All Brands - API"

    # string to store the body of the mail
    body = "OF - All Brands - API"

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
    s.login(fromaddr, "9U&AU=bm")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rcpt, text)

    # terminating the session
    s.quit()