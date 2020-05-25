import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from time import sleep


class SignUpFirstStepPage(CRMBasePage):

    def first_step_sign_up(self, url=None, field1=None, first_name=None, field2=None, last_name=None, field3=None,
                           email=None, field4=None, phone=None, field5=None, password=None, field6=None, password2=None,
                           field7=None, promo_code=None, country=None):
        self.open_first_tab_page(url)
        self.close_campaign_banner()
        if global_var.current_brand_name == "trade99":
            self.click_sign_in_btn()
        self.click_sign_up()
        if field1 and first_name:
            self.set_text_field(field1, first_name)
        if field2 and last_name:
            self.set_text_field(field2, last_name)
        if field3 and email:
            self.set_text_field(field3, email)
        if field4 and phone:
            self.set_text_field(field4, phone)
        if field5 and password:
            self.set_text_field(field5, password)
        if field6 and password2:
            self.set_text_field(field6, password2)
        if field7 and promo_code:
            self.set_text_field(field7, promo_code)
        if country:
            self.select_country_first_step(country)
        self.check_box_accept()
        self.risk_check_box_accept()
        self.click_submit()
        self.close_payment_popup()
        return SignUpFirstStepPage(self.driver)

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return SignUpFirstStepPage(self.driver)

    def close_campaign_banner(self):
        sleep(3)
        try:
            super().wait_load_element("(//div[contains(@class,'Campaign__')])[2]", timeout=15)
            campaign_close_btn = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["campaign_close_btn"])
            self.driver.execute_script("arguments[0].click();", campaign_close_btn)
            Logging().reportDebugStep(self, "Campaign banner is closed")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Campaign banner doesn't appears")
        return SignUpFirstStepPage(self.driver)

    def click_sign_up(self):
        sleep(1)
        Logging().reportDebugStep(self, "Click Sign Up")
        try:
            sign_up_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["sign_up"])
            sleep(1)
            try:
                sign_up_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", sign_up_button)
        except:
            Logging().reportDebugStep(self, "There is no panda plugin")
            Logging().reportDebugStep(self, "NOT RUNNED")
        return SignUpFirstStepPage(self.driver)

    def click_sign_in_btn(self):
        sleep(1)
        try:
            login_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["login_btn"])
            self.driver.execute_script("arguments[0].click();", login_button)
        except(NoSuchElementException, TimeoutException):
            sleep(1)
            self.refresh_page()
            sleep(1)
            login_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["login_btn"], timeout=35)
            self.driver.execute_script("arguments[0].click();", login_button)
        Logging().reportDebugStep(self, "Click Login button")
        return SignUpFirstStepPage(self.driver)

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        try:
            input_field = super().wait_load_element("//input[@placeholder='%s']" % field)
            sleep(0.1)
            input_field.clear()
            input_field.send_keys(text)
        except:
            Logging().reportDebugStep(self, "The " + field + " field doesn't exist or read only")
        return SignUpFirstStepPage(self.driver)

    def select_country_first_step(self, country):
        try:
            country_list = super().wait_element_to_be_clickable("//select[@id='country']", timeout=5)
            select_status = Select(country_list)
            select_status.select_by_visible_text(country)
            Logging().reportDebugStep(self, "Select Country(first step): " + country)
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "There are no 'Select Country' field on first registration step")
        return CALoginPage(self.driver)

    def check_box_accept(self):
        check_box = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["check_box_accept"])
        try:
            check_box.click()
        except:
            self.driver.execute_script("arguments[0].click();", check_box)
        Logging().reportDebugStep(self,
            "Check 'By checking this box I accept the Terms and Conditions and confirm that I am over 18 year of age'")
        return CALoginPage(self.driver)

    def risk_check_box_accept(self):
        try:
            check_box = super().wait_load_element(
                "//span[contains(text(),'CFD and Forex trading involves substantial risk')]", timeout=5)
            check_box.click()
            Logging().reportDebugStep(self,
             "Check 'CFD and Forex trading involves substantial risk and may result in the loss of the invested capital'")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Risk check box doesn't exist")
        return CALoginPage(self.driver)

    def click_submit(self):
        submit_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["submit_btn"])
        try:
            submit_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", submit_button)
        Logging().reportDebugStep(self, "Click submit")
        return SignUpFirstStepPage(self.driver)

    def close_payment_popup(self):
        sleep(1)
        try:
            sleep(1)
            close_payment_btn = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["close_payment_btn"], timeout=5)
            self.driver.execute_script("arguments[0].click();", close_payment_btn)
            Logging().reportDebugStep(self, "Close the pop up 'Choose a payment method'")
            try:
                sleep(0.1)
                approve_close_btn = super().wait_element_to_be_clickable("//*[@id='dialog_btn_leave']", timeout=5)
                self.driver.execute_script("arguments[0].click();", approve_close_btn)
                Logging().reportDebugStep(self, "Click 'I'm Sure' button")
            except(NoSuchElementException, TimeoutException):
                Logging().reportDebugStep(self, "There is no approving button")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Pop up 'Choose a payment method' wasn't opened")
        return SignUpFirstStepPage(self.driver)
