from selenium.webdriver.common.by import By

from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from scr.main.python.ui.brand.model.client_area_modules.verification_center.CaVerificationCenter import \
    CaVerificationCenter
from scr.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawFirstStepRequest import \
    CaWithdrawFirstStepRequest


class CAModules(BrandBasePage):

    def __init__(self):
        super().__init__()

    def switch_first_tab_page(self):
        super().switch_first_tab_page()
        return CAModules()

    def open_withdraw_page(self):
        withdraw_page = self.driver.find_element(By.XPATH, "//a[@href='#/clientArea/withdraw']")
        withdraw_page.click()
        return CaWithdrawFirstStepRequest()


    def open_verification_center_page(self):
        withdraw_page = self.driver.find_element(By.XPATH, "//a[@href='#/clientArea/withdraw']")
        withdraw_page.click()
        return CaVerificationCenter()

