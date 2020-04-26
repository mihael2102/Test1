from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.client_modules.mass_assign.MassAssignClientsModule import \
    MassAssignClientsModule
from src.main.python.ui.crm.model.modules.client_modules.mass_edit.MassEditClientsModule import MassEditClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
#import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class GlobalDetailsPageUI(CRMBasePage):

    def open_tab(self, title):
        sleep(0.5)
        try:
            Logging().reportDebugStep(self, "Open tab: " + title)
            tab = super().wait_load_element(
                "//mat-expansion-panel-header[@aria-expanded='false']//mat-panel-title/div[contains(text(),'%s')]"
                % title)
            self.driver.execute_script("arguments[0].click();", tab)
            sleep(1)
            self.wait_loading_to_finish_new_ui(15)
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Tab " + title + " already opened")
        return GlobalDetailsPageUI(self.driver)

    def click_to_view_btn(self, field):
        sleep(0.1)
        try:
            btn = super().wait_load_element(
                "//div[label='%s']//following-sibling::button/div[contains(@class,'click-to-view')]" % field)
            Logging().reportDebugStep(self, "Click to view in field: " + field)
            btn.click()
        except:
            Logging().reportDebugStep(self, "Click to view button is not available in field " + field)
        return GlobalDetailsPageUI(self.driver)

    def get_text_from_field(self, field):
        sleep(0.5)
        try:
            data = super().wait_load_element(
                "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field).text
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Field " + field + " is not editable")
            data = super().wait_load_element(
                "//div[label='%s']//following-sibling::div//div[@class='ng-star-inserted']" % field).text
        Logging().reportDebugStep(self, "Get data from field " + field + ": " + data)
        return data

    def click_edit_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click Edit button")
        edit_btn = super().wait_load_element(
            "//div[@class='wrap-navigation d-flex align-items-center']//button[span[i[contains(@class,'pencil')]]]")
        edit_btn.click()
        self.wait_loading_to_finish_new_ui(25)
        return GlobalDetailsPageUI(self.driver)

    """
        Edit field via pencil icon
    """

    def click_pencil_icon_in_field(self, field):
        sleep(1)
        Logging().reportDebugStep(self, "Click Pencil icon in field " + field)
        try:
            pencil_btn = super().wait_load_element(
                "//div[label='%s']//following-sibling::button//i[contains(@class,'pencil')]" % field)
            sleep(0.5)
            self.driver.execute_script("arguments[0].click();", pencil_btn)
            self.wait_loading_to_finish_new_ui(25)
        except:
            Logging().reportDebugStep(self, "Field is not editable")
        return GlobalDetailsPageUI(self.driver)

    def set_text_pencil_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Edit field '" + field + "' by pencil (set text): " + text)
        edit_fld = super().wait_load_element(
            "//div[label='%s']//following-sibling::mat-form-field//input" % field)
        edit_fld.clear()
        edit_fld.send_keys(text)
        return GlobalDetailsPageUI(self.driver)

    def select_item_list_pencil_field(self, field, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Edit field '" + field + "' by pencil (select item): " + item)
        first_item = super().wait_load_element(
            "(//div[label='%s']//following-sibling::div[@class='picklist-select']//span[text()])[2]" % field)
        self.driver.execute_script("arguments[0].click();", first_item)
        edit_fld = super().wait_load_element(
            "//div[label='%s']//following-sibling::div[@class='picklist-select']//span[text()='%s']"
            % (field, item))
        self.driver.execute_script("arguments[0].click();", edit_fld)
        return GlobalDetailsPageUI(self.driver)

    def click_confirm_btn_pencil_field(self, field):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Confirm' button in field: " + field)
        conf_btn = super().wait_load_element(
            "//div[label='%s']//following-sibling::div//field-confirm//div[@class='button-confirm']" % field)
        conf_btn.click()
        return GlobalDetailsPageUI(self.driver)

    """
        Action bar: Add Interaction, Click 2 Call, Send Mail, Send Sms
    """
    def click_action_bar_btn(self, button):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click '" + button + "' button")
        btn = super().wait_load_element("//div[@class='actions-bar d-flex']/button[@title='%s']" % button)
        btn.click()
        self.wait_loading_to_finish_new_ui(25)
        return GlobalDetailsPageUI(self.driver)
