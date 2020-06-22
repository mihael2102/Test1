from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from src.main.python.ui.crm.model.pages.campaign_module_ui.CampaignCreatePage import CampaignCreatePage
from src.main.python.ui.crm.model.modules.campaigns_module.EditCampaignModule import EditCampaignModule
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CampaignsPage(CRMBasePage):

    def open_add_campaign_module(self):
        sleep(0.2)
        add_campaign_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add Campaign')]")
        add_campaign_button.click()
        Logging().reportDebugStep(self, "The Add campaign module was opened")
        return CampaignCreatePage(self.driver)

    def perform_searching_campaign_by_name(self, campaign_name):
        add_campaign_button = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input")
        add_campaign_button.clear()
        add_campaign_button.send_keys(campaign_name)
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return CampaignsPage(self.driver)

    def campaign_exist(self):
        campaign = super().wait_load_element("//*[@id='row0ListGrid0']/div[2]/div/a").text
        Logging().reportDebugStep(self, "Verify campaign name")
        return campaign

    def perform_searching_campaign_by_columns(self, campaign_name, campaign_id, cpa):
        self.set_campaign_id(campaign_id)
        sleep(1)
        self.set_campaign_name(campaign_name)
        sleep(1)
        self.set_cpa(cpa)
        sleep(0.5)
        return CampaignsPage(self.driver)

    def open_campaign_view(self, campaign_name):
        sleep(0.2)
        campaign_name_link = super().wait_element_to_be_clickable(
            "//a[contains(text(),'%s')]" % campaign_name)
        sleep(2)
        hoverer = ActionChains(self.driver).move_to_element(campaign_name_link).move_by_offset(20, 0)
        hoverer.perform()
        campaign_name_link.click()
        sleep(2)
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return EditCampaignModule()

    def click_delete_campaign(self):
        delete_element = super().wait_visible_of_element("//div[@role='row'][1]//div[@title='Delete']")
        hoverer = ActionChains(self.driver).move_to_element(delete_element).move_by_offset(20, 0)
        hoverer.perform()
        delete_element.click()
        Logging().reportDebugStep(self, "The campaign was deleted ")
        return CampaignsPage(self.driver)

    def get_message(self):
        delete_button = super().wait_element_to_be_clickable("//div[@role='row'][1]//div[15]//span")
        delete_button.click()
        Logging().reportDebugStep(self, "The message was getting ")
        return delete_button.text

    def set_campaign_name(self, campaign_name):
        name_field = super().wait_visible_of_element(
            "(//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input)[1]")
        name_field.clear()
        name_field.send_keys(campaign_name)
        Logging().reportDebugStep(self, "The Campaign Name was entered: " + campaign_name)
        return CampaignsPage(self.driver)

    def set_campaign_id(self, campaign_id):
        id_field = super().wait_load_element(
            "/html/body/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/div/input")
        id_field.clear()
        id_field.send_keys(campaign_id)
        Logging().reportDebugStep(self, "The Campaign ID was set: " + campaign_id)
        return CampaignsPage(self.driver)

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
        return CampaignsPage(self.driver)

    def set_start_date(self, start_date):
        start_date_field = super().wait_visible_of_element(
            "//div[@class='jqx-max-size jqx-position-relative']//div[1]")
        start_date_field.click()
        sleep(2)
        today_field = super().wait_visible_of_element("//a[contains(text(),'Today')]")
        today_field.click()
        Logging().reportDebugStep(self, "The today was clicked: " + start_date)
        return CampaignsPage(self.driver)

    def get_start_date(self):
        actual_start_date = super().wait_load_element("//*[@id='start_date']").get_attribute("value")
        Logging().reportDebugStep(self, "Current start date is: " + actual_start_date)
        return actual_start_date

    def get_end_date(self):
        actual_end_date = super().wait_load_element("//*[@id='end_date']").get_attribute("value")
        Logging().reportDebugStep(self, "Current end date is: " + actual_end_date)
        return actual_end_date

    def get_deal(self):
        deal_index = super().wait_load_element("//*[@id='deal']").get_attribute("selectedIndex")
        deal = ""
        if int(deal_index) == 0:
            deal = "CPA"
        elif int(deal_index) == 1:
            deal = "CPL"
        elif int(deal_index) == 2:
            deal = "FIX"
        Logging().reportDebugStep(self, "Current end date is: " + deal)
        return deal

    def get_rate(self):
        rate = super().wait_load_element("//input[@name='deal_value']").get_attribute("value")
        Logging().reportDebugStep(self, "Current end date is: " + rate)
        return rate

    def click_cancel_button(self):
        cancel_button = super().wait_load_element("//*[@id='Cancel']")
        sleep(2)
        cancel_button.click()
        Logging().reportDebugStep(self, "The Cancel button is clicked")
        return CampaignsPage(self.driver)

    def deleting_confirmation(self):
        super().wait_visible_of_element("//div[contains(text(),'Confirm Delete')]")     #deleting confirmation popup is appear
        deleting_confirmation_button = super().wait_element_to_be_clickable("//button[contains(text(),'OK')]")
        sleep(1)
        deleting_confirmation_button.click()
        Logging().reportDebugStep(self, "The deleting confirmation button is clicked")
        return CampaignsPage(self.driver)

    def check_campaign_deleted(self):
        super().wait_visible_of_element("//span[contains(text(), 'No data to display')]")
        Logging().reportDebugStep(self, "Campaign not found")
        return CampaignsPage(self.driver)

    def set_cpa(self, cpa):
        today_field = super().wait_visible_of_element("(//div[@id='filterrow.ListGrid0']//div[11]//input)[1]")
        today_field.send_keys(cpa)
        Logging().reportDebugStep(self, "The CPA was entered: " + cpa)
        return CampaignsPage(self.driver)

    def get_campaign_id_list_view(self):
        campaign_id = super().wait_load_element("(//a[contains(@onclick,'PandaCampaign')])[1]").text
        Logging().reportDebugStep(self, "Get first Campaign ID from list view: " + campaign_id)
        return campaign_id

    def get_campaign_name_list_view(self):
        campaign_name = super().wait_load_element("(//a[contains(@onclick,'PandaCampaign')])[2]").text
        Logging().reportDebugStep(self, "Get first Campaign Name from list view: " + campaign_name)
        return campaign_name

    def get_cpa_list_view(self):
        cpa = super().wait_load_element("(//span[@title='USD'])[1]").text
        Logging().reportDebugStep(self, "Get first CPA from list view: " + cpa)
        return cpa

    def campaign_data_checker(self, data):
        sleep(2)
        try:
            table = self.driver.find_element_by_xpath("//*[@id='contenttableListGrid0']")
            row_count = 0
            for tr in table.find_elements_by_xpath("//div[@role='row']"):
                if tr.text:
                    assert data.lower() in tr.text.lower()
                    row_count += 1
            Logging().reportDebugStep(self, data + " is verified in " + str(row_count) + " rows")
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            super().wait_visible_of_element \
                ("//span[@class='genHeaderSmall message_title' and contains(text(),'There are no')]")
            Logging().reportDebugStep(self, "There are no documents that match the search criteria!")
        return CampaignsPage(self.driver)

    def clear_filter(self):
        clear_filter = super().wait_load_element("//div/a[@id='clearfilteringbutton']")
        self.driver.execute_script("arguments[0].click();", clear_filter)
        sleep(1)
        Logging().reportDebugStep(self, "Clear filter")
        return CampaignsPage(self.driver)

    def refresh_filter(self):
        refresh_filter = super().wait_load_element("//div/a[@id='refreshgridbutton']")
        self.driver.execute_script("arguments[0].click();", refresh_filter)
        sleep(1)
        Logging().reportDebugStep(self, "Refresh filter")
        return CampaignsPage(self.driver)
