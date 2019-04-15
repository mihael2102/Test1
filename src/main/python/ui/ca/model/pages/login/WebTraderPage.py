from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class WebTraderPage(CRMBasePage):

    def select_asset(self):
        forex = self.driver.find_element(By.XPATH,"//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/perfect-scrollbar/div[1]/ul/li[2]/div/span")
        forex.click()
        crypto = self.driver.find_element(By.XPATH,"//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/perfect-scrollbar/div[1]/ul/li[3]/div/span")
        crypto.click()
        sleep(5)
        click_select_account = self.driver.find_element(By.XPATH,"//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/perfect-scrollbar/div[1]/ul/li[3]/ul/li[2]/asset-item/div/div[2][contains(text(), 'BTCUSD')]")
        click_select_account.click()
        Logging().reportDebugStep(self, "Click select account")
        return WebTraderPage(self.driver)


    def click_buy(self):
        sleep(3)
        btn_deposit = self.driver.find_element(By.XPATH,
                                               "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/div[3]/div[2]")
        btn_deposit.click()
        Logging().reportDebugStep(self, "Choose a different asset from the list to the left")
        return WebTraderPage(self.driver)

    def choose_asset(self):
        forex = self.driver.find_element(By.XPATH,
                                         "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/perfect-scrollbar/div[1]/ul/li[2]/div/span")
        forex.click()
        crypto = self.driver.find_element(By.XPATH,
                                          "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/perfect-scrollbar/div[1]/ul/li[3]/div/span")
        crypto.click()
        sleep(5)
        click_select_account = self.driver.find_element(By.XPATH,
                                                        "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/perfect-scrollbar/div[1]/ul/li[3]/ul/li[2]/asset-item/div/div[2][contains(text(), 'BTCUSD')]")
        click_select_account.click()
        # sleep(3)
        # btn_deposit = self.driver.find_element(By.XPATH,"//*[@id='Content']/div/div/div/div[1]/div/div/div/div/div/div/div[2]/panda-forex-trading-platform/div/div/div/div[1]/asset-list/div/div[2]/perfect-scrollbar/div/div[1]/ul/li[2]/ul/li[25]/asset-item/div/div[2][contains(text(), 'BTCGBP.m')]")
        # btn_deposit.click()
        # self.driver.execute_script("arguments[0].scrollIntoView();", btn_deposit)
        # try:
        #     btn_deposit.click()
        # except:
        #     self.driver.execute_script("arguments[0].click();", btn_deposit)
        Logging().reportDebugStep(self, "Choose a different asset from the list to the left")
        return WebTraderPage(self.driver)

    def get_number_account(self):
        sleep(3)
        succsessfull_order = self.driver.find_element(By.XPATH, "//*[@id='header']/div[1]/panda-forex-accounts/div/div[1]/div[2]/span[2]").text
        Logging().reportDebugStep(self, "Get account number" + succsessfull_order)
        return succsessfull_order

    def click_deposit(self):
        sleep(10)
        btn_deposit = self.driver.find_element(By.XPATH, "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/div[6]/div[2]/button")
        btn_deposit.click()
        Logging().reportDebugStep(self, "Click Deposit")
        return WebTraderPage(self.driver)

    def get_msg_succsessfull_order(self):
        sleep(1)
        succsessfull_order = self.driver.find_element(By.XPATH, "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/popup/div/div[1]/h2").text
        Logging().reportDebugStep(self, "Check message")
        return succsessfull_order

    def select_volume_in_lot(self):
        sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        sleep(3)
        select_volume = self.driver.find_element(By.XPATH, "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/div[1]/div[2]/input")
        select_volume.send_keys("2")
        Logging().reportDebugStep(self, "Select volume in lot")
        return WebTraderPage(self.driver)

    def click_sell(self):
        sleep(2)
        sell = self.driver.find_element(By.XPATH,
                                                 "//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/div[3]/div[1]")
        sell.click()
        Logging().reportDebugStep(self, "Click SELL")
        return WebTraderPage(self.driver)

    def click_invest(self):
        sleep(2)
        invest = self.driver.find_element(By.XPATH,"//*[@id='platform']/panda-forex-trading-platform/div/div/div/div[2]/div[1]/div[2]/div/invest/perfect-scrollbar/div[1]/form/div[5]/button")
        invest.click()
        Logging().reportDebugStep(self, "Click Invest")
        return WebTraderPage(self.driver)

    def check_avaliable_funds(self):
        avaliable_funds = self.driver.find_element_by_xpath("//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[1]/div[1]").text
        Logging().reportDebugStep(self, "Check avaliable funds")
        return avaliable_funds

    def check_used_funds(self):
        used_funds = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[2]/div[1]").text
        Logging().reportDebugStep(self, "Check used funds")
        return used_funds

    def check_account_value(self):
        account_value = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[3]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return account_value

    def check_total_p_l(self):
        total_p_l = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[4]/div[1]").text
        Logging().reportDebugStep(self, "Check account value")
        return total_p_l

    def check_margin_level(self):
        margin_level = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[5]/div[1]").text
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
        avaliable_funds = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[1]/div[2]").text
        Logging().reportDebugStep(self, "Check avaliable funds" + avaliable_funds)
        return avaliable_funds

    def check_used_funds_number(self):
        used_funds = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[2]/div[2]").text
        Logging().reportDebugStep(self, "Check used funds" + used_funds)
        return used_funds

    def check_account_value_number(self):
        account_value = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[3]/div[2]").text
        Logging().reportDebugStep(self, "Check account value" + account_value)
        return account_value

    def check_total_p_l_number(self):
        total_p_l = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[4]/div[2]").text
        Logging().reportDebugStep(self, "Check account value" + total_p_l)
        return total_p_l

    def check_margin_level_number(self):
        margin_level = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/panda-forex-account-status/div/ul/li[5]/div[2]").text
        Logging().reportDebugStep(self, "Check account value" + margin_level)
        return margin_level
