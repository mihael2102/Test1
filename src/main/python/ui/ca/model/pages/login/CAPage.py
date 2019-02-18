from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants

class CAPage(CRMBasePage):

    def open_manage_accounts(self):
        manage_accounts_button = super().wait_element_to_be_clickable \
                    ("//li[@class='ng-star-inserted'][contains(text(), 'Manage Accounts')]")
        sleep(1)
        manage_accounts_button.click()
        Logging().reportDebugStep(self, "Click Manage Accounts button")
        return CAPage(self.driver)

    def open_new_account_btn(self):
        open_new_account_button = super().wait_element_to_be_clickable \
                    ("//button[@class='forex-button-pandats'][contains(text(), 'Open New Account')]")
        sleep(1)
        open_new_account_button.click()
        Logging().reportDebugStep(self, "Click Open New Account button")
        return CAPage(self.driver)

    def select_account_type(self, account_type):
        sleep(1)
        ac_type = self.driver.find_element_by_xpath("//span[@class='itemLabel'][contains(text(), '%s')]" % account_type)
        print(ac_type)
        self.driver.execute_script("arguments[0].click();", ac_type)
        Logging().reportDebugStep(self, "Select account type : " + account_type)
        return CAPage(self.driver)

    def select_currency(self, currency):
        data = self.driver.find_element_by_xpath("//span[@class='itemLabel'] \
                                                    [contains(text(), '%s')]" % currency)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select currency : " + currency)
        return CAPage(self.driver)

    def select_leverage_level(self, leverage_level):
        data = self.driver.find_element_by_xpath("//span[@class='itemLabel'] \
                                                    [contains(text(), '%s')]" % leverage_level)
        sleep(1)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select leverage level : " + leverage_level)
        return CAPage(self.driver)

    def click_create_account(self):
        create_account_btn = super().wait_load_element("//button[@class='forex-button-pandats'][contains(text(), 'Create Account')]")
        self.driver.execute_script("arguments[0].click();", create_account_btn)
        Logging().reportDebugStep(self, "Click Create Account")
        return CAPage(self.driver)

    def additional_account_created(self):
        sleep(2)
        accounts = self.driver.find_elements_by_xpath("//panda-forex-client-area/div/div/client-area-popup/div/div[2]/ \
                                                      div[2]/div[2]/manage/div[2]/accounts/div/div/perfect-scrollbar/ \
                                                      div/div[1]/div/table/tbody/tr[2]")
        if len(accounts) == 0:
            Logging().reportDebugStep(self, "Additional live account was not created")
        else:
            Logging().reportDebugStep(self, "Additional live account was created successfully")

        return CAPage(self.driver)

    def open_demo_section(self):
        demo_btn = super().wait_load_element("//span[contains(text(), 'Demo')]")
        self.driver.execute_script("arguments[0].click();", demo_btn)
        Logging().reportDebugStep(self, "Click Demo accounts section")
        return CAPage(self.driver)

    def get_leverage(self):
        leverage = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                    self.__class__.__name__)["actual_leverage"]).text
        Logging().reportDebugStep(self, "The Leverage is " + leverage)
        return leverage

    def get_currency(self):
        currency = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                    self.__class__.__name__)["actual_currency"]).text
        Logging().reportDebugStep(self, "The Currency is " + currency)
        return currency

    def set_initial_deposit(self, in_deposit):
        input_initial_deposit = super().wait_load_element("//input[@name = 'deposit']")
        input_initial_deposit.clear()
        input_initial_deposit.send_keys(in_deposit)
        Logging().reportDebugStep(self, "Fill Initial Deposit : " + in_deposit)
        return CAPage(self.driver)

    def verify_init_deposit_error(self):
        sleep(1)
        message = self.driver.find_elements_by_xpath("//div[contains(text(), 'Minimum initial deposit is ')]")
        if len(message) == 0:
            Logging().reportDebugStep(self, "Validation message does not appear")
        else:
            Logging().reportDebugStep(self, "Validation message is displayed")

        return CAPage(self.driver)

    def verify_demo_account_created(self):
        sleep(2)
        accounts = self.driver.find_elements_by_xpath("//panda-forex-client-area/div/div/client-area-popup/div/div[2]/ \
                                                              div[2]/div[2]/manage/div[2]/accounts/div/div/perfect-scrollbar/ \
                                                              div/div[1]/div/table/tbody/tr[1]")
        if len(accounts) == 0:
            Logging().reportDebugStep(self, "Demo account was not created")
        else:
            Logging().reportDebugStep(self, "Demo account was created successfully")

        return CAPage(self.driver)

    def get_demo_account_number(self):
        CAConstants.DEMO_ACCOUNT_NUMBER = super().wait_load_element("//accounts/div/div/perfect-scrollbar/ \
                                                                    div/div[1]/div/table/tbody/tr/td[1]").text
        print(CAConstants.DEMO_ACCOUNT_NUMBER)
        Logging().reportDebugStep(self, "Demo account number is " + CAConstants.DEMO_ACCOUNT_NUMBER)
        return CAPage(self.driver)

    def open_live_section(self):
        sleep(1)
        live_btn = super().wait_load_element("//li[@class='header-menu-pandats']/span[contains(text(), 'Live')]")
        self.driver.execute_script("arguments[0].click();", live_btn)
        Logging().reportDebugStep(self, "Open Live account's section")
        return CAPage(self.driver)

    def get_live_account_number(self):
        sleep(1)
        CAConstants.LIVE_ACCOUNT_NUMBER = super().wait_load_element("//accounts/div/div/perfect-scrollbar/div/ \
                                                                        div[1]/div/table/tbody/tr[2]/td[1]").text
        print(CAConstants.LIVE_ACCOUNT_NUMBER)
        Logging().reportDebugStep(self, "Live account number is " + CAConstants.LIVE_ACCOUNT_NUMBER)
        return CAPage(self.driver)

    def open_accounts_list(self, server):
        sleep(1)
        accounts_list = super().wait_load_element("//span[@class='account-type-pandats ng-star-inserted'] \
                                                [contains(text(), '%s')]" % server)
        self.driver.execute_script("arguments[0].click();", accounts_list)
        Logging().reportDebugStep(self, "Open list accounts")
        return CAPage(self.driver)

    def switch_to_account(self, account_number, account_server):
        sleep(1)
        account = super().wait_element_to_be_clickable("//div[@class='account-title-pandats roboto-pandats'] \
                                                        [contains(text(), '%s')]" % account_number)
        self.driver.execute_script("arguments[0].click();", account)
        Logging().reportDebugStep(self, "Switch to " + account_server + " account")
        return CAPage(self.driver)

    def verify_active_account_currency(self, expected_currency):
        actual_currency = ''
        if expected_currency == 'EUR':
            if self.driver.find_element_by_xpath("//li[@class='account-pandats active-pandats'] \
                                                            /div[@class='account-wrapper-pandats'] \
                                                            /div[@class='account-details-pandats'] \
                                                            /div[@class='tr-row-pandats account-data-pandats'] \
                                                            /div[contains(text(), '€')]"):
                actual_currency = 'EUR'
            assert expected_currency == actual_currency
            Logging().reportDebugStep(self, "Currency of active account is: " + actual_currency)
        else:
            if self.driver.find_element_by_xpath("//li[@class='account-pandats active-pandats'] \
                                                            /div[@class='account-wrapper-pandats'] \
                                                            /div[@class='account-details-pandats'] \
                                                            /div[@class='tr-row-pandats account-data-pandats'] \
                                                            /div[contains(text(), 'BTC')]"):
                actual_currency = 'BTC'
            assert expected_currency == actual_currency
            Logging().reportDebugStep(self, "Currency of active account is: " + actual_currency)

        return CAPage(self.driver)

    def verify_active_account_number(self, expected_acc_number):
        actual_acc_number = self.driver.find_element_by_xpath("//div[@class='login-pandats'][contains(text(), '%s')]" \
                                                              % expected_acc_number).text
        if len(actual_acc_number) != 0:
            Logging().reportDebugStep(self, "Active account number is verified")
        else:
            Logging().reportDebugStep(self, "Active account number was not verified")

    def open_personal_details(self):
        personal_details_btn = super().wait_element_to_be_clickable("//li[@class='ng-star-inserted'] \
                                                                    [contains(text(), 'Personal Details')]")
        self.driver.execute_script("arguments[0].click();", personal_details_btn)
        sleep(1)
        Logging().reportDebugStep(self, "Open Personal Details")
        return CAPage(self.driver)

    def edit_first_name(self, first_name):
        first_name_field = super().wait_load_element("//input[@name='firstName']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "Edit First Name")
        return CAPage(self.driver)

    def edit_last_name(self, last_name):
        last_name_field = super().wait_load_element("//input[@name='lastName']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "Edit Last Name")
        return CAPage(self.driver)

    def edit_citizenship(self, citizenship):
        citizenship_field = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                    self.__class__.__name__)["citizenship"] % citizenship)
        self.driver.execute_script("arguments[0].click();", citizenship_field)
        d = self.driver.find_element_by_xpath("//label[contains (text(), 'First Name')]")
        d.click()
        Logging().reportDebugStep(self, "Edit citizenship : " + citizenship)
        return CAPage(self.driver)

    def edit_city(self, city):
        city_field = super().wait_load_element("//input[@name='city']")
        city_field.clear()
        city_field.send_keys(city)
        Logging().reportDebugStep(self, "Edit City field")
        return CAPage(self.driver)

    def edit_zip(self, zipcode):
        zip_field = super().wait_load_element("//input[@name='postCode']")
        zip_field.clear()
        zip_field.send_keys(zipcode)
        Logging().reportDebugStep(self, "Edit Zip code field")
        return CAPage(self.driver)

    def edit_address(self, address):
        address_field = super().wait_load_element("//input[@name='address']")
        address_field.clear()
        address_field.send_keys(address)
        Logging().reportDebugStep(self, "Edit Address field")
        return CAPage(self.driver)

    def click_save_changes_btn(self):
        save_changes_btn = super().wait_element_to_be_clickable("//button[contains (text(), 'Save Changes')]")
        self.driver.execute_script("arguments[0].click();", save_changes_btn)
        Logging().reportDebugStep(self, "Click Save Changes button")
        return CAPage(self.driver)

    def get_first_name(self):
        first_name = super().wait_load_element("//input[@name='firstName']").text
        Logging().reportDebugStep(self, "Client's First Name is " + first_name)
        return first_name

    def get_last_name(self):
        last_name = super().wait_load_element("//input[@name='lastName']").text
        Logging().reportDebugStep(self, "Client's Last Name is " + last_name)
        return last_name

    def get_citizenship(self):
        citizenship = super().wait_load_element("//custom-select[@name='citizenship']").text
        Logging().reportDebugStep(self, "Client's citizenship : " + citizenship)
        return citizenship

    def get_city(self):
        city = super().wait_load_element("//input[@name='city']").text
        Logging().reportDebugStep(self, "Client's City : " + city)
        return city

    def get_zipcode(self):
        postalcode = super().wait_load_element("//input[@name='postCode']").text
        Logging().reportDebugStep(self, "Client's Zip code is : " + postalcode)
        return postalcode

    def get_address(self):
        address = super().wait_load_element("//input[@name='address']").text
        Logging().reportDebugStep(self, "Client's Address is : " + address)
        return address