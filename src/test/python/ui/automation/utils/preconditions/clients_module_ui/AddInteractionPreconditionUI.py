import pytest
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI


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
            .set_data_column_field(column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   data=AddDeleteEventConstantsUI.SHORT_EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(row='1')

        """ Add Interaction: set Assign To, Subject, Comments -> Save&New """
        AddDeleteEventPageUI(self.driver)\
            .add_edit_event(
                btn_interaction=AddDeleteEventConstantsUI.BTN_ADD_INT,
                list4=AddDeleteEventConstantsUI.LIST_ASSIGN_TO, assign_to=AddDeleteEventConstantsUI.ASSIGN_TO,
                field1=AddDeleteEventConstantsUI.FIELD_SUBJECT, subject=AddDeleteEventConstantsUI.INT_SUBJ_1,
                comments=AddDeleteEventConstantsUI.COMMENTS,
                final_btn=AddDeleteEventConstantsUI.BTN_SAVE_NEW)\
            .click_cancel_btn()

        """ Get data of created event """
        record_num = ClientDetailsPageUI(self.driver)\
            .open_tab(ClientDetailsConstantsUI.TAB_ACTIVITIES) \
            .get_last_record_number()
        subject = ClientDetailsPageUI(self.driver)\
            .get_data_cell_table(column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                                 row=record_num)
        assign_to = ClientDetailsPageUI(self.driver) \
            .get_data_cell_table(column=TasksModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                 row=record_num)
        comment = ClientDetailsPageUI(self.driver) \
            .get_data_cell_table(column=TasksModuleConstantsUI.COLUMN_COMMENT,
                                 row=record_num)

        """ Verify event data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(subject, AddDeleteEventConstantsUI.INT_SUBJ_1) \
            .comparator_string(assign_to, AddDeleteEventConstantsUI.ASSIGN_TO) \
            .comparator_string(comment, AddDeleteEventConstantsUI.COMMENTS)

        """ Edit Event """
        AddDeleteEventPageUI(self.driver) \
            .add_edit_event(
            row=record_num,
            field1=AddDeleteEventConstantsUI.FIELD_SUBJECT, subject=AddDeleteEventConstantsUI.INT_SUBJ_2,
            final_btn=AddDeleteEventConstantsUI.BTN_SAVE)

        """ Get data of edited event """
        subject = ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_ACTIVITIES) \
            .get_data_cell_table(column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                                 row=record_num)

        """ Verify event data was edited """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(subject, AddDeleteEventConstantsUI.INT_SUBJ_2)

        """ Delete event """
        AddDeleteEventPageUI(self.driver)\
            .delete_record(record_num)
