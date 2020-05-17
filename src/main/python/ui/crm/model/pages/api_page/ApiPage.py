from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException
import autoit
import os
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class ApiPage(CRMBasePage):

    def check_page_from_token(self):
        sleep(5)
        payment_details = super().wait_load_element("//h1[contains(text(),'Payment Details')]", timeout=35).text
        Logging().reportDebugStep(self, "Check login token")
        return payment_details

    def check_login_token(self):
        sleep(5)
        check_token = super().wait_load_element(
            "//*[@id='api-System-LoginToken-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check login token: " + check_token)
        return check_token

    def send_login_token(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,
                                            "//*[@id='api-System-LoginToken-0.0.0']/form/fieldset/div[4]/div/button")
        customer_module.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def enter_email_for_login_token(self, email):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-email-System-LoginToken-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(email)
        Logging().reportDebugStep(self, "Enter email")
        return ApiPage(self.driver)

    def login_token_module(self):
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//a[contains(text(),'Login token')]")
            read_leads_module = self.driver.find_element(By.XPATH, "//*[@id='scrollingNav']/ul/li[24]/a")
            read_leads_module.click()
            Logging().reportDebugStep(self, "Open login token module")
            return ApiPage(self.driver)
        except NoSuchElementException:
            Logging().reportDebugStep(self, "Login token module does not exist")
            return ApiPage(self.driver)

    def check_read_leads_token(self):
        sleep(5)
        check_token = super().wait_load_element(
            "//*[@id='api-Leads-readLeads-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token read leads details: " + check_token)
        return check_token

    def send_leads_read(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,
                                                "//*[@id='api-Leads-readLeads-0.0.0']/form/fieldset/div[4]/div/button")
        customer_module.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def enter_leads_limit(self, limit):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-limit-Leads-readLeads-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(limit)
        Logging().reportDebugStep(self, "Enter limit")
        return ApiPage(self.driver)

    def enter_leads_page(self, page):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-page-Leads-readLeads-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(page)
        Logging().reportDebugStep(self, "Enter page")
        return ApiPage(self.driver)

    def read_leads_module(self):
        sleep(2)
        read_leads_module = self.driver.find_element(By.XPATH, "//*[@id='scrollingNav']/ul/li[22]/a")
        read_leads_module.click()
        Logging().reportDebugStep(self, "Open read leads module")
        return ApiPage(self.driver)

    def create_lead_module(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH, "//*[@id='scrollingNav']/ul/li[21]/a")
        customer_module.click()
        Logging().reportDebugStep(self, "Open create lead module")
        return ApiPage(self.driver)

    def enter_email_lead(self, email):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-email-Leads-Leads-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.clear()
        input.send_keys(email)
        Logging().reportDebugStep(self, "Enter email " + email)
        return ApiPage(self.driver)

    def enter_firstName_lead(self, fname):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-firstName-Leads-Leads-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.clear()
        input.send_keys(fname)
        Logging().reportDebugStep(self, "Enter first name " + fname)
        return ApiPage(self.driver)

    def enter_lastName_lead(self, lname):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-lastName-Leads-Leads-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.clear()
        input.send_keys(lname)
        Logging().reportDebugStep(self, "Enter last name " + lname)
        return ApiPage(self.driver)

    def enter_phone_lead(self, phone):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-phone-Leads-Leads-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.clear()
        input.send_keys(phone)
        Logging().reportDebugStep(self, "Enter phone " + phone)
        return ApiPage(self.driver)

    def check_create_lead_token(self):
        sleep(15)
        check_token = super().wait_load_element(
            "//*[@id='api-Leads-Leads-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token create lead: " + check_token)
        return check_token

    def send_create_lead(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,
                                                   "//*[@id='api-Leads-Leads-0.0.0']/form/fieldset/div[4]/div/button")
        customer_module.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def check_update_token(self):
        sleep(15)
        check_token = super().wait_load_element(
            "//*[@id='api-Customers-updateCustomer-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token read customers details: " + check_token)
        return check_token

    def send_update_customer(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,
                                        "//*[@id='api-Customers-updateCustomer-0.0.0']/form/fieldset/div[4]/div/button")
        customer_module.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def enter_email_for_update(self, email):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-email-Customers-updateCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(email)
        Logging().reportDebugStep(self, "Enter email")
        return ApiPage(self.driver)

    def change_first_name(self, name):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                    "//*[@id='sample-request-param-field-firstName-Customers-updateCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(name)
        Logging().reportDebugStep(self, "Change first name")
        return ApiPage(self.driver)

    def change_postalCode(self, code):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                    "//*[@id='sample-request-param-field-zip-Customers-updateCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(code)
        Logging().reportDebugStep(self, "Change postal code")
        return ApiPage(self.driver)

    def change_phone(self, phone):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-phone-Customers-updateCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(phone)
        Logging().reportDebugStep(self, "Change phone")
        return ApiPage(self.driver)

    def update_customer_module(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH, "//*[@id='scrollingNav']/ul/li[10]/a")
        customer_module.click()
        Logging().reportDebugStep(self, "Open update customer module")
        return ApiPage(self.driver)

    def check_reads_customer_details(self):
        sleep(5)
        check_token = super().wait_load_element(
            "//*[@id='api-Customers-readCustomers-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token read customers details: " + check_token)
        return check_token

    def send_read_customers(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,
                                        "//*[@id='api-Customers-readCustomers-0.0.0']/form/fieldset/div[4]/div/button")
        customer_module.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def enter_limit(self, limit):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-limit-Customers-readCustomers-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(limit)
        Logging().reportDebugStep(self, "Enter limit")
        return ApiPage(self.driver)

    def enter_page(self, page):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-page-Customers-readCustomers-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(page)
        Logging().reportDebugStep(self, "Enter page")
        return ApiPage(self.driver)

    def read_customers_module(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH, "//*[@id='scrollingNav']/ul/li[9]/a")
        customer_module.click()
        Logging().reportDebugStep(self, "Open Read Customers module")
        return ApiPage(self.driver)

    def check_read_customer_details(self):
        sleep(5)
        check_token = super().wait_load_element(
            "//*[@id='api-Customers-readCustomer-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token read customer details: " + check_token)
        return check_token

    def send_read_customer(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,
                                        "//*[@id='api-Customers-readCustomer-0.0.0']/form/fieldset/div[4]/div/button")
        customer_module.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def enter_email_for_read_customer(self, email):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-email-Customers-readCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(email)
        Logging().reportDebugStep(self, "Enter email")
        return ApiPage(self.driver)

    def read_customer_module(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH, "//*[@id='scrollingNav']/ul/li[8]/a")
        customer_module.click()
        Logging().reportDebugStep(self, "Open Read Customer module")
        return ApiPage(self.driver)

    def enter_refferal(self, refferal):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                        "//*[@id='sample-request-param-field-referral-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(refferal)
        Logging().reportDebugStep(self, "Enter refferal")
        return ApiPage(self.driver)

    def check_create_customer_token(self):
        sleep(15)
        check_token = super().wait_load_element(
            "//*[@id='api-Customers-createCustomer-0.0.0']/form/fieldset/div[5]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token: " + check_token)
        return check_token

    def enter_email(self, email):
        sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-email-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(email)
        Logging().reportDebugStep(self, "Enter email")
        return ApiPage(self.driver)

    def enter_password(self, password):
        input = self.driver.find_element(By.XPATH,
                                        "//*[@id='sample-request-param-field-password-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(password)
        Logging().reportDebugStep(self, "Enter password")
        return ApiPage(self.driver)

    def enter_country(self, country):
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-country-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(country)
        Logging().reportDebugStep(self, "Enter country")
        return ApiPage(self.driver)

    def enter_firstName(self, firstName):
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-firstName-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(firstName)
        Logging().reportDebugStep(self, "Enter First Name")
        return ApiPage(self.driver)

    def enter_lastName(self, lastName):
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-lastName-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(lastName)
        Logging().reportDebugStep(self, "Enter Last Name")
        return ApiPage(self.driver)

    def enter_phone(self, phone):
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='sample-request-param-field-phone-Customers-createCustomer-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input)
        input.send_keys(phone)
        Logging().reportDebugStep(self, "Enter phone")
        return ApiPage(self.driver)

    def send_create_customer(self):
        sleep(2)
        send = self.driver.find_element(By.XPATH,
                                        "//*[@id='api-Customers-createCustomer-0.0.0']/form/fieldset/div[4]/div/button")
        self.driver.execute_script("arguments[0].scrollIntoView();", send)
        send.click()
        Logging().reportDebugStep(self, "Click Send")
        return ApiPage(self.driver)

    def create_customer_module(self):
        sleep(2)
        customer_module = self.driver.find_element(By.XPATH,"//*[@id='scrollingNav']/ul/li[7]/a")
        customer_module.click()
        Logging().reportDebugStep(self, "Open Customer module")
        return ApiPage(self.driver)

    def enter_secret_key(self, partnerSecretKey):
        sleep(5)
        input_secret_key = self.driver.find_element(By.XPATH, "//*[@id='partnerSecretKey']")
        input_secret_key.send_keys(partnerSecretKey)
        Logging().reportDebugStep(self, "Enter Secret Key")
        return ApiPage(self.driver)

    def authorization_module(self):
        sleep(2)
        authorization_module = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Authorization')]")
        authorization_module.click()
        Logging().reportDebugStep(self, "Open Authorization module")
        return ApiPage(self.driver)

    def input_partner_id(self, partnerId):
        sleep(2)
        input_partnarId = self.driver.find_element(By.XPATH,"//*[@id='sample-request-param-field-partnerId-Authorization-Authorization-0_0_0']")
        self.driver.execute_script("arguments[0].scrollIntoView();", input_partnarId)
        input_partnarId.send_keys(partnerId)
        Logging().reportDebugStep(self, "Enter partnerId")
        return ApiPage(self.driver)

    def generate_time(self):
        sleep(2)
        time = self.driver.find_element(By.XPATH,"//*[@id='time-generator']")
        self.driver.execute_script("arguments[0].scrollIntoView();", time)
        time.click()
        Logging().reportDebugStep(self, "Generate time")
        return ApiPage(self.driver)

    def generate_accessKey(self):
        sleep(2)
        accessKey = self.driver.find_element(By.XPATH,"//*[@id='accessKey-generator']")
        self.driver.execute_script("arguments[0].scrollIntoView();", accessKey)
        accessKey.click()
        Logging().reportDebugStep(self, "Generate accessKey")
        return ApiPage(self.driver)

    def send_authorization(self):
        sleep(2)
        send = self.driver.find_element(By.XPATH, "//*[@id='api-Authorization-Authorization-0.0.0']/form/fieldset/div[3]/div/button")
        self.driver.execute_script("arguments[0].scrollIntoView();", send)
        send.click()
        Logging().reportDebugStep(self, "Click send")
        return ApiPage(self.driver)

    def check_token(self):
        sleep(5)
        check_token = super().wait_load_element(
            "//*[@id='api-Authorization-Authorization-0.0.0']/form/fieldset/div[4]/pre/code", timeout=35).text
        Logging().reportDebugStep(self, "Check token: " + check_token)
        return check_token
