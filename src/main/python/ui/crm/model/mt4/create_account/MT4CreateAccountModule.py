from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support.select import Select
from time import sleep


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
            try:
                self.select_leverage(leverage)
            except:
                Logging().reportDebugStep(self, "No option select leverage")
        self.click_create()
        return ClientProfilePage(self.driver)

    def create_account_new_ui(self, server=None, currency=None, group=None, leverage=None):
        if server:
            self.select_server_new_ui(server)
        if currency:
            self.select_currency_new_ui(currency)
        if group:
            try:
                self.select_group_new_ui(group)
            except:
                Logging().reportDebugStep(self, "No option select group")
        if leverage:
            try:
                self.select_leverage_new_ui(leverage)
            except:
                Logging().reportDebugStep(self, "No option select leverage")
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
        Logging().reportDebugStep(self, "Trading account server was selected: " + server)
        return self

    def select_server_new_ui(self, server):
        sleep(0.2)
        server_item = super().wait_load_element("//span[contains(text(),'%s')]" % server)
        self.driver.execute_script("arguments[0].click();", server_item)
        Logging().reportDebugStep(self, "Trading account server was selected: " + server)
        return self

    def select_currency(self, currency):
        drop_down = self.wait_element_to_be_clickable("//select[@name='currency']")
        drop_down.click()
        currency_selection = self.driver.find_element(By.XPATH, "//select[@name='currency']//"
                                                                "following-sibling::*[contains(.,'%s')]" % currency)
        currency_selection.click()
        Logging().reportDebugStep(self, "Trading account currency was selected: " + currency)
        return self

    def select_currency_new_ui(self, currency):
        sleep(0.2)
        currency_item = super().wait_load_element("//span[text()='%s']" % currency)
        self.driver.execute_script("arguments[0].click();", currency_item)
        Logging().reportDebugStep(self, "Trading account currency was selected: " + currency)
        return self

    def select_group(self, group):
        drop_down = self.wait_element_to_be_clickable("//select[@name='group']", timeout=5)
        drop_down.click()
        group_selection = self.driver.find_element(By.XPATH, "//select[@name='group']//"
                                                             "*[contains(.,'%s')]" % group)
        group_selection.click()
        Logging().reportDebugStep(self, "Trading account group was selected: " + group)
        return self

    def select_group_new_ui(self, group):
        group_item = super().wait_load_element(
            "//mt-user-create/div[2]/form/div[2]/div[1]/nice-select/div/div/ul/li/a/span[contains(text(),'%s')]"
            % group)
        self.driver.execute_script("arguments[0].click();", group_item)
        Logging().reportDebugStep(self, "Trading account group was selected: " + group)
        return self

    def select_leverage(self, leverage):
        try:
            super().wait_load_element("//select[@id='leverage' and @aria-required='true']", timeout=15)
            Logging().reportDebugStep(self, "Leverage can't be selected: readonly")
            return self
        except:
            drop_down = self.wait_element_to_be_clickable("//select[@name='leverage']", timeout=5)
            drop_down.click()
            leverage_selection = self.driver.find_element(By.XPATH, "//select[@name='leverage']//"
                                                                    "following-sibling::*[contains(.,'%s')]" % leverage)
            leverage_selection.click()
            Logging().reportDebugStep(self, "Trading account leverage was selected: " + leverage)
            return self

    def select_leverage_new_ui(self, leverage):
        sleep(0.2)
        leverage_item = super().wait_load_element("//span[contains(text(),'%s')]" % leverage)
        self.driver.execute_script("arguments[0].click();", leverage_item)
        Logging().reportDebugStep(self, "Trading account leverage was selected: " + leverage)
        return self

    '''
        Second method for set leverage because of previous method can't be used for selecting 1:30 leverage
        Please, choose this method for every new test!
    '''
    def set_leverage(self, leverage):
        leverage_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leverage']"))
        leverage_list.select_by_visible_text(leverage)
        Logging().reportDebugStep(self, "Trading account leverage was selected: " + leverage)
        return MT4CreateAccountModule(self.driver)

    def click_create(self):
        sleep(1)
        button = self.wait_element_to_be_clickable("//button[contains(., 'Create')]")
        button.click()
        Logging().reportDebugStep(self, "The Create button was clicked")

    def click_update(self):
        button = self.wait_load_element("//button[contains(., 'Save')]")
        button.click()
        Logging().reportDebugStep(self, "The Save button was clicked")

    '''
        Check, that server is not available for account opening 
    '''

    def verify_server_not_available(self, server):
        server_pick_list = super().wait_load_element("//select[@id='server']").text
        assert server not in server_pick_list.upper()
        Logging().reportDebugStep(self, server + " server is not available for accounts opening")
        return MT4CreateAccountModule(self.driver)

    '''
        Check, that group is not available
    '''
    def verify_group_not_available(self, group):
        group_pick_list = super().wait_load_element("//select[@name='group']").text
        assert group.upper() not in group_pick_list.upper()
        Logging().reportDebugStep(self, group + " group is not available")
        return MT4CreateAccountModule(self.driver)

    def verify_leverage_not_available(self, leverage):
        leverage_visibility = super().wait_load_element("//select[@id='leverage']/option[@value='%s']" % leverage)\
            .get_attribute("data-live")
        if '0' in leverage_visibility:
            assert '0' in leverage_visibility
            Logging().reportDebugStep(self, 'Leverage ' + leverage + " is not available")
        elif '1' in leverage_visibility:
            Logging().reportDebugStep(self, 'Warning: Leverage ' + leverage + " is available")
            assert '0' in leverage_visibility
        return MT4CreateAccountModule(self.driver)

    def verify_leverage_available(self, leverage):
        leverage_visibility = super().wait_load_element("//select[@id='leverage']/option[@value='%s']" % leverage)\
            .get_attribute("data-live")
        if '1' in leverage_visibility:
            assert '1' in leverage_visibility
            Logging().reportDebugStep(self, 'Leverage ' + leverage + " is available")
        elif '0' in leverage_visibility:
            Logging().reportDebugStep(self, 'Warning: Leverage ' + leverage + " is not available")
            assert '1' in leverage_visibility
        return MT4CreateAccountModule(self.driver)

    def verify_success_message(self):
        message = super().wait_load_element("//div[@class='dialog-content-success mat-dialog-content']").text
        assert "success" in message.lower()
        Logging().reportDebugStep(self, "Get message: " + message)
        return MT4CreateAccountModule(self.driver)
