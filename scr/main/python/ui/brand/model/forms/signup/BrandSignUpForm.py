from selenium.webdriver.common.by import By

from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from scr.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPageBrand
from scr.main.python.utils.screenshot.ScreenShot import ScreenShot


class BrandSignUpForm(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_email(self, email):
        self.email_locator = self.driver.find_element(By.XPATH, "//input[@name='email']")
        self.email_locator.clear()
        self.email_locator.send_keys(email)
        return BrandSignUpForm()

    def set_password(self, password):
        self.password_locator = self.driver.find_element(By.XPATH, "//*[@name='password']")
        self.password_locator.clear()
        self.password_locator.send_keys(password)
        return BrandSignUpForm()

    def set_confirm_password(self, confirm_password):
        self.confirmLocator = self.driver.find_element(By.XPATH, "//*[@name='passwordConfirm']")
        self.confirmLocator.clear()
        self.confirmLocator.send_keys(confirm_password)
        return BrandSignUpForm()

    def set_promo_code(self, promo_code):
        self.promo_code_locator = self.driver.find_element(By.XPATH, "//*[@placeholder='Enter Promocode']")
        self.promo_code_locator.clear()
        self.promo_code_locator.send_keys(promo_code)
        return BrandSignUpForm()

    def set_country(self, country):
        self.change_country_locator = self.driver.find_element(By.XPATH,
                                                               "//div[@class='country-pandats']//following-sibling::a")
        self.change_country_locator.click()
        self.exist_counter_locator = self.driver.find_element(By.XPATH, "//div[@class='content-pandats']//ul")
        self.search_locator = self.driver.find_element(By.XPATH,
                                                       "//div[@class='search-pandats']//following-sibling::input")

        self.search_locator.send_keys(country)
        self.exist_counter_locator.click()
        return BrandSignUpForm()

    def set_check_box(self):
        self.checkBoxLocator = self.driver.find_element(By.XPATH, "//label[@class='terms-pandats']")
        screen_path = "/"
        screen = ScreenShot(self.driver)
        if self.checkBoxLocator.is_displayed():
            self.checkBoxLocator.click()
        screen.PerfomScreenShot(screen_path + "NewForexSignForm.png")
        return BrandSignUpForm()

    def sign_up_button(self):
        self.submitLocator = self.driver.find_element(By.XPATH,
                                                      "//button[@class='forex-button-pandats signup-button-pandats']")
        screen_path = "/"
        screen = ScreenShot(self.driver)
        self.submitLocator.click()
        screen.PerfomScreenShot(screen_path + "ForexTradingPlatformPage.png")
        return BrandTradingPlatformPageBrand()
