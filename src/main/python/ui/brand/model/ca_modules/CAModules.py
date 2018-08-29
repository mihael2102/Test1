from selenium.webdriver.common.by import By

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.client_area_modules.verification_center.CaVerificationCenter import \
    CaVerificationCenter
from src.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawFirstStepRequest import \
    CaWithdrawFirstStepRequest
from src.main.python.utils.waitting_utils.JSWaiter import JSWaiter


class CAModules(BrandBasePage):

    def __init__(self):
        super().__init__()

    def switch_first_tab_page(self):
        super().switch_first_tab_page()
        return CAModules()

    def open_withdraw_page(self):
        # Check that JS script for angular is working
        JSWaiter().wait_for_angular_load(self.driver)
        withdraw_page = super().wait_element_to_be_clickable("//a[@href='#/clientArea/withdraw']")
        withdraw_page.click()
        return CaWithdrawFirstStepRequest()

    def open_verification_center_page(self):
        verification__page = super().wait_element_to_be_clickable("//a[@href='#/clientArea/verification']")
        verification__page.click()
        return CaVerificationCenter()
