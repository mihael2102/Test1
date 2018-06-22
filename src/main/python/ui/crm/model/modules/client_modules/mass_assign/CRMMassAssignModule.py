from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class CRMMassAssignModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def search_user(self, user_name):
        user_field = super().wait_element_to_be_clickable("//input[@id='searchstring']")
        user_field.clear()
        user_field.send_keys(user_name)
        return CRMMassAssignModule()

    def enter_check_box(self):
        check_box = self.driver.find_element(By.XPATH,
                                             "//li[@userid='122']//div[1]")
        check_box.click()

        return CRMMassAssignModule()

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH,
                                               "//button[contains(text(),'Assign')]")
        save_button.click()
        return CRMMassAssignModule()
