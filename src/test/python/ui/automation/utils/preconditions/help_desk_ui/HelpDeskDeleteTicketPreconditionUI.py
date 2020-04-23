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
class HelpDeskDeleteTicketPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def delete_ticket_ui(self):
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
