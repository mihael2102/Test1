import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDCreateTicketConstantsUI import HDCreateTicketConstantsUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDModuleConstantsUI import HDModuleConstantsUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskModulePageUI import HelpDeskModulePageUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskDetailsPageUI import HelpDeskDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDDetailsConstantsUI import HDDetailsConstantsUI


@pytest.mark.run(order=31)
class HDEditTicketPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def edit_ticket_ui(self):
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

        """ Edit ticket """
        HelpDeskModulePageUI(self.driver) \
            .set_data_column_field(
                column=HDModuleConstantsUI.COLUMN_TITLE,
                data=HDCreateTicketConstantsUI.TITLE) \
            .open_ticket() \
            .click_edit_btn() \
            .create_edit_ticket(
                list2=HDCreateTicketConstantsUI.LIST_PRIORITY, priority=HDCreateTicketConstantsUI.PRIORITY_EDIT,
                list3=HDCreateTicketConstantsUI.LIST_STATUS, status=HDCreateTicketConstantsUI.STATUS_EDIT,
                final_btn=HDCreateTicketConstantsUI.BTN_FNL_EDIT)

        """ Verify data was updated """
        details = HelpDeskDetailsPageUI(self.driver)

        status = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_STATUS)
        priority = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_PRIORITY)

        """ Verify ticket's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status, HDCreateTicketConstantsUI.STATUS_EDIT) \
            .comparator_string(priority, HDCreateTicketConstantsUI.PRIORITY_EDIT)
