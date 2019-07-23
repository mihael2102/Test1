from requests import get

test = "NF Special CA"
file_path_1 = "C:/Program Files (x86)/Jenkins/workspace/" + test + "/result/final_file.xlsx"
file_path_2 = 'C:/Program Files (x86)/Jenkins/workspace/' + test + '/result/*.xlsx'
file_path_3 = "C:/Program Files (x86)/Jenkins/workspace/" + test + "/%s"
short_excel_path = "C:/Program Files (x86)/Jenkins/workspace/" + test + "/result/short_final_file.xlsx"
mail_subject = test
timeout = 4
data = None
url_client_area = ""
url_ca = ""
url_crm = ""
url_gmail = "https://mail.google.com"
window_after = None
window_before = None
counter = 1
logger = None
handler = None


chrome_driver = "C:/Users/Panda102/automation-newforexqa/src/main/python/resources/grid/drivers/chromedriver.exe"
# chrome_driver = "C:/Users/Panda102/Desktop/drivers/chromedriver2.exe"


# ip = get('https://api.ipify.org').text
# print('My public IP address is: {}'.format(ip))
#
# if ip == '35.158.30.212':
#     chrome_driver = "D:/automation-newforexqa/src/main/python/resources/grid/drivers/chromedriver.exe"
# elif ip == '35.158.90.50':
#     chrome_driver = "C:/Users/Panda102/automation-newforexqa/src/main/python/resources/grid/drivers/chromedriver2.exe"
