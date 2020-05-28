from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
# from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CampaignCreatePage(CRMBasePage):

    def add_campaign(self, name=None, assigned_to=None, deal=None, rate=None):
        if name:
            self.set_name(name)
        if assigned_to:
            self.set_assigned_to(assigned_to)
        if deal:
            self.set_deal(deal)
        if rate:
            self.set_rate(rate)
        self.click_save_button()
        return CampaignsPage(self.driver)

    def set_name(self, name):
        search_button = super().wait_element_to_be_clickable("//input[@name='campaign_name']")
        search_button.send_keys(name)
        Logging().reportDebugStep(self, "The campaign name was set : "+name)
        return CampaignCreatePage()

    def set_assigned_to(self, assigned_to):
        assigned_to_drop_down = super().wait_element_to_be_clickable("//span[@dir='ltr']")
        assigned_to_drop_down.click()
        assign_to_field = super().wait_load_element("/html/body/span/span/span[1]/input")
        assign_to_field.send_keys(assigned_to)
        element = super().wait_element_to_be_clickable("//li[contains(text(),'%s')]" % assigned_to)
        element.click()
        Logging().reportDebugStep(self, "The assigned to was set: " + assigned_to)
        return CampaignCreatePage()

    def set_start_date(self, start_date):
        start_date_button = super().wait_element_to_be_clickable("//input[@name='start_date']")
        sleep(1)
        start_date_button.send_keys(Keys.CONTROL + "a")
        start_date_button.send_keys(Keys.DELETE)
        #start_date_button.clear()
        sleep(1)
        start_date_button.send_keys(start_date)
        start_date_button.send_keys(Keys.ENTER)
        sleep(1)
        # start_date_button.click()
        Logging().reportDebugStep(self, "The start date was set: " + start_date)
        return CampaignCreatePage()

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
        return CampaignCreatePage()

    def set_rate(self, rate):
        rate_field = super().wait_element_to_be_clickable("//input[@name='deal_value']")
        rate_field.clear()
        rate_field.send_keys(rate)
        Logging().reportDebugStep(self, "The rate was set: " + rate)
        return CampaignCreatePage()

    def click_save_button(self):
        save_button = super().wait_element_to_be_clickable("//button[@id='Save']")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", save_button)
        # save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked ")
        return CampaignCreatePage()

    def set_deal(self, deal):
        deal_button = Select(self.driver.find_element(By.XPATH, "//select[@name='deal']"))
        deal_button.select_by_visible_text(deal)
        deal_drop_down = self.driver.find_element(By.XPATH, "//select[@name='deal']")
        # deal_drop_down.click()
        self.driver.execute_script("arguments[0].click();", deal_drop_down)
        Logging().reportDebugStep(self, "The deal was set ")
        return CampaignCreatePage()

    def set_active_check_box(self):
        activity_button = super().wait_element_to_be_clickable("//input[@type='checkbox']")
        sleep(2)
        activity_button.click()
        Logging().reportDebugStep(self, "The active check box was set ")
        return CampaignCreatePage()
