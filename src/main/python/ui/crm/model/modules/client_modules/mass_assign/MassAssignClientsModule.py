from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import time

class MassAssignClientsModule(CRMBasePage):

    def search_user(self, user_name):
        user_field = super().wait_element_to_be_clickable("//input[@id='searchstring']")
        user_field.clear()
        user_field.send_keys(user_name)
        return MassAssignClientsModule(self.driver)

    def enter_check_box(self):
        time.sleep(6)
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[contains(text(), 'Panda Auto')]")
        check_box.click()

        return MassAssignClientsModule(self.driver)

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH,
                                               "//button[contains(text(),'Assign')]")
        save_button.click()
        return MassAssignClientsModule(self.driver)
