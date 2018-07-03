from time import sleep
from datetime import *
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.filter.FilterModule import FilterModule
from src.main.python.ui.crm.model.modules.leads_module.MassAssignLeadModule import MassAssignLeadModule
from src.main.python.ui.crm.model.modules.leads_module.MassEditLeadModule import MassEditLeadModule
from src.main.python.ui.crm.model.pages.leads_pages.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging


class LeadsModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def open_create_lead_module(self):
        task_module = super().wait_load_element("//td[@class='moduleName']//button[1]")
        task_module.click()
        Logging().reportDebugStep(self, "Create leads module is opened")
        return CreateLeadsProfilePage()

    def open_create_filter_pop_up(self):
        filter_button = super().wait_element_to_be_clickable("//a[@title='Create Filter']")
        filter_button.click()
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterModule()

    '''
         Returns a confirmation  message if the user entered a valid password
    '''

    def get_confirm_message_lead_module(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + confirm_message.text)
        return confirm_message.text

    def select_three_records_task_module(self):
        sleep(1)
        first_check_box = super().wait_element_to_be_clickable("//tbody[@id='listBody']//tr[1]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[2]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//tbody[@id='listBody']//tr[3]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The records were selected")
        return LeadsModule()

    def open_mass_edit_task(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass Edit']")
        mass_edit_module.click()
        return MassEditLeadModule()

    def open_mass_assign_lead_module(self):
        mass_edit_module = super().wait_element_to_be_clickable("//input[@value='Mass assign']")
        mass_edit_module.click()
        return MassAssignLeadModule()

    '''
            Returns a task was_updated  message if the user entered a valid password
     '''

    def get_message_lead_module(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns the message task  : " + confirm_message.text)
        return confirm_message.text

    def click_ok(self):
        super().click_ok()
        return LeadsModule()

    def perform_screen_shot_lead_module(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/lead_module/lead update_screenshot %s.png' % now
        Config.browser.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('screenshot', Config.browser.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return LeadsModule()

    def delete_filter_lead_module(self):
        delete_filter_button = super().wait_element_to_be_clickable("//a[@title='Delete']")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "The delete button was clicked")
        return LeadsModule()

    def confirm_delete_lead_module(self):
        delete_filter_button = super().wait_element_to_be_clickable("//button[contains(text(),'OK')]")
        delete_filter_button.click()
        Logging().reportDebugStep(self, "Filter was deleted")
        return LeadsModule()
