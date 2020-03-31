import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskCreateTicketPageUI import HelpDeskCreateTicketPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDCreateTicketConstantsUI import HDCreateTicketConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HelpDeskModuleConstantsUI import HelpDeskModuleConstantsUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskModulePageUI import HelpDeskModulePageUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskDetailsPageUI import HelpDeskDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDDetailsConstantsUI import HDDetailsConstantsUI


@pytest.mark.run(order=31)
class HelpDeskCreateTicketPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def create_delete_ticket_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Help Desk module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_HELP_DESK)

        """ Create New Ticket """
        HelpDeskCreateTicketPageUI(self.driver) \
            .click_create_ticket_btn() \
            .set_title(HDCreateTicketConstantsUI.TITLE) \
            .select_assigned_to(HDCreateTicketConstantsUI.ASSIGNED_TO) \
            .select_priority(HDCreateTicketConstantsUI.PRIORITY) \
            .select_status(HDCreateTicketConstantsUI.STATUS) \
            .select_category(HDCreateTicketConstantsUI.CATEGORY) \
            .select_related_to(HDCreateTicketConstantsUI.RELATED_TO) \
            .select_ticket_source(HDCreateTicketConstantsUI.SOURCE) \
            .set_description(HDCreateTicketConstantsUI.DESCRIPTION) \
            .click_save_button()

        """ Verify successful message """
        # GlobalTablePageUI(self.driver) \
        #     .verify_success_message() \
        #     .click_ok()

        """ Search ticket """
        GlobalModulePageUI(self.driver)\
            .set_data_column_field(column=HelpDeskModuleConstantsUI.COLUMN_TITLE,
                                   data=HDCreateTicketConstantsUI.TITLE)

        """ Open ticket and get data """
        HelpDeskModulePageUI(self.driver) \
            .open_ticket()

        details = HelpDeskDetailsPageUI(self.driver)

        title = details \
            .get_title()
        status = details \
            .get_status()
        assigned_to = details \
            .get_assigned_to()
        priority = details \
            .get_priority()
        category = details \
            .get_category()
        source = details \
            .get_source()
        description = details \
            .open_tab(HDDetailsConstantsUI.TAB_DESCRIPTION) \
            .get_description()

        """ Verify ticket's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(title, HDCreateTicketConstantsUI.TITLE) \
            .comparator_string(status, HDCreateTicketConstantsUI.STATUS) \
            .comparator_string(category, HDCreateTicketConstantsUI.CATEGORY) \
            .comparator_string(description, HDCreateTicketConstantsUI.DESCRIPTION) \
            .comparator_string(assigned_to, HDCreateTicketConstantsUI.ASSIGNED_TO) \
            .comparator_string(priority, HDCreateTicketConstantsUI.PRIORITY) \
            .comparator_string(source, HDCreateTicketConstantsUI.SOURCE)\
            .came_back_on_previous_page()

        """ Delete ticket """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=HelpDeskModuleConstantsUI.COLUMN_TITLE,
                                   data=HDCreateTicketConstantsUI.TITLE) \
            .open_actions_list() \
            .click_delete_icon_list_view(HelpDeskModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1) \
            .approve_deleting() \
            .verify_success_message() \
            .click_ok() \
            .set_data_column_field(column=HelpDeskModuleConstantsUI.COLUMN_TITLE,
                                   data=HDCreateTicketConstantsUI.TITLE) \
            .verify_data_not_found()
