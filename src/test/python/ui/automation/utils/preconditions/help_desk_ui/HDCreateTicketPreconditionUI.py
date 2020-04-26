import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskCreateTicketPageUI import HelpDeskCreateTicketPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDCreateTicketConstantsUI import HDCreateTicketConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDModuleConstantsUI import HDModuleConstantsUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskModulePageUI import HelpDeskModulePageUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskDetailsPageUI import HelpDeskDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDDetailsConstantsUI import HDDetailsConstantsUI


@pytest.mark.run(order=31)
class HDCreateTicketPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_ticket_ui(self):
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
            .create_edit_ticket(
                create_btn=1, field1=HDCreateTicketConstantsUI.FIELD_TITLE, title=HDCreateTicketConstantsUI.TITLE,
                list1=HDCreateTicketConstantsUI.LIST_ASSIGNED, assigned_to=HDCreateTicketConstantsUI.ASSIGNED_TO,
                list2=HDCreateTicketConstantsUI.LIST_PRIORITY, priority=HDCreateTicketConstantsUI.PRIORITY,
                list3=HDCreateTicketConstantsUI.LIST_STATUS, status=HDCreateTicketConstantsUI.STATUS,
                list4=HDCreateTicketConstantsUI.LIST_CATEGORY, category=HDCreateTicketConstantsUI.CATEGORY,
                related_to=HDCreateTicketConstantsUI.RELATED_TO,
                list5=HDCreateTicketConstantsUI.LIST_SOURCE, source=HDCreateTicketConstantsUI.SOURCE,
                field2=HDCreateTicketConstantsUI.FIELD_DESCRIPTION, description=HDCreateTicketConstantsUI.DESCRIPTION,
                final_btn=HDCreateTicketConstantsUI.BTN_FINAL)

        """ Open ticket and get data """
        HelpDeskModulePageUI(self.driver)\
            .set_data_column_field(
                column=HDModuleConstantsUI.COLUMN_TITLE,
                data=HDCreateTicketConstantsUI.TITLE) \
            .open_ticket()

        details = HelpDeskDetailsPageUI(self.driver)

        title = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_TITLE)
        status = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_STATUS)
        priority = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_PRIORITY)
        category = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_CATEGORY)
        source = details \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_SOURCE)
        description = details \
            .open_tab(HDDetailsConstantsUI.TAB_DESCRIPTION) \
            .get_text_from_field(HDDetailsConstantsUI.FIELD_DESCRIPTION)

        """ Verify ticket's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(title, HDCreateTicketConstantsUI.TITLE) \
            .comparator_string(status, HDCreateTicketConstantsUI.STATUS) \
            .comparator_string(category, HDCreateTicketConstantsUI.CATEGORY) \
            .comparator_string(description, HDCreateTicketConstantsUI.DESCRIPTION)
            # .comparator_string(priority, HDCreateTicketConstantsUI.PRIORITY) \
            # .comparator_string(source, HDCreateTicketConstantsUI.SOURCE)
