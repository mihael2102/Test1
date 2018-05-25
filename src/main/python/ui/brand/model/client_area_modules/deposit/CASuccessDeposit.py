from selenium.webdriver.common.by import By

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class CASuccessDeposit(BrandBasePage):

    def __init__(self):
        super().__init__()

    def get_successful_deposit_message(self):
        message_element = super().wait_load_element_present("//div[@class='body-pandats']//h1")
        return message_element.text

    def get_amount_text(self):
        amount_element = self.driver.find_element(By.XPATH, "//div[@class='transaction-amount-pandats']")
        return amount_element.text
