from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

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
        data = self.driver.find_element_by_xpath("//span[@class='frx-currentvalue-pandats ng-star-inserted'] \
                                                    [contains(text(), '%s')]" % currency)
        self.driver.execute_script("arguments[0].click();", data)
        Logging().reportDebugStep(self, "Select currency : " + currency)
        return CAPage(self.driver)

    def select_leverage_level(self, leverage_level):
        data = self.driver.find_element_by_xpath("//span[@class='itemLabel'] \
                                                    [contains(text(), '%s')]" % leverage_level)
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
            Logging().reportDebugStep(self, "Additional account was not created")
        else:
            Logging().reportDebugStep(self, "Additional account was created successfully")
        # i = 0
        #
        # for elem in accounts:
        #     link = elem.get_attribute("href")
        #     if 'trading-platform' in link:
        #         i += 1
        # if i > 1:
        #     Logging().reportDebugStep(self, "You are on the Webtrader page")
        # else:
        #     Logging().reportDebugStep(self, "You are not on the Webtrader page")

        return CAPage(self.driver)