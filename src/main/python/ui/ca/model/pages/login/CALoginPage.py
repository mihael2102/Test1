from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class CALoginPage(CRMBasePage):

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return CALoginPage(self.driver)

    def click_sign_up(self):
        sign_up_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["sign_up"])
        sign_up_button.click()
        Logging().reportDebugStep(self, "Click Sign Up")
        return CALoginPage(self.driver)

    def select_country(self, country):
        country_drop_down = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["country_registr"])
        country_drop_down.click()
        country = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["select_country"] % country)
        country.click()
        Logging().reportDebugStep(self, "Select country")
        return CALoginPage(self.driver)

    def fill_first_name(self, first_name):
        input_first_name = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["first_name"])

        input_first_name.send_keys(first_name)
        Logging().reportDebugStep(self, "Fill First Name : " + first_name)
        return CALoginPage(self.driver)

    def fill_last_name(self, last_name):
        input_last_name = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["last_name"])
        input_last_name.send_keys(last_name)
        Logging().reportDebugStep(self, "Fill Last Name : " + last_name)
        return CALoginPage(self.driver)

    def fill_email(self, email):
        input_email = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["email"])
        input_email.send_keys(email)
        Logging().reportDebugStep(self, "Fill email : " + email)
        return CALoginPage(self.driver)

    def fill_area_code(self, area):
        input_phone = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["phone_area"])
        input_phone.send_keys(area)
        Logging().reportDebugStep(self, "Fill phone : " + area)
        return CALoginPage(self.driver)

    def fill_phone(self, phone):
        input_phone = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["phone"])
        input_phone.send_keys(phone)
        Logging().reportDebugStep(self, "Fill phone : " + phone)
        return CALoginPage(self.driver)

    def fill_password(self, password):
        input_password = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["password"])
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Fill password : " + password)
        return CALoginPage(self.driver)

    def fill_confirm_password(self, password):
        input_password = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["confirm_password"])
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Fill confirm : " + password)
        return CALoginPage(self.driver)

    def check_box_accept(self):
        check_box = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["terms_conditions"])
        self.driver.execute_script("arguments[0].click();", check_box)
        # check_box.click()
        Logging().reportDebugStep(self, "Check 'By checking this box I accept the Terms and Conditions and confirm that I am over 18 year of age'")
        return CALoginPage(self.driver)

    def check_box_accept_new(self):
        check_box = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_box_2"])
        self.driver.execute_script("arguments[0].click();", check_box)
        Logging().reportDebugStep(self,
                                  "Check box in registration form 2")
        return CALoginPage(self.driver)

    def click_submit(self):
        submit_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["submit"])
        self.driver.execute_script("arguments[0].click();", submit_button)
        Logging().reportDebugStep(self, "Click Submit")
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

    def enter_data_birth(self, data):
        enter_data_birth = super().wait_load_element("//input[@class = 'form-control hasDatepicker']")
        enter_data_birth.send_keys(data)
        Logging().reportDebugStep(self, "Fill data birth : " + data)
        return CALoginPage(self.driver)

    def close_welcome_message(self):
        btn_continue = super().wait_load_element("//*[@id='welcome_continue']")
        btn_continue.click()
        Logging().reportDebugStep(self, "Click Continue button")
        return CALoginPage(self.driver)

    def select_data_birth_day(self, data_birth_day):
        sleep(3)
        data = super().wait_load_element("//select[@id='dobday']")
        data.click()
        datad = self.driver.find_element_by_xpath("//select[@id='dobday']//option[text()='%s']" % data_birth_day)
        datad.click()
        Logging().reportDebugStep(self, "Select day of birth : " + data_birth_day)
        return CALoginPage(self.driver)

    def select_data_birth_month(self, data_birth_month):
        sleep(3)
        data = self.driver.find_element_by_xpath("//select[@id='dobmonth']")
        data.click()
        datad = self.driver.find_element_by_xpath("//select[@id='dobmonth']//option[text()='%s']" % data_birth_month)
        datad.click()
        Logging().reportDebugStep(self, "Select month birth : " + data_birth_month)
        return CALoginPage(self.driver)

    def select_data_birth_year(self, data_birth_year):
        sleep(3)
        data = self.driver.find_element_by_xpath("//select[@id='dobyear']")
        data.click()
        datad = self.driver.find_element_by_xpath("//select[@id='dobyear']//option[text()='%s']" % data_birth_year)
        datad.click()
        Logging().reportDebugStep(self, "Select year birth : " + data_birth_year)
        return CALoginPage(self.driver)

    def choose_currency(self, currency):
        data = self.driver.find_element_by_xpath("//select[@id='ddlCurrency']//option[text()='%s']" % currency)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select currency : " + currency)
        return CALoginPage(self.driver)

    def choose_citizenship(self, citizenship):
        data = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["citizenship"] % citizenship)
        self.driver.execute_script("arguments[0].click();", data)
        d = self.driver.find_element_by_xpath("//label[contains (text(), 'First Name')]")
        d.click()
        Logging().reportDebugStep(self, "Select currency : " + citizenship)
        return CALoginPage(self.driver)

    def fill_city(self, city):
        sleep(3)
        input_city = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["city"])
        input_city.send_keys(city)
        Logging().reportDebugStep(self, "Fill city : " + city)
        return CALoginPage(self.driver)

    def fill_zip_code(self, zip_code):
        sleep(3)
        input_zip_code = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["zip_code"])
        input_zip_code.send_keys(zip_code)
        Logging().reportDebugStep(self, "Fill zip_code : " + zip_code)
        return CALoginPage(self.driver)

    def fill_address(self, address):
        sleep(3)
        input_address = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["address"])
        input_address.send_keys(address)
        Logging().reportDebugStep(self, "Fill address : " + address)
        return CALoginPage(self.driver)

    def account_type(self, type):
        data = self.driver.find_element_by_xpath("//custom-select[@name='customerType']//span[text()='%s']" % type)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select type : " + type)
        return CALoginPage(self.driver)

    def click_next(self):
        submit_button = super().wait_load_element("//*[@id='continueToEmploymentQ']")
        submit_button.click()
        Logging().reportDebugStep(self, "Click Next")
        return CALoginPage(self.driver)

    def click_next_open_live_account(self):
        if global_var.current_brand_name == "oinvestsa" or global_var.current_brand_name == "triomarkets" or global_var.current_brand_name == "itrader" or global_var.current_brand_name == "gmo":
            submit_button = super().wait_load_element("//*[@id='continueToEmploymentQ']")
        else:
            submit_button = super().wait_load_element("//*[@id='Next']")
        submit_button.click()
        Logging().reportDebugStep(self, "Click Next")
        return CALoginPage(self.driver)

    def my_account_link(self):
        sleep(2)
        link = super().wait_load_element("//a[contains(text(), 'MY ACCOUNT')]")
        link.click()
        Logging().reportDebugStep(self, "Click MY ACCOUNT")
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
        else:
            Logging().reportDebugStep(self, "You are not on the Webtrader page")

        return CALoginPage(self.driver)

    def click_hi_user(self, user_name):
        click_hi_user = super().wait_load_element("//span[contains(text(), '%s')]" % user_name)
        click_hi_user.click()
        Logging().reportDebugStep(self, "Click Hi, " + user_name)
        return CALoginPage(self.driver)

    def sign_out(self):
        sign_out = super().wait_load_element("//*[@id='dnn_dnnLogin_enhancedLoginLink']")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "Click Sign Out")
        return CALoginPage(self.driver)

    def login(self):
        login_button = super().wait_load_element("//*[@id='open-account-desktop']/div/li[1]/a")
        self.driver.execute_script("arguments[0].click();", login_button)
        Logging().reportDebugStep(self, "Click Login")
        return CALoginPage(self.driver)

    def enter_email(self, email):
        sleep(1)
        input_email = self.driver.find_element_by_xpath("//*[@id='dnn_ctr517_Login_Login_DNN_txtUsername']")
        self.driver.execute_script("arguments[0].click();", input_email)
        sleep(1)
        input_email.send_keys(email)
        Logging().reportDebugStep(self, "Enter Email: " + email)
        return CALoginPage(self.driver)

    def enter_password(self, password):
        sleep(1)
        input_password = self.driver.find_element_by_xpath("//*[@id='dnn_ctr517_Login_Login_DNN_txtPassword']")
        self.driver.execute_script("arguments[0].click();", input_password)
        sleep(1)
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Enter Password: " + password)
        return CALoginPage(self.driver)

    def click_login(self):
        login_button = super().wait_load_element("//*[@id='dnn_ctr517_Login_Login_DNN_cmdLogin']")
        login_button.click()
        Logging().reportDebugStep(self, "Click Login in pop up")
        return CALoginPage(self.driver)

    def click_personal_details(self):
        button = super().wait_load_element("//a[contains(text(), 'Personal Details')]")
        button.click()
        Logging().reportDebugStep(self, "Go to Personal Details module")
        return CALoginPage(self.driver)

    def update_address(self, address):
        input = super().wait_load_element("//*[@id='txtAddress']")
        input.send_keys(address)
        Logging().reportDebugStep(self, "Enter new address")
        return CALoginPage(self.driver)

    def update_city(self, city):
        input = super().wait_load_element("//*[@id='txtCity']")
        input.send_keys(city)
        Logging().reportDebugStep(self, "Enter new city")
        return CALoginPage(self.driver)

    def update_code(self, code):
        input = super().wait_load_element("//*[@id='txtPostalZipCode']")
        input.send_keys(code)
        Logging().reportDebugStep(self, "Enter new code")
        return CALoginPage(self.driver)

    def submit_personal_details(self):
        submit_personal_details = super().wait_load_element("//*[@id='btnSubmit']")
        self.driver.execute_script("arguments[0].click();", submit_personal_details)
        Logging().reportDebugStep(self, "Click submit personal details")
        return CALoginPage(self.driver)

    def verify_client(self, user_name):
        verify_client = super().wait_load_element("//a[contains(text(), '%s')]" % user_name)
        client = verify_client.text
        Logging().reportDebugStep(self, "Verify " + client)
        return client

    def click_my_account(self):
        sleep(5)
        my_account_brn = super().wait_load_element("/html/body/header/div/div[2]/div[1]/label/div[1]/span")
        my_account_brn.click()
        Logging().reportDebugStep(self, "My account button click")
        return CALoginPage(self.driver)

    def logout(self):
        logout_btn = super().wait_load_element("/html/body/header/div/div[2]/div[1]/label/div[2]/div/span")
        self.driver.execute_script("arguments[0].click();", logout_btn)
        Logging().reportDebugStep(self, "Logout click")
        return CALoginPage(self.driver)

    def account_details(self):
        logout_btn = super().wait_load_element("/html/body/header/div/div[2]/div[1]/label/div[2]/div/a[6]")
        self.driver.execute_script("arguments[0].click();", logout_btn)
        Logging().reportDebugStep(self, "Account details click")
        return CALoginPage(self.driver)