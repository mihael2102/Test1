from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI


class ClientsSortingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def clients_sorting_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS) \
            .open_tab_list_view_ui(ClientsModuleConstantsUI.TAB_ALL)

        """ Get 'CRM Id' from 1st and 2nd row of list view """
        get_data = GlobalModulePageUI(self.driver)
        crm_id_1 = get_data \
            .get_data_from_list_view_ui(
                column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                row='1')
        crm_id_1 = crm_id_1.replace('ACC', '')
        crm_id_2 = get_data \
            .get_data_from_list_view_ui(
                column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                row='2')
        crm_id_2 = crm_id_2.replace('ACC', '')

        """ Sorting by 'CRM Id' column """
        if crm_id_1 > crm_id_2:
            GlobalModulePageUI(self.driver) \
                .click_arrow_up(
                    column=ClientsModuleConstantsUI.COLUMN_CRM_ID)
            crm_id_1 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                    row='1')
            crm_id_1 = crm_id_1.replace('ACC', '')
            crm_id_2 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                    row='2')
            crm_id_2 = crm_id_2.replace('ACC', '')
            assert crm_id_1 < crm_id_2
        else:
            GlobalModulePageUI(self.driver) \
                .click_arrow_down(
                    column=ClientsModuleConstantsUI.COLUMN_CRM_ID)
            crm_id_1 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                    row='1')
            crm_id_1 = crm_id_1.replace('ACC', '')
            crm_id_2 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                    row='2')
            crm_id_2 = crm_id_2.replace('ACC', '')
            assert crm_id_1 > crm_id_2

        """ Get 'Client Name' from 1st row of list view """
        client_name_1 = get_data \
            .get_data_from_list_view_ui(
                column=ClientsModuleConstantsUI.COLUMN_CLIENT_NAME,
                row='1')

        """ Sorting by 'Client Name' column """
        GlobalModulePageUI(self.driver) \
            .click_arrow_up(
                column=ClientsModuleConstantsUI.COLUMN_CLIENT_NAME)
        client_name_2 = get_data \
            .get_data_from_list_view_ui(
                column=ClientsModuleConstantsUI.COLUMN_CLIENT_NAME,
                row='1')
        assert client_name_1 != client_name_2

        """ Get 'Created Time' from 1st and 2nd row of list view """
        created_time_1 = get_data \
            .get_data_from_list_view_ui(
                column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME,
                row='1')
        created_time_1 = created_time_1.split(' ')[0]
        created_time_1 = created_time_1.replace('-', '')
        created_time_2 = get_data \
            .get_data_from_list_view_ui(
                column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME,
                row='2')
        created_time_2 = created_time_2.split(' ')[0]
        created_time_2 = created_time_2.replace('-', '')

        """ Sorting by 'Created Time' column """
        if created_time_1 > created_time_2:
            GlobalModulePageUI(self.driver) \
                .click_arrow_up(
                    column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME)
            created_time_1 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='1')
            created_time_1 = created_time_1.split(' ')[0]
            created_time_1 = created_time_1.replace('-', '')
            created_time_2 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='2')
            created_time_2 = created_time_2.split(' ')[0]
            created_time_2 = created_time_2.replace('-', '')
            assert created_time_1 <= created_time_2
        else:
            GlobalModulePageUI(self.driver) \
                .click_arrow_down(
                    column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME)
            created_time_1 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='1')
            created_time_1 = created_time_1.split(' ')[0]
            created_time_1 = created_time_1.replace('-', '')
            created_time_2 = get_data \
                .get_data_from_list_view_ui(
                    column=ClientsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='2')
            created_time_2 = created_time_2.split(' ')[0]
            created_time_2 = created_time_2.replace('-', '')
            assert created_time_1 >= created_time_2
