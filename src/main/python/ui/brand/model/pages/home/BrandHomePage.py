import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.forms.login.BrandLoginForm import BrandLoginForm
from src.main.python.ui.brand.model.forms.signup.BrandSignUpForm import BrandSignUpForm
from src.main.python.utils.logs.Loging import Logging


class BrandHomePage(BrandBasePage):

    def __init__(self):
        super().__init__()

    def open_first_tab_page(self, url):
        with allure.step("Open the first tab with the page: " + url):
            super().open_first_tab_page(url)
            Logging().reportDebugStep(self, "Open the first tab with the page: " + url)
        return BrandHomePage()

    def open_second_tab_page(self, url):
        with allure.step("Open the second tab with the page: " + url):
            super().open_second_tab_page(url)
            Logging().reportDebugStep(self, "Open the second tab with the page: " + url)
        return BrandHomePage()

    def open_sign_form(self):
        with allure.step("Open the sign form: "):
            sign_on_button_locator = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains (text(),'Sign Up')]")))
        sign_on_button_locator.click()
        Logging().reportDebugStep(self, "Open the sign form")
        return BrandSignUpForm()

    def login(self):
        with allure.step("Click the 'Login' button on Home page: "):
            login_button_locator = super().wait_load_element_present(
                "//button[@class='forex-button-pandats simple-button-pandats "
                "spinner-button-pandats']")
        login_button_locator.click()
        Logging().reportDebugStep(self, "Click the 'Login' button on Home page")
        return BrandLoginForm()

    def switch_first_tab_page(self):
        super().switch_first_tab_page()
        return BrandHomePage()

    def refresh(self):
        self.driver.refresh()
        return BrandHomePage()

    def open_drop_down_menu(self):
        super().open_drop_down_menu()
        return BrandHomePage()

    def select_module(self, module):
        super().select_module(module)
