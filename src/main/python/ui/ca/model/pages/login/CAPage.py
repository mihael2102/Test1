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
        leverage = super().wait_load_element("//accounts/div/div/perfect-scrollbar/div/div[1]/div/table/tbody/tr/td[2]") \
                                                .text
        Logging().reportDebugStep(self, "The Leverage is " + leverage)
        return leverage

    def get_currency(self):
        currency = super().wait_load_element("//accounts/div/div/perfect-scrollbar/div/div[1]/div/table/tbody/tr/td[3]") \
                                                .text
        Logging().reportDebugStep(self, "The Leverage is " + currency)
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
        live_btn = super().wait_load_element("//li[@class='header-menu-pandats']/span[contains(text(), 'Live')]")
        self.driver.execute_script("arguments[0].click();", live_btn)
        Logging().reportDebugStep(self, "Click Live account's section")
        return CAPage(self.driver)

    def get_live_account_number(self):
        sleep(2)
        CAConstants.LIVE_ACCOUNT_NUMBER = super().wait_load_element("//accounts/div/div/perfect-scrollbar/div/ \
                                                                        div[1]/div/table/tbody/tr[2]/td[1]").text
        print(CAConstants.LIVE_ACCOUNT_NUMBER)
        Logging().reportDebugStep(self, "Live account number is " + CAConstants.LIVE_ACCOUNT_NUMBER)
        return CAPage(self.driver)
