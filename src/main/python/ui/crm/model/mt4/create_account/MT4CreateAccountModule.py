from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging


class MT4CreateAccountModule(CRMBasePage):

    def create_account(self, server, currency, group, leverage):
        """
        create a trading account
        :param server:
        :param currency:
        :param group:
        :param leverage:
        :return:
        """
        if server:
            self.select_server(server)
        if currency:
            self.select_currency(currency)
        if group:
            self.select_group(group)
        if leverage:
            self.select_leverage(leverage)
        self.click_create()
        return ClientProfilePage(self.driver)

    def create_account_with_platform(self, platform, server, currency, group, leverage):
        if platform:
            self.select_platform(platform)
        self.create_account(server, currency, group, leverage)
        return ClientProfilePage(self.driver)

    def update_account(self, trading_account, group, leverage):
        """
                create a trading account
                :param trading_account:
                :param group:
                :param leverage:
                :return:
                """
        if trading_account:
            self.select_trading_account(trading_account)
        if group:
            self.select_group(group)
        if leverage:
            self.select_leverage(leverage)
        self.click_update()
        return ClientProfilePage(self.driver)

    def select_platform(self, platform):
        drop_down = super().wait_element_to_be_clickable("//*[@id='trading_platform']", timeout=10)
        drop_down.click()
        platform_selection = self.driver.find_element(
            By.XPATH,
            "//select[@id='trading_platform']/option[contains(text(), '%s')]" % platform)
        platform_selection.click()
        Logging().reportDebugStep(self, "Platform was selected: " + platform_selection.text)
        return self

    def select_trading_account(self, trading_account):
        drop_down = self.wait_element_to_be_clickable("//select[@name='login']")
        drop_down.click()
        trading_account_selection = self.driver.find_element(By.XPATH, "//*[@id='login']/option[contains(text(), '%s')]" % trading_account)
        trading_account_selection.click()
        Logging().reportDebugStep(self, "Trading account was updated with value: %s" % trading_account_selection.text)
        return self

    def select_server(self, server):
        drop_down = self.wait_element_to_be_clickable("//select[@name='server']")
        drop_down.click()
        server_selection = self.driver.find_element(By.XPATH, "//select[@name='server']//"
                                                              "following-sibling::*[contains(.,'%s')]" % server)
        server_selection.click()
        Logging().reportDebugStep(self, "Trading account server was selected: " + server_selection.text)
        return self

    def select_currency(self, currency):
        drop_down = self.wait_element_to_be_clickable("//select[@name='currency']")
        drop_down.click()
        currency_selection = self.driver.find_element(By.XPATH, "//select[@name='currency']//"
                                                                "following-sibling::*[contains(.,'%s')]" % currency)
        currency_selection.click()
        Logging().reportDebugStep(self, "Trading account currency was selected: " + currency_selection.text)
        return self

    def select_group(self, group):
        drop_down = self.wait_element_to_be_clickable("//select[@name='group']")
        drop_down.click()
        group_selection = self.driver.find_element(By.XPATH, "//select[@name='group']//"
                                                             "*[contains(.,'%s')]" % group)
        #"//select[@name='group']//following-sibling::*[contains(.,'%s')]"
        group_selection.click()
        Logging().reportDebugStep(self, "Trading account group was selected: " + group_selection.text)
        return self

    def select_leverage(self, leverage):
        drop_down = self.wait_element_to_be_clickable("//select[@name='leverage']")
        drop_down.click()
        leverage_selection = self.driver.find_element(By.XPATH, "//select[@name='leverage']//"
                                                                "following-sibling::*[contains(.,'%s')]" % leverage)
        leverage_selection.click()
        Logging().reportDebugStep(self, "Trading account leverage was selected: " + leverage_selection.text)
        return self

    def click_create(self):
        button = self.wait_load_element("//button[contains(., 'Create')]")
        button.click()
        Logging().reportDebugStep(self, "The Create button was clicked")

    def click_update(self):
        button = self.wait_load_element("//button[contains(., 'Save')]")
        button.click()
        Logging().reportDebugStep(self, "The Save button was clicked")
