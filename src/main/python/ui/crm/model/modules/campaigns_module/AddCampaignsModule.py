from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.webdriver import ActionChains
from src.main.python.ui.crm.model.modules.campaigns_module.EditCampaignModule import EditCampaignModule
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class AddCampaignsModule(CRMBasePage):

    def perform_add_new_campaign(self, name, assigned_to, start_date, end_date, deal, rate):
        self.set_name(name)
        self.set_assigned_to(assigned_to)
        self.set_start_date(start_date)
        self.set_end_date(end_date)
        self.set_deal(deal)
        self.set_rate(rate)
        self.set_active_check_box()
        self.click_save_button()

    def set_name(self, name):
        search_button = super().wait_element_to_be_clickable("//input[@name='campaign_name']")
        search_button.send_keys(name)
        Logging().reportDebugStep(self, "The campaign name was set : "+name)
        return AddCampaignsModule()

    def set_assigned_to(self, assigned_to):
        sleep(2)
        assigned_to_drop_down = super().wait_element_to_be_clickable("//span[@dir='ltr']")
        assigned_to_drop_down.click()
        if global_var.current_brand_name == "stoxmarket":
            element = super().wait_element_to_be_clickable("//li[contains(text(),'pandaqaa pandaqa')]")
        elif global_var.current_brand_name == "capitalmarketsbanc":
            element = super().wait_element_to_be_clickable("//li[contains(text(),'Panda Auto')]")
        else:
            element = super().wait_element_to_be_clickable("//li[contains(text(),'%s')]" % assigned_to)
        element.click()
        Logging().reportDebugStep(self, "The assigned to was set: " + assigned_to)
        return AddCampaignsModule()

    def set_start_date(self, start_date):
        start_date_button = super().wait_element_to_be_clickable("//input[@name='start_date']")
        sleep(1)
        start_date_button.send_keys(Keys.CONTROL + "a")
        start_date_button.send_keys(Keys.DELETE)
        # start_date_button.clear()
        sleep(1)
        start_date_button.send_keys(start_date)
        start_date_button.send_keys(Keys.ENTER)
        sleep(1)
        # start_date_button.click()
        Logging().reportDebugStep(self, "The start date was set: " + start_date)
        return AddCampaignsModule()

    def set_end_date(self, end_date):
        search_button = super().wait_element_to_be_clickable("//input[@name='end_date']")
        sleep(1)
        search_button.send_keys(Keys.CONTROL + "a")
        search_button.send_keys(Keys.DELETE)
        sleep(1)
        # search_button.clear()
        search_button.send_keys(end_date)
        search_button.send_keys(Keys.ENTER)
        # search_button.click()
        Logging().reportDebugStep(self, "The end date was set: " + end_date)
        return AddCampaignsModule()

    def set_rate(self, rate):
        rate_field = super().wait_element_to_be_clickable("//input[@name='deal_value']")
        rate_field.send_keys(rate)
        Logging().reportDebugStep(self, "The rate was set: " + rate)
        return AddCampaignsModule()

    def click_save_button(self):
        save_button = super().wait_element_to_be_clickable("//button[@id='Save']")
        sleep(1)
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked ")
        return AddCampaignsModule()

    def set_deal(self, deal):
        deal_button = Select(self.driver.find_element(By.XPATH, "//select[@name='deal']"))
        deal_button.select_by_visible_text(deal)
        deal_drop_down = self.driver.find_element(By.XPATH, "//select[@name='deal']")
        deal_drop_down.click()
        Logging().reportDebugStep(self, "The deal was set ")
        return AddCampaignsModule()

    def set_active_check_box(self):
        activity_button = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        activity_button.click()
        Logging().reportDebugStep(self, "The deal was set ")
        return AddCampaignsModule()
