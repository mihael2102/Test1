from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import time

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
        self.click_update() #for_old_forex
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
        time.sleep(5)
        drop_down = self.wait_element_to_be_clickable("//select[@name='mtUserSelect']")
        # drop_down.click()
        self.driver.execute_script("arguments[0].click();", drop_down)
        server_selection = self.driver.find_element(By.XPATH,
                                                    "//select[@name='mtUserSelect']/option[contains(text(),'%s')]" % trading_account)
        # server_selection.click()
        self.driver.execute_script("arguments[0].click();", server_selection)
        Logging().reportDebugStep(self, "Trading account server was selected: " + server_selection.text)
        return self

    def select_server(self, server):
        #for_old_forex
        drop_down = self.wait_element_to_be_clickable("//select[@name='mtUserSelect']")
        drop_down.click()
        server_selection = self.driver.find_element(By.XPATH, "//select[@name='mtUserSelect']/option[contains(text(),'%s')]" % server)
        server_selection.click()
        Logging().reportDebugStep(self, "Trading account server was selected: " + server_selection.text)
        return self

    def select_currency(self, currency):
        # for_old_forex
        drop_down = self.wait_element_to_be_clickable("//select[@name='tacurrency']")
        drop_down.click()
        currency_selection = self.driver.find_element(By.XPATH, "//select[@name='tacurrency']/option[contains(text(),'%s')]" % currency)
        currency_selection.click()
        Logging().reportDebugStep(self, "Trading account currency was selected: " + currency_selection.text)
        return self

    def select_group(self, group):
        # for_old_forex
        time.sleep(5)
        drop_down = self.wait_element_to_be_clickable("//select[@name='mtGroupSelect']")
        drop_down.click()
        # self.driver.execute_script("arguments[0].click();", drop_down)
        group_selection = self.driver.find_element(By.XPATH, "//select[@name='mtGroupSelect']/option[contains(text(),'%s')]" % group)
        #"//select[@name='group']//following-sibling::*[contains(.,'%s')]"
        group_selection.click()
        # self.driver.execute_script("arguments[0].click();", group_selection)
        Logging().reportDebugStep(self, "Trading account group was selected: " + group_selection.text)
        return self

    def select_leverage(self, leverage):
        # for_old_forex
        drop_down = self.wait_element_to_be_clickable("//select[@name='leverage']")
        self.driver.execute_script("arguments[0].click();", drop_down)
        # drop_down.click()
        leverage_selection = self.driver.find_element(By.XPATH, "//select[@name='leverage']/option[contains(text(),'%s')]" % leverage)
        # leverage_selection.click()
        self.driver.execute_script("arguments[0].click();", leverage_selection)
        Logging().reportDebugStep(self, "Trading account leverage was selected: " + leverage_selection.text)
        return self

    def click_create(self):
        button = self.wait_load_element("//button[contains(., 'Create')]")
        button.click()
        Logging().reportDebugStep(self, "The Create button was clicked")

    def click_update(self):
        button = self.wait_load_element("//button[contains(., 'Save')]")
        # button.click()
        self.driver.execute_script("arguments[0].click();", button)
        Logging().reportDebugStep(self, "The Save button was clicked")
