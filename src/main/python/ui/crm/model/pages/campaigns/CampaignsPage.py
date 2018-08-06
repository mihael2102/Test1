from selenium.webdriver import ActionChains

from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.modules.campaigns_module.EditCampaignModule import EditCampaignModule
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CampaignsPage(CRMBasePage):
    def __init__(self) -> None:
        super().__init__()

    def open_add_campaign_module(self):
        add_campaign_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add Campaign')]")
        add_campaign_button.click()
        Logging().reportDebugStep(self, "The Add campaign module ")
        return AddCampaignsModule()

    def perform_searching_campaign_by_name(self, campaign_name):
        add_campaign_button = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input")
        add_campaign_button.clear()
        add_campaign_button.send_keys(campaign_name)
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return CampaignsPage()

    def open_campaign_view(self, campaign_name):
        campaign_name_link = super().wait_visible_of_element(
            "//a[contains(text(),'%s')]" % campaign_name)
        campaign_name_link.click()
        Logging().reportDebugStep(self, "The campaign_name was entered: " + campaign_name)
        return EditCampaignModule()

    def click_delete_campaign(self):
        delete_element = super().wait_visible_of_element("//div[@role='row'][1]//div[@title='Delete']")
        hoverer = ActionChains(self.driver).move_to_element(delete_element).move_by_offset(20, 0)
        hoverer.perform()
        Logging().reportDebugStep(self, "The campaign was deleted ")
        return CampaignsPage()

    def get_message(self):
        delete_button = super().wait_element_to_be_clickable("//div[@role='row'][1]//div[15]//span")
        delete_button.click()
        Logging().reportDebugStep(self, "The message was getting ")
        return delete_button.text
