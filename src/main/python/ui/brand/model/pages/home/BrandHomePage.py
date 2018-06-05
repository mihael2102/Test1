import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.forms.login.BrandLoginForm import BrandLoginForm
from src.main.python.ui.brand.model.forms.signup.BrandSignUpForm import BrandSignUpForm
from src.main.python.utils.screenshot.ScreenShot import ScreenShot


class BrandHomePage(BrandBasePage):

    def __init__(self):
        super().__init__()

    @allure.step("Open first tab")
    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        return BrandHomePage()

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        return BrandHomePage()

    def open_sign_form(self):
        sign_on_button_locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains (text(),'Sign Up')]")))

        screen_path = "/"
        screen = ScreenShot(self.driver)
        sign_on_button_locator.click()
        screen.perform_screen_shot(screen_path + "NewForexLoginPage.png")
        return BrandSignUpForm()

    @allure.step("Login")
    def login(self):
        login_button_locator = super().wait_load_element_present("//button[@class='forex-button-pandats simple-button-pandats "
                                                         "spinner-button-pandats']")
        login_button_locator.click()
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
