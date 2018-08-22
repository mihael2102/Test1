from time import sleep

from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class CASuccessFailedDeposit(BrandBasePage):

    def __init__(self):
        super().__init__()

    def get_successful_deposit_message(self):
        message_element = super().wait_load_element_present("//div[@class='body-pandats']//h1")
        Logging().reportDebugStep(self, "Returns the successful deposit message: " + message_element.text)
        return message_element.text

    def get_failed_deposit_message(self):
        message_element = super().wait_load_element_present("//*[@id='Top_bar']/div[1]/div/div[1]/div[2]/ul/li[6]/panda-forex-deposit-credit/div/div/credit-card/div/div[2]/toast/div/div[1]")
        contains_text = False
        i = 5
        sleep(0.3)      # Wait message to display
        while not contains_text or (i == 5):
            message_text = message_element.text
            if message_text != "":
                Logging().reportDebugStep(self, "Returns the failed deposit message: " + message_element.text)
                return message_text
            sleep(0.2)
            Logging().reportDebugStep(self, "Trying to get transaction operation message again.")
            message_element = super().driver.find_element(By, "//*[@id='Top_bar']/div[1]/div/div[1]/div[2]/ul/li[6]/panda-forex-deposit-credit/div/div/credit-card/div/div[2]/toast/div/div[1]")
        Logging().reportDebugStep(self, "Transaction operation message cannot be read from UI")
        return message_text


    def get_amount_text(self):
        amount_element = self.driver.find_element(By.XPATH, "//span[contains(@class, 'amount-pandats')]")
        Logging().reportDebugStep(self, "In deposit popup the amount is:" + amount_element.text)
        return amount_element.text
