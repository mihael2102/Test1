from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.ca_modules.CAModules import CAModules
from src.main.python.ui.brand.model.forms.create_personal_profile.BrandCreatePersonalProfileForm import \
    BrandCreatePersonalProfileForm
from src.main.python.utils.logs.Loging import Logging


class BrandTradingPlatformPageBrand(BrandBasePage):

    def __init__(self):
        super().__init__()

    ''' 
         Open the demo drop down to create a live account for 2st step 
    '''

    def open_demo_drop_down(self, value):
        demo_drop_down = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='button-pandats account-pandats']")))

        demo_drop_down.click()
        Logging().reportDebugStep(self, "Click the drop down")
        select = self.driver.find_element(By.XPATH, "//div[@class='account-actions-pandats']//"
                                                    "following-sibling::"
                                                    "button[contains(text(),'%s')]" % value)
        select.click()
        Logging().reportDebugStep(self, "Select the module")
        return BrandCreatePersonalProfileForm()

    ''' 
        Open the drop down menu 
    '''

    def open_drop_down_menu(self):
        super().open_drop_down_menu()
        Logging().reportDebugStep(self, "Open the drop down menu")
        return BrandTradingPlatformPageBrand()

    ''' 
        Select the module 
        :parameter module 
    '''

    def select_module(self, module):
        super().select_module(module)
        select_module = "Select the drop menu: " + module + " module"
        Logging().reportDebugStep(self, select_module)
        return CAModules()
