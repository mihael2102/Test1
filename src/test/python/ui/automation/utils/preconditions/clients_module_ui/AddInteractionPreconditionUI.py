import pytest
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreateTAPageUI import MT4CreateTAPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreateTAConstantsUI import MT4CreateTAConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class AddInteractionPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def add_interaction_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module. Find client by 'pandaqa' email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   AddDeleteEventConstantsUI.SHORT_EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Add Interaction: set Assign To, Subject, Comments -> Save&New """
        AddDeleteEventPageUI(self.driver)\
            .add_edit_event(
            btn_interaction=AddDeleteEventConstantsUI.BTN_ADD_INT,
            list4=AddDeleteEventConstantsUI.LIST_ASSIGN_TO, assign_to=AddDeleteEventConstantsUI.ASSIGN_TO,
            field1=AddDeleteEventConstantsUI.FIELD_SUBJECT, subject=AddDeleteEventConstantsUI.INT_SUBJ_1,
            comments=AddDeleteEventConstantsUI.COMMENTS,
            final_btn=AddDeleteEventConstantsUI.BTN_SAVE_NEW)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        AddDeleteEventPageUI(self.driver) \
            .click_cancel_btn()

        """ Get data of created event """
        record_num = ClientDetailsPageUI(self.driver)\
            .open_tab(ClientDetailsConstantsUI.TAB_ACTIVITIES) \
            .get_last_record_number()
        subject = ClientDetailsPageUI(self.driver)\
            .get_data_cell_table(TasksModuleConstantsUI.COLUMN_SUBJECT,
                                 record_num)
        assign_to = ClientDetailsPageUI(self.driver) \
            .get_data_cell_table(TasksModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                 record_num)
        comment = ClientDetailsPageUI(self.driver) \
            .get_data_cell_table(TasksModuleConstantsUI.COLUMN_COMMENT,
                                 record_num)

        """ Verify event data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(subject, AddDeleteEventConstantsUI.INT_SUBJ_1) \
            .comparator_string(assign_to, AddDeleteEventConstantsUI.ASSIGN_TO) \
            .comparator_string(comment, AddDeleteEventConstantsUI.COMMENTS)

        """ Edit Event """
        AddDeleteEventPageUI(self.driver) \
            .edit_record(record_num) \
