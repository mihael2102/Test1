from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select

class CALoginPage(CRMBasePage):

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return CALoginPage(self.driver)

    def click_sign_up(self):
        sign_up_button = super().wait_load_element("//button[contains (text(), 'Sign Up')]")
        sign_up_button.click()
        Logging().reportDebugStep(self, "Click Sign Up")
        return CALoginPage(self.driver)

    def fill_first_name(self, first_name):
        input_first_name = super().wait_load_element("//input[@name = 'firstName']")
        input_first_name.send_keys(first_name)
        Logging().reportDebugStep(self, "Fill First Name : " + first_name)
        return CALoginPage(self.driver)

    def fill_last_name(self, last_name):
        input_last_name = super().wait_load_element("//input[@name = 'lastName']")
        input_last_name.send_keys(last_name)
        Logging().reportDebugStep(self, "Fill Last Name : " + last_name)
        return CALoginPage(self.driver)

    def fill_email(self, email):
        input_email = super().wait_load_element("//input[@name = 'email']")
        input_email.send_keys(email)
        Logging().reportDebugStep(self, "Fill email : " + email)
        return CALoginPage(self.driver)

    def fill_phone(self, phone):
        input_phone = super().wait_load_element("//input[@name = 'phone']")
        input_phone.send_keys(phone)
        Logging().reportDebugStep(self, "Fill phone : " + phone)
        return CALoginPage(self.driver)

    def fill_password(self, password):
        input_password = super().wait_load_element("//input[@name = 'password']")
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Fill password : " + password)
        return CALoginPage(self.driver)

    def fill_confirm_password(self, password):
        input_password = super().wait_load_element("//input[@name = 'passwordConfirm']")
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Fill confirm : " + password)
        return CALoginPage(self.driver)

    def check_box_accept(self):
        check_box = super().wait_load_element("//span[contains (text(), 'Terms and Conditions')]")
        check_box.click()
        Logging().reportDebugStep(self, "Check 'By checking this box I accept the Terms and Conditions and confirm that I am over 18 year of age'")
        return CALoginPage(self.driver)

    def click_submit(self):
        submit_button = super().wait_load_element("//button[contains (text(), 'Submit')]")
        submit_button.click()
        Logging().reportDebugStep(self, "Click submit")
        return CALoginPage(self.driver)

    def click_hi_guest(self):
        hi_guest_button = super().wait_load_element("//div[contains (text(), 'Hi, Guest')]")
        hi_guest_button.click()
        Logging().reportDebugStep(self, "Click Hi, Guest")
        return CALoginPage(self.driver)

    def click_transactions_history(self):
        transactions_history_button = super().wait_load_element("//li[contains (text(), 'Transaction History ')]")
        transactions_history_button.click()
        Logging().reportDebugStep(self, "Click Transaction History")
        return CALoginPage(self.driver)

    def select_data_birth_day(self, data_birth_day):
        data = self.driver.find_element_by_xpath("//custom-select[@name='day']//span[text()='%s']" % data_birth_day)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select data birth : " + data_birth_day)
        return CALoginPage(self.driver)

    def select_data_birth_month(self, data_birth_month):
        data = self.driver.find_element_by_xpath("//custom-select[@name='month']//span[text()='%s']" % data_birth_month)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select month birth : " + data_birth_month)
        return CALoginPage(self.driver)

    def select_data_birth_year(self, data_birth_year):
        data = self.driver.find_element_by_xpath("//custom-select[@name='year']//span[text()='%s']" % data_birth_year)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select year birth : " + data_birth_year)
        return CALoginPage(self.driver)

    def choose_currency(self, currency):
        data = self.driver.find_element_by_xpath("//custom-select[@name='currency']//span[text()='%s']" % currency)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select currency : " + currency)
        return CALoginPage(self.driver)

    def choose_citizenship(self, citizenship):
        data = self.driver.find_element_by_xpath("//custom-select[@name='citizenship']//span[text()='%s']" % citizenship)
        self.driver.execute_script("arguments[0].click();", data)
        d = self.driver.find_element_by_xpath("/html/body/div[3]/panda-forex-personal-profile/div/personal-popup/div/div[2]/div[2]/div/h1")
        d.click()
        Logging().reportDebugStep(self, "Select currency : " + citizenship)
        return CALoginPage(self.driver)

    def fill_city(self, city):
        input_city = super().wait_load_element("//input[@name = 'city']")
        input_city.send_keys(city)
        Logging().reportDebugStep(self, "Fill city : " + city)
        return CALoginPage(self.driver)

    def fill_zip_code(self, zip_code):
        input_zip_code = super().wait_load_element("//input[@name = 'postCode']")
        input_zip_code.send_keys(zip_code)
        Logging().reportDebugStep(self, "Fill zip_code : " + zip_code)
        return CALoginPage(self.driver)

    def fill_address(self, address):
        input_address = super().wait_load_element("//input[@name = 'address']")
        input_address.send_keys(address)
        Logging().reportDebugStep(self, "Fill address : " + address)
        return CALoginPage(self.driver)

    def click_next(self):
        submit_button = super().wait_load_element("//button[contains (text(), 'Next')]")
        submit_button.click()
        Logging().reportDebugStep(self, "Click Next")
        return CALoginPage(self.driver)

    def verify(self):
        sleep(10)
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        i = 0
        for elem in elems:
            link = elem.get_attribute("href")
            if 'trading-platform' in link:
                i += 1
        if i > 1:
            Logging().reportDebugStep(self, "You are on the Webtrader page")
        return CALoginPage(self.driver)

    def click_hi_user(self, user_name):
        click_hi_user = super().wait_load_element("//span[contains(text(), '%s')]" % user_name)
        click_hi_user.click()
        Logging().reportDebugStep(self, "Click Hi, " + user_name)
        return CALoginPage(self.driver)

    def sign_out(self):
        sign_out = super().wait_load_element("//li[contains(text(), 'Sign Out')]")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "Click Sign Out")
        return CALoginPage(self.driver)

    def verify_start_page(self):
        sleep(3)
        start_page = self.driver.find_element_by_xpath("//*[@id='Content']//h3[contains(text(), 'Join us')]")
        Logging().reportDebugStep(self, "Verify start page")
        return CALoginPage(self.driver)

    def login(self):
        login_button = super().wait_load_element("//button[contains(text(), 'Login')]")
        login_button.click()
        Logging().reportDebugStep(self, "Click Login")
        return CALoginPage(self.driver)

    def enter_email(self, email):
        input_email = super().wait_load_element("//input[@name='login']")
        input_email.send_keys(email)
        Logging().reportDebugStep(self, "Enter Email")
        return CALoginPage(self.driver)

    def enter_password(self, password):
        input_email = super().wait_load_element("//input[@name='password']")
        input_email.send_keys(password)
        Logging().reportDebugStep(self, "Enter Email")
        return CALoginPage(self.driver)

    def click_login(self):
        login_button = super().wait_load_element("//button[@class = 'forex-button-pandats short-button-pandats login-button-pandats'][contains(text(), 'Login')]")
        login_button.click()
        Logging().reportDebugStep(self, "Click Login in pop up")
        return CALoginPage(self.driver)

    def verify_client(self, user_name):
        verify_client = super().wait_load_element("//span[contains(text(), '%s')]" % user_name)
        client = verify_client.text
        Logging().reportDebugStep(self, "Verify " + client)
        return client