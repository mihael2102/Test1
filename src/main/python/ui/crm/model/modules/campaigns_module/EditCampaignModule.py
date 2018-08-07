from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class EditCampaignModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_edit_campaign(self, name, assigned_to, start_date, end_date, deal, rate):
        self.set_campaign_name(name)
        self.set_assigned_to(assigned_to)
        self.set_start_date(start_date)
        self.set_end_date(end_date)
        self.set_deal(deal)
        self.set_rate(rate)
        self.click_save_button()

    def set_campaign_name(self, name):
        campaign_name_button = super().wait_element_to_be_clickable("//input[@name='campaign_name']")
        campaign_name_button.clear()
        campaign_name_button.send_keys(name)
        Logging().reportDebugStep(self, "The search button was clicked ")
        return EditCampaignModule()

    def set_assigned_to(self, assigned_to):
        assigned_to_drop_down = super().wait_element_to_be_clickable("//span[@dir='ltr']")
        assigned_to_drop_down.click()
        element = super().wait_element_to_be_clickable("//li[contains(text(),'%s')]" % assigned_to)
        element.click()
        Logging().reportDebugStep(self, "The assigned to was set: " + assigned_to)
        return EditCampaignModule()

    def set_start_date(self, start_date):
        start_date_button = super().wait_element_to_be_clickable("//input[@name='start_date']")
        start_date_button.clear()
        start_date_button.send_keys(start_date)
        start_date_button.send_keys(Keys.ENTER)
        Logging().reportDebugStep(self, "The start date was set: " + start_date)
        return EditCampaignModule()

    def set_end_date(self, end_date):
        end_date_button = super().wait_element_to_be_clickable("//input[@name='end_date']")
        end_date_button.clear()
        end_date_button.send_keys(end_date)
        end_date_button.send_keys(Keys.ENTER)
        Logging().reportDebugStep(self, "The end date was set: " + end_date)
        return EditCampaignModule()

    def set_rate(self, rate):
        rate_field = super().wait_element_to_be_clickable("//input[@name='deal_value']")
        rate_field.clear()
        rate_field.send_keys(rate)
        Logging().reportDebugStep(self, "The rate was set: " + rate)
        return EditCampaignModule()

    def click_save_button(self):
        save_button = super().wait_element_to_be_clickable("//button[@id='Save']")
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked ")
        return EditCampaignModule()

    def set_deal(self, deal):
        deal_button = Select(self.driver.find_element(By.XPATH, "//select[@name='deal']"))
        deal_button.select_by_visible_text(deal)
        Logging().reportDebugStep(self, "The deal was set ")
        return EditCampaignModule()

    def get_name_text(self, name):
        if super().wait_visible_of_element("//input[@value='%s']" % name).is_displayed():
            Logging().reportDebugStep(self, "Campaign name exist: " + name)
        else:
            return False
        return True

    def get_assigned_to_text(self):
        assigned_to_text = super().wait_element_to_be_clickable("//span[@dir='ltr']").text
        Logging().reportDebugStep(self, "The assigned to was set: " + assigned_to_text)
        return assigned_to_text

    def get_start_date_text(self, start_date):
        if super().wait_element_to_be_clickable("//input[@value='%s']" % start_date).is_displayed():
            Logging().reportDebugStep(self, "The start date of campaign is: " + start_date)
        else:
            return False
        return True

    def get_end_date_text(self, end_date):
        if super().wait_element_to_be_clickable("//input[@value='%s']" % end_date).is_displayed():
            Logging().reportDebugStep(self, "The end date of campaign is: " + end_date)
        else:
            return False
        return True

    def get_rate_text(self, rate):
        if super().wait_element_to_be_clickable("//input[@value='%s']" % rate).is_displayed():
            Logging().reportDebugStep(self, "The rate of campaign is : " + rate)
        else:
            return False
        return True

    def get_deal_text(self, deal):

        element = Select(self.driver.find_element(By.XPATH,
                                                  "//select[@name='deal']"))
        if element.first_selected_option.text == deal:

            Logging().reportDebugStep(self, "The deal is displayed: " + deal)

        else:
            return False

        return True

    def click_save_button(self):
        save_button = super().wait_element_to_be_clickable("//button[@id='Save']")
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked ")
        return EditCampaignModule()
