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
        sleep(10)
        try:
            #check bunner exist
            self.driver.find_element_by_xpath("(//div[@class='Campaign__alphaLayer'])[2]")
            close_btn = self.driver.find_element_by_xpath("(//button[@title='Close'])[2]")
            close_btn.click()
            Logging().reportDebugStep(self, "Campaign bunner is closed")
        except NoSuchElementException:
            pass
        sign_up_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["sign_up"])
        sleep(1)
        sign_up_button.click()
        Logging().reportDebugStep(self, "Click Sign Up")
        return CALoginPage(self.driver)

    def fill_first_name(self, first_name):
        input_first_name = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["input_first_name"])
        input_first_name.send_keys(first_name)
        Logging().reportDebugStep(self, "Fill First Name : " + first_name)
        return CALoginPage(self.driver)

    def fill_last_name(self, last_name):
        input_last_name = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["input_last_name"])
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
        input_password = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["input_confirm_password"])
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Fill confirm : " + password)
        return CALoginPage(self.driver)

    def check_box_accept(self):
        check_box = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["check_box_accept"])
        check_box.click()
        Logging().reportDebugStep(self, "Check 'By checking this box I accept the Terms and Conditions and confirm that I am over 18 year of age'")
        return CALoginPage(self.driver)

    def click_submit(self):
        submit_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["submit_btn"])
        submit_button.click()
        Logging().reportDebugStep(self, "Click submit")
        return CALoginPage(self.driver)

    def click_hi_guest(self):
        sleep(1)
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
        sleep(2)
        if global_var.current_brand_name == "ptbanc":
            pick_list = super().wait_load_element("//span[contains(text(),'Day')]")
            pick_list.click()
            day = super().wait_load_element("//custom-select[@name='day']//span[text()='%s']" % data_birth_day)
            day.click()
        else:
            data = self.driver.find_element_by_xpath("//custom-select[@name='day']//span[text()='%s']" % data_birth_day)
            self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select data birth : " + data_birth_day)
        return CALoginPage(self.driver)

    def select_data_birth_month(self, data_birth_month):
        if global_var.current_brand_name == "ptbanc":
            super().wait_load_element("//span[contains(text(),'Month')]").click()
            super().wait_load_element("//custom-select[@name='month']//span[text()='%s']" % data_birth_month).click()
        else:
            data = self.driver.find_element_by_xpath("//custom-select[@name='month']//span[text()='%s']" % data_birth_month)
            self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select month birth : " + data_birth_month)
        return CALoginPage(self.driver)

    def select_data_birth_year(self, data_birth_year):
        if global_var.current_brand_name == "ptbanc":
            super().wait_load_element("//span[contains(text(),'Year')]").click()
            super().wait_load_element("//custom-select[@name='year']//span[text()='%s']" % data_birth_year).click()
        else:
            data = self.driver.find_element_by_xpath("//custom-select[@name='year']//span[text()='%s']" % data_birth_year)
            self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select year birth : " + data_birth_year)
        return CALoginPage(self.driver)

    def choose_currency(self, currency):
        if global_var.current_brand_name == "ptbanc":
            super().wait_load_element("//custom-select[@name='currency']").click()
            self.driver.find_element_by_xpath("//custom-select[@name='currency']//span[text()='%s']" % currency) \
                                                .click()
        else:
            data = self.driver.find_element_by_xpath("//custom-select[@name='currency']//span[text()='%s']" % currency)
            self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select currency : " + currency)
        return CALoginPage(self.driver)

    def choose_citizenship(self, citizenship):
        if global_var.current_brand_name == "ptbanc":
            pick_list_citizenship = super().wait_load_element("//span[contains(text(),'Please select')]")
            pick_list_citizenship.click()
            select_citizenship = self.driver.find_element_by_xpath("//custom-select[@name='citizenship'] \
                                                                    //span[text()='%s']" % citizenship)
            select_citizenship.click()
        else:
            data = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["citizenship"] % citizenship)
            self.driver.execute_script("arguments[0].click();", data)
            d = self.driver.find_element_by_xpath("//label[contains (text(), 'First Name')]")
            d.click()
        Logging().reportDebugStep(self, "Select citizenship : " + citizenship)
        return CALoginPage(self.driver)

    def fill_city(self, city):
        input_city = super().wait_load_element(
            global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["city"])
        input_city.send_keys(city)
        Logging().reportDebugStep(self, "Fill city : " + city)
        return CALoginPage(self.driver)

    def select_pt_b(self):
        btn_data = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[1]/div[2]/custom-select[1]/div/div[1]")
        btn_data.click()
        btn_data_s = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[1]/div[2]/custom-select[1]/div/div[2]/perfect-scrollbar/div/div[1]/div/span[3]")
        btn_data_s.click()
        btn_month = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[1]/div[2]/custom-select[2]/div/div[1]")
        btn_month.click()
        btn_month_s = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[1]/div[2]/custom-select[2]/div/div[2]/perfect-scrollbar/div/div[1]/div/span[2]")
        btn_month_s.click()
        btn_year = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[1]/div[2]/custom-select[3]/div/div[1]")
        btn_year.click()
        btn_year_s = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[1]/div[2]/custom-select[3]/div/div[2]/perfect-scrollbar/div/div[1]/div/span[4]")
        btn_year_s.click()
        btn_citiz = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[2]/custom-select/div/div[1]")
        btn_citiz.click()
        btn_citiz_s = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[2]/custom-select/div/div[2]/perfect-scrollbar/div/div[1]/div/span[3]")
        btn_citiz_s.click()
        btn_curr = super().wait_load_element("/html/body/panda-forex-personal-profile[2]/div/personal-popup/div/div[2]/div[2]/form/div[2]/div[2]/div/custom-select/div/div[1]")
        btn_curr.click()
        Logging().reportDebugStep(self, "Fill all fields")
        return CALoginPage(self.driver)

    def fill_zip_code(self, zip_code):
        input_zip_code = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["zip_code"])
        input_zip_code.send_keys(zip_code)
        Logging().reportDebugStep(self, "Fill zip_code : " + zip_code)
        return CALoginPage(self.driver)

    def fill_address(self, address):
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
        submit_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["next_btn"])
        submit_button.click()
        # if global_var.current_brand_name == "ptbanc":
        #     sleep(7)
        #     super().wait_load_element("//div[@class='close-pandats cmicon-close4']").click()
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
        else:
            Logging().reportDebugStep(self, "You are not on the Webtrader page")

        return CALoginPage(self.driver)

    def click_hi_user(self, user_name):
        click_hi_user = super().wait_load_element("//span[contains(text(), '%s')]" % user_name)
        sleep(7)
        self.driver.execute_script("arguments[0].click();", click_hi_user)
        # click_hi_user.click()
        Logging().reportDebugStep(self, "Click Hi, " + user_name)
        return CALoginPage(self.driver)

    def sign_out(self):
        sign_out = super().wait_load_element("//li[contains(text(), 'Sign Out')]")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "Click Sign Out")
        return CALoginPage(self.driver)

    def login(self):
        try:
            # check bunner exist
            self.driver.find_element_by_xpath("(//div[@class='Campaign__alphaLayer'])[2]")
            close_btn = self.driver.find_element_by_xpath("(//button[@title='Close'])[2]")
            close_btn.click()
            Logging().reportDebugStep(self, "Campaign bunner is closed")
        except NoSuchElementException:
            pass
        login_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["login_btn"])
        self.driver.execute_script("arguments[0].click();", login_button)
        Logging().reportDebugStep(self, "Click Login")
        return CALoginPage(self.driver)

    def enter_email(self, email):
        sleep(1)
        input_email = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["login_email_input"])
        self.driver.execute_script("arguments[0].click();", input_email)
        sleep(1)
        input_email.send_keys(email)
        Logging().reportDebugStep(self, "Enter Email")
        return CALoginPage(self.driver)

    def enter_password(self, password):
        sleep(1)
        input_password = self.driver.find_element_by_xpath("//input[@name='password']")
        self.driver.execute_script("arguments[0].click();", input_password)
        sleep(1)
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Enter Password")
        return CALoginPage(self.driver)

    def click_login(self):
        login_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["login_btn_2"])
        login_button.click()
        Logging().reportDebugStep(self, "Click Login in pop up")
        return CALoginPage(self.driver)

    def verify_client(self, user_name):
        verify_client = super().wait_load_element("//span[contains(text(), '%s')]" % user_name)
        client = verify_client.text
        Logging().reportDebugStep(self, "Verify " + client)
        return client

    def click_my_account(self):
        sleep(5)
        my_account_brn = super().wait_load_element("//span[contains(text(),'my account')]")
        my_account_brn.click()
        Logging().reportDebugStep(self, "My Account button is clicked")
        return CALoginPage(self.driver)

    def logout(self):
        logout_btn = super().wait_load_element("//a[contains(text(),'logout')]")
        self.driver.execute_script("arguments[0].click();", logout_btn)
        Logging().reportDebugStep(self, "Logout click")
        return CALoginPage(self.driver)

    def account_details(self):
        logout_btn = super().wait_load_element("//a[text()='account portal']")
        self.driver.execute_script("arguments[0].click();", logout_btn)
        Logging().reportDebugStep(self, "Account Portal is clicked")
        return CALoginPage(self.driver)

    def click_regulatory_confirmation(self):
        sleep(2)
        ok_btn = super().wait_load_element("//button[@class='forex-button-pandats simple-button-pandats'][contains(text(), 'OK')]")
        ok_btn.click()
        Logging().reportDebugStep(self, "Regulatory message is confirmed")
        return CALoginPage(self.driver)

    def click_customer_policy(self):
        customer_policy_checkbox = super().wait_load_element("//span[contains(text(),'I have read and agree')]")
        customer_policy_checkbox.click()
        Logging().reportDebugStep(self, "Customer Policy is confirmed")
        return CALoginPage(self.driver)

    def open_ca_menu(self):
        click_hi_user = super().wait_load_element("//span[@class='first-last-name-pandats ng-star-inserted'] \
                                                    [contains(text(),'Hi, ')]")
        sleep(7)
        self.driver.execute_script("arguments[0].click();", click_hi_user)
        Logging().reportDebugStep(self, "Open main menu")
        return CALoginPage(self.driver)