from time import sleep

from selenium.webdriver import ActionChains
from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.modules.campaigns_module.EditCampaignModule import EditCampaignModule
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CampaignsPage(CRMBasePage):

    def open_add_campaign_module(self):
        add_campaign_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add Campaign')]")
        add_campaign_button.click()
        Logging().reportDebugStep(self, "The Add campaign module was opened")
        return AddCampaignsModule()

    def perform_searching_campaign_by_name(self, campaign_name):
        add_campaign_button = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input")
        add_campaign_button.clear()
        add_campaign_button.send_keys(campaign_name)
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return CampaignsPage()

    def campaign_exist(self):
        campaign = super().wait_load_element("//*[@id='row0ListGrid0']/div[2]/div/a").text
        Logging().reportDebugStep(self, "Verify campaign name")
        return campaign

    def perform_searching_campaign_by_columns(self, campaign_name, activity, start_date, cpa):
        self.set_campaign_name(campaign_name)
        self.set_activity(activity)
        self.set_start_date(start_date)
        self.set_cpa(cpa)
        return CampaignsPage()

    def open_campaign_view(self, campaign_name):
        campaign_name_link = super().wait_element_to_be_clickable(
            "//a[contains(text(),'%s')]" % campaign_name)
        sleep(2)
        campaign_name_link.click()
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return EditCampaignModule()

    def click_delete_campaign(self):
        delete_element = super().wait_visible_of_element("//div[@role='row'][1]//div[@title='Delete']")
        hoverer = ActionChains(self.driver).move_to_element(delete_element).move_by_offset(20, 0)
        hoverer.perform()
        delete_element.click()
        Logging().reportDebugStep(self, "The campaign was deleted ")
        return CampaignsPage()

    def get_message(self):
        delete_button = super().wait_element_to_be_clickable("//div[@role='row'][1]//div[15]//span")
        delete_button.click()
        Logging().reportDebugStep(self, "The message was getting ")
        return delete_button.text

    def set_campaign_name(self, campaign_name):
        add_campaign_button = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input")
        add_campaign_button.clear()
        add_campaign_button.send_keys(campaign_name)
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return CampaignsPage()

    def set_activity(self, activity):
        activity_button = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[3]")
        activity_button.click()
        reset = super().wait_visible_of_element("(//div[@class='chkbox'])[1]")
        reset.click()
        item = super().wait_visible_of_element(
            "(//div[@class='chkbox'])[%s]" % activity)
        item.click()
        activity_button.click()
        Logging().reportDebugStep(self, "The activity entered: " + activity)
        return CampaignsPage()

    def set_start_date(self, start_date):
        start_date_field = super().wait_visible_of_element(
            "//div[@class='jqx-max-size jqx-position-relative']//div[1]")
        start_date_field.click()
        sleep(2)
        today_field = super().wait_visible_of_element("//a[contains(text(),'Today')]")
        today_field.click()
        Logging().reportDebugStep(self, "The today  was clicked: " + start_date)
        return CampaignsPage()

    def get_start_date(self):
        actual_start_date = super().wait_load_element("//*[@id='start_date']").get_attribute("value")
        Logging().reportDebugStep(self, "Current start date is: " + actual_start_date)
        return actual_start_date

    def get_end_date(self):
        actual_end_date = super().wait_load_element("//*[@id='end_date']").get_attribute("value")
        Logging().reportDebugStep(self, "Current end date is: " + actual_end_date)
        return actual_end_date

    def click_cancel_button(self):
        cancel_button = super().wait_load_element("//*[@id='Cancel']")
        sleep(2)
        cancel_button.click()
        Logging().reportDebugStep(self, "The Cancel button is clicked")
        return CampaignsPage()

    def deleting_confirmation(self):
        super().wait_visible_of_element("//div[contains(text(),'Confirm Delete')]")     #deleting confirmation popup is appear
        deleting_confirmation_button = super().wait_element_to_be_clickable("//button[contains(text(),'OK')]")
        sleep(1)
        deleting_confirmation_button.click()
        Logging().reportDebugStep(self, "The deleting confirmation button is clicked")
        return CampaignsPage()

    def check_campaign_deleted(self):
        super().wait_visible_of_element("//span[contains(text(), 'No data to display')]")
        Logging().reportDebugStep(self, "Campaign not found")
        return CampaignsPage()


    # def set_assigned_to(self, assigned_to):
    #     assigned_to_field = super().wait_visible_of_element(
    #         "//div[@id='filterrow.ListGrid0']//div[6]/div[1]//div[2]")
    #     assigned_to_field.click()
    #
    #     select_all = super().wait_visible_of_element(
    #         "(//div[@role='option'])[37]//div[1]")
    #     select_all.click()
    #
    #     assigned_to_item = super().wait_visible_of_element(
    #         "//span[contains(text(),'%s')]" % assigned_to)
    #
    #     self.driver.execute_script("arguments[0].scrollIntoView();", assigned_to_item)
    #     sleep(3)
    #
    #     first_item = super().wait_visible_of_element(
    #         "//span[contains(text(),'%s')]//preceding-sibling::div[1]/div[1]//div[1]" % assigned_to)
    #
    #     hoverer = ActionChains(self.driver).move_to_element(first_item).click(first_item)
    #     hoverer.perform()
    #     first_item.click()
    #     Logging().reportDebugStep(self, "The assigned_to was entered: " + assigned_to)
    #     return CampaignsPage()

    def set_cpa(self, cpa):
        today_field = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[11]//input")
        today_field.send_keys(cpa)
        Logging().reportDebugStep(self, "The cpa was entered: " + cpa)
        return CampaignsPage()
