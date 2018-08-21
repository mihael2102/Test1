from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class BrandTradingExperienceForm(BrandBasePage):

    def __init__(self):
        super().__init__()
        super().wait_load_element_present("//custom-select[@name='tradingFrequency']")

    def select_trading_frequency(self, trading_frequency):
        drop_down_trading_frequency = self.driver.find_element(By.XPATH, "//custom-select[@name='tradingFrequency']")
        drop_down_trading_frequency.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'tradingFrequency']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % trading_frequency)
        select.click()
        Logging().reportDebugStep(self, "The trading_frequency was set: " + trading_frequency)
        return BrandTradingExperienceForm()

    def select_cfd_trading(self, cfd_trading):
        drop_down_cfd_trading = self.driver.find_element(By.XPATH, "//custom-select[@name='cfdTrading']")
        drop_down_cfd_trading.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'cfdTrading']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % cfd_trading)
        select.click()
        Logging().reportDebugStep(self, "The cfd trading was set: " + cfd_trading)
        return BrandTradingExperienceForm()

    def select_otcd_frequency(self, otcd_frequency):
        drop_down_otcd_frequency = self.driver.find_element(By.XPATH, "//custom-select[@name='otcdFrequency']")
        drop_down_otcd_frequency.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'otcdFrequency']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % otcd_frequency)
        select.click()
        Logging().reportDebugStep(self, "The otcd_frequency was set: " + otcd_frequency)
        return BrandTradingExperienceForm()

    def select_etd_frequency(self, etd_frequency):
        drop_down_etd_frequency = self.driver.find_element(By.XPATH, "//custom-select[@name='etdFrequency']")
        drop_down_etd_frequency.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'etdFrequency']//"
                                                    "following-sibling::*//*[contains(text(),'%s')]" % etd_frequency)
        select.click()
        Logging().reportDebugStep(self, "The etd frequency was set: " + etd_frequency)
        return BrandTradingExperienceForm()

    def select_us_citizen(self, us_citizen):
        drop_down_etd_frequency = self.driver.find_element(By.XPATH, "//custom-select[@name='usCitizen']")
        drop_down_etd_frequency.click()
        select = self.driver.find_element(By.XPATH, "//custom-select[@name= 'usCitizen']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % us_citizen)
        select.click()
        Logging().reportDebugStep(self, "The eus_citizen was set: " + us_citizen)
        return BrandTradingExperienceForm()

    def set_us_taxid(self, us_taxid):
        field_us_taxid = self.driver.find_element(By.XPATH, "//input[@name='ustaxid']")
        field_us_taxid.clear()
        field_us_taxid.send_keys(us_taxid)
        Logging().reportDebugStep(self, "The us_taxid was set: " + us_taxid)
        return BrandTradingExperienceForm()

    def enter_finish_button(self):
        next_button = self.driver.find_element(By.XPATH, "//div[@class='next-pandats']")
        next_button.click()
        Logging().reportDebugStep(self, "Next button was clicked")
        return BrandTradingExperienceForm()
