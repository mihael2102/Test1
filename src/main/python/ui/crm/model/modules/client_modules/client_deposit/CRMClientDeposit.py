from time import sleep

from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CRMClientDeposit(CRMBasePage):

    def select_payment_method(self, payment_method):
        sleep(10)
        super().wait_visible_of_element("//div[@id='popupcontent']//iframe")
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//div[@id='popupcontent']//iframe"))
        method = super().wait_load_element("//perfect-scrollbar/div/div[1]/div/div[%s]/div" % payment_method)
        method.click()
        sleep(14)
        super().wait_visible_of_element("//*[@id='depositFrame']")
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//*[@id='depositFrame']"))
        credit_card_type = super().wait_element_to_be_clickable("//*[@id='depositoptions']/div[1]/a[2]")
        credit_card_type.click()
        Logging().reportDebugStep(self, "The payment method was set:" + payment_method)
        return CRMClientDeposit(self.driver)

    def set_amount_deposit(self, amount):
        amount_element = super().wait_element_to_be_clickable("//div[@class='formrow']//input[@name='convertedamount']")
        amount_element.clear()
        amount_element.send_keys(amount)
        Logging().reportDebugStep(self, "The amount  was set:" + amount)
        return CRMClientDeposit(self.driver)

    def click_deposit_button(self):
        deposit_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        deposit_button.click()
        Logging().reportDebugStep(self, "Click the deposit button")
        return CRMClientDeposit(self.driver)

    def set_card_number(self, card_number):
        card_number_element = super().wait_load_element("//div[@class='formrow']//input[@name='cardnumber']")
        card_number_element.clear()
        card_number_element.send_keys(card_number)
        Logging().reportDebugStep(self, "The card number  was set:" + card_number)
        return CRMClientDeposit(self.driver)

    def set_expiry_date(self, expiry_date):
        expiry_date_element = self.driver.find_element(By.XPATH, "//input[@name='cardexp']")
        expiry_date_element.clear()
        expiry_date_element.send_keys(expiry_date)
        Logging().reportDebugStep(self, "The expiry date was set:" + expiry_date)
        return CRMClientDeposit(self.driver)

    def set_expiry_year(self, expiry_year):
        sleep(1)
        expiry_year_element = self.driver.find_element(By.XPATH, "//input[@name='cardexp']")
        expiry_year_element.clear()
        expiry_year_element.send_keys(expiry_year)
        Logging().reportDebugStep(self, "The expiry year was set:" + expiry_year)
        return CRMClientDeposit(self.driver)

    def set_cvc(self, cvc_number):
        cvc_element = self.driver.find_element(By.XPATH, "//input[@name='CVV']")
        cvc_element.clear()
        cvc_element.send_keys(cvc_number)
        Logging().reportDebugStep(self, "The cvc number was set:" + cvc_number)
        return CRMClientDeposit(self.driver)

    def perform_deposit(self):
        deposit_button = self.driver.find_element(By.XPATH, "//div[@class='formarea']//input[@name='SubmitBtn']")
        deposit_button.click()
        Logging().reportDebugStep(self, "Perform the deposit")
        return CRMClientDeposit(self.driver)

    def get_successful_deposit_message(self):
        sleep(7)
        message_element = super().wait_visible_of_element("//main/div[2]/div[1]")
        Logging().reportDebugStep(self, "Returns the successful deposit message: " + message_element.text)
        return message_element.text