from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage

class WebTraderPage(CRMBasePage):

    def ptbanc_webtrader(self):
        CALoginPage(self.driver).open_first_tab_page("https://ptbanc.com/trading.html#/")

        Logging().reportDebugStep(self, "Click TRADING")
        return WebTraderPage(self.driver)

    def select_demo_account_by_number(self, number):
        sleep(3)
        click_select_account = self.driver.find_element(By.XPATH,
                                                        "//div[contains(text(), ' #" + number +" ')]")
        try:
            click_select_account.click()
        except:
            self.driver.execute_script("arguments[0].click();", click_select_account)
        Logging().reportDebugStep(self, "Click demo account")
        return WebTraderPage(self.driver)

    def check_hight_low(self):
        sleep(3)
        check_stop_loss_in_table = self.driver.find_element(By.XPATH,
                                                            "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[2]/div[2]/sltp-popup/div/div[2]/div[1]/div[1]/span")
        Logging().reportDebugStep(self, "check hight low" + check_stop_loss_in_table.text)
        return check_stop_loss_in_table.text


    def check_stop_loss_in_table(self):
        sleep(3)
        check_stop_loss_in_table = self.driver.find_element(By.XPATH,
                                                     "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[2]/div[2]/tabs/div/div/open-trades/div/div/perfect-scrollbar/div/div[1]/div/table/tbody/tr/open-trade/td[1]")
        Logging().reportDebugStep(self, "check stop loss in table" + check_stop_loss_in_table.text)
        return check_stop_loss_in_table.text

    def click_submit_changes(self):
        sleep(3)
        click_stop_loss = self.driver.find_element(By.XPATH,
                                                   "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[2]/div[2]/sltp-popup/div/div[2]/div[3]/div/button")
        click_stop_loss.click()
        Logging().reportDebugStep(self, "click submit changes")
        return WebTraderPage(self.driver)

    def check_pips_stop_loss(self):
        sleep(3)

        pips_bottom_panel = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
                                                        self.__class__.__name__)["pips_bottom_panel_test"])
        Logging().reportDebugStep(self, "Check pip in bottom panel" + pips_bottom_panel.text)
        return pips_bottom_panel.text

    def enter_stop_loss(self, stop_loss):
        sleep(3)
        enter_stop_loss = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
                                                        self.__class__.__name__)["enter_stop_loss"])
        enter_stop_loss.clear()
        enter_stop_loss.send_keys(stop_loss)
        Logging().reportDebugStep(self, "Enter stop loss")
        return WebTraderPage(self.driver)

    def click_stop_loss(self):
        sleep(3)
        click_stop_loss = self.driver.find_element(By.XPATH,global_var.get_xpath_for_current_brand_element(
                                                        self.__class__.__name__)["click_stop_loss"])
        click_stop_loss.click()
        Logging().reportDebugStep(self, "Click stop loss")
        return WebTraderPage(self.driver)

    def check_button_set_stop_loss(self):
        sleep(3)
        check_button = self.driver.find_element(By.XPATH,
                                               "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[2]/div[2]/sltp-popup/div/div[2]/div[2]/div[3]/div[1]/label")
        check_button.click()
        Logging().reportDebugStep(self, "Check button set stop loss")
        return WebTraderPage(self.driver)

    def check_pips_bottom_panel(self):
        sleep(3)
        pips_bottom_panel = self.driver.find_element(By.XPATH,
                                                     global_var.get_xpath_for_current_brand_element(
                                                         self.__class__.__name__)["pips_bottom_panel"])
        Logging().reportDebugStep(self, "Check pip in bottom panel" + pips_bottom_panel.text)
        return pips_bottom_panel.text

    def check_pips_right_panel(self):
        sleep(3)
        pips_right_panel = self.driver.find_element(By.XPATH,
                                                    global_var.get_xpath_for_current_brand_element(
                                                        self.__class__.__name__)["pips_right_panel"])
        Logging().reportDebugStep(self, "Check pip in right panel" + pips_right_panel.text)
        return pips_right_panel.text

    def select_asset(self):
        sleep(15)
        if global_var.current_brand_name == "ptbanc":
            click_select_account = self.driver.find_element(By.XPATH,
                                                            "//panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[2]/div/span")
            click_select_account.click()
            crypto = self.driver.find_element(By.XPATH, "//panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[3]/div/span")
            crypto.click()
            sleep(2)
            asset = self.driver.find_element(By.XPATH,"//panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[3]/ul/li[39]/asset-item/div/div[2]")
            self.driver.execute_script("arguments[0].scrollIntoView();", asset)
            try:
                asset.click()
            except:
                self.driver.execute_script("arguments[0].click();", asset)
        else:
            try:
                sleep(8)
                click_select_account = self.driver.find_element(By.XPATH,
                                                                "//panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[2]/ul/li[7]/asset-item/div/div[2][contains(text(), 'BTCUSD.m')]")
                click_select_account.click()
            except:
                self.refresh_page()
                sleep(7)
                click_select_account = self.driver.find_element(By.XPATH,
                                                                "//panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[2]/ul/li[7]/asset-item/div/div[2][contains(text(), 'BTCUSD.m')]")
                click_select_account.click()
        Logging().reportDebugStep(self, "Click select account")
        return WebTraderPage(self.driver)

    def click_select_account(self):
        sleep(5)
        if global_var.current_brand_name == "ptbanc":
            click_select_account = self.driver.find_element(By.XPATH,
                                                   "//*[@id='u33171']/panda-forex-accounts/div/div/i[2]")

        elif global_var.current_brand_name == "brokerz":
            click_select_account = self.driver.find_element(By.XPATH,
                                                            "//*[@id='panda-buttons']/panda-forex-accounts/div/div/i[2]")

        else:
            click_select_account = self.driver.find_element(By.XPATH,
                                                            "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-accounts/div/div/i[2]")

        click_select_account.click()
        Logging().reportDebugStep(self, "Click select account")
        return WebTraderPage(self.driver)

    def select_demo_account(self):
        sleep(8)
        if global_var.current_brand_name == "ptbanc":
            click_select_account = self.driver.find_element(By.XPATH,
                                                            "//*[@id='u33171']/panda-forex-accounts/div/div/div/perfect-scrollbar/div/div[1]/div/ul/li[3]/div/div[3]/span")
        elif global_var.current_brand_name == "brokerz":
            click_select_account = self.driver.find_element(By.XPATH,
                                                            "//*[@id='panda-buttons']/panda-forex-accounts/div/div/div/perfect-scrollbar/div/div[1]/div/ul/li[2]/div/div[3]/span[contains(text(), 'Demo')]")

        else:
            click_select_account = self.driver.find_element(By.XPATH,
                                                            "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-accounts/div/div/div/perfect-scrollbar/div/div[1]/div/ul/li[3]/div/div[3]/span")

        try:
            click_select_account.click()
        except:
            self.driver.execute_script("arguments[0].click();", click_select_account)
        Logging().reportDebugStep(self, "Click demo account")
        return WebTraderPage(self.driver)

    def click_buy(self):
        sleep(3)
        click_buy = self.driver.find_element(By.XPATH,global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["click_buy"])
        click_buy.click()
        Logging().reportDebugStep(self, "click Buy")
        return WebTraderPage(self.driver)

    def choose_asset(self):
        sleep(3)
        if global_var.current_brand_name != "ptbanc":
            btn_deposit = self.driver.find_element(By.XPATH,
                                                   "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[2]/ul/li[25]/asset-item/div/div[2][contains(text(), 'BTCGBP.m')]")
        else:
            btn_deposit = self.driver.find_element(By.XPATH, "//*[@id='u8983']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[3]/ul/li[39]/asset-item/div/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", btn_deposit)
        try:
            btn_deposit.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn_deposit)
        Logging().reportDebugStep(self, "Choose a different asset from the list to the left")
        return WebTraderPage(self.driver)

    def get_number_account(self):
        if global_var.current_brand_name != "ptbanc":
            demo = self.driver.find_element(By.XPATH, "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-accounts/div/div/i[2]")
            try:
                demo.click()
            except:
                self.driver.execute_script("arguments[0].click();", demo)
            sleep(3)
            succsessfull_order = self.driver.find_element(By.XPATH, "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-accounts/div/div/div/ul/li/div/div[1]/div/div[2]").text
            succsessfull_order1 = succsessfull_order.replace(' #', '')
            succsessfull_order2 = succsessfull_order1.replace(' - ', '')
            Logging().reportDebugStep(self, "Get account number" + succsessfull_order2)
        else:
            sleep(10)
            demo = self.driver.find_element(By.XPATH,
                                            "//panda-forex-accounts/div/div/i[2]")
            try:
                demo.click()
            except:
                self.driver.execute_script("arguments[0].click();", demo)
            sleep(3)
            succsessfull_order = self.driver.find_element(By.XPATH,
                                                          "//panda-forex-accounts/div/div/div/ul/li/div/div[1]/div/div[2]").text
            succsessfull_order1 = succsessfull_order.replace(' #', '')
            succsessfull_order2 = succsessfull_order1.replace(' - ', '')
            Logging().reportDebugStep(self, "Get account number" + succsessfull_order2)

        return succsessfull_order2

    def click_deposit(self):
        sleep(10)
        btn_deposit = self.driver.find_element(By.XPATH, "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/div[6]/div[2]/button")
        btn_deposit.click()
        Logging().reportDebugStep(self, "Click Deposit")
        return WebTraderPage(self.driver)

    def get_msg_succsessfull_order(self):
        sleep(1)
        if global_var.current_brand_name != "ptbanc":
            succsessfull_order = self.driver.find_element(By.XPATH, "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/popup/div/div[1]/h2").text
        else:
            succsessfull_order = self.driver.find_element(By.XPATH, "//*[@id='u8983']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/popup/div/div[1]/h2").text

        Logging().reportDebugStep(self, "Check message")
        return succsessfull_order

    def select_volume_in_lot(self):
        sleep(3)
        # window_after = self.driver.window_handles[1]
        # self.driver.switch_to_window(window_after)
        sleep(3)
        select_volume = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["volume_in_lot"])
        select_volume.clear()
        select_volume.send_keys("0.1")
        Logging().reportDebugStep(self, "Select volume in lot")
        return WebTraderPage(self.driver)

    def click_sell(self):
        sleep(2)
        sell = self.driver.find_element(By.XPATH,global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["sell"])
        sell.click()
        Logging().reportDebugStep(self, "Click SELL")
        return WebTraderPage(self.driver)

    def click_invest(self):
        sleep(2)
        invest = self.driver.find_element(By.XPATH,global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["invest"])
        invest.click()
        Logging().reportDebugStep(self, "Click Invest")
        return WebTraderPage(self.driver)

    def check_avaliable_funds(self):
        sleep(5)
        avaliable_funds = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["avaliable_funds"]).text
        Logging().reportDebugStep(self, "Check avaliable funds")
        return avaliable_funds

    def check_used_funds(self):
        used_funds = self.driver.find_element_by_xpath(
            global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["used_funds"]).text
        Logging().reportDebugStep(self, "Check used funds")
        return used_funds

    def check_account_value(self):
        account_value = self.driver.find_element_by_xpath(
            "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-account-status/div/ul/li[3]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return account_value

    def check_total_p_l(self):
        total_p_l = self.driver.find_element_by_xpath(
            "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-account-status/div/ul/li[4]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return total_p_l

    def check_margin_level(self):
        margin_level = self.driver.find_element_by_xpath(
            "//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[1]/panda-forex-account-status/div/ul/li[5]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return margin_level

    def get_avaliable_funds(self):
        sleep(5)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        # main_window = self.driver.find_element(By.XPATH, "//*[@id='main-wrapper-webtrader']")
        # self.driver.switch_to_window(main_window)
        avaliable_funds = self.driver.find_element(By.XPATH,
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[1]/div[2]").text
        Logging().reportDebugStep(self, "Check account value")
        return avaliable_funds

    def check_avaliable_funds_number(self):
        sleep(10)
        # window_after = self.driver.window_handles[1]
        # self.driver.switch_to_window(window_after)
        avaliable_funds_number = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["avaliable_funds_number"]
            ).text
        Logging().reportDebugStep(self, "Check avaliable funds" + avaliable_funds_number)
        return avaliable_funds_number

    def check_used_funds_number(self):
        used_funds_number = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["used_funds_number"]
            ).text
        Logging().reportDebugStep(self, "Check used funds" + used_funds_number)
        return used_funds_number

    def check_account_value_number(self):
        account_value_number = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["account_value_number"]
            ).text
        Logging().reportDebugStep(self, "Check account value" + account_value_number)
        return account_value_number

    def check_total_p_l_number(self):
        total_p_l_number = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["total_p_l_number"]
            ).text
        Logging().reportDebugStep(self, "Check account value" + total_p_l_number)
        return total_p_l_number

    def check_margin_level_number(self):
        margin_level_number = self.driver.find_element_by_xpath(global_var.get_xpath_for_current_brand_element(
                                                           self.__class__.__name__)["margin_level_number"]
           ).text
        Logging().reportDebugStep(self, "Check account value" + margin_level_number)
        return margin_level_number
