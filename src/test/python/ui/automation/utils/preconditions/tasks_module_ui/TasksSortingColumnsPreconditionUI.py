from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI


class TasksSortingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def tasks_sorting_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Tasks module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TASKS) \
            .open_tab_list_view_ui(TasksModuleConstantsUI.TAB_ALL)

        """ Get 'Subject' from 1st row of list view """
        get_data = GlobalModulePageUI(self.driver)
        subject_1 = get_data \
            .get_data_from_list_view_ui(
                column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                row='1')

        """ Sorting by 'Subject' column """
        GlobalModulePageUI(self.driver) \
            .click_arrow_up(
                column=TasksModuleConstantsUI.COLUMN_SUBJECT)
        subject_2 = get_data \
            .get_data_from_list_view_ui(
                column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                row='1')
        assert subject_1 != subject_2

        """ Get 'Status' from 1st row of list view """
        status_1 = get_data \
            .get_data_from_list_view_ui(
                column=TasksModuleConstantsUI.COLUMN_STATUS,
                row='1')

        """ Sorting by 'Client Name' column """
        GlobalModulePageUI(self.driver) \
            .click_arrow_up(
                column=TasksModuleConstantsUI.COLUMN_STATUS) \
            .click_arrow_up(
                column=TasksModuleConstantsUI.COLUMN_STATUS)
        status_2 = get_data \
            .get_data_from_list_view_ui(
                column=TasksModuleConstantsUI.COLUMN_STATUS,
                row='1')
        assert status_1 != status_2

        """ Get 'Start date' from 1st and 2nd row of list view """
        start_date_1 = get_data \
            .get_data_from_list_view_ui(
                column=TasksModuleConstantsUI.COLUMN_START_DATE,
                row='1')
        start_date_1 = start_date_1.split(' ')[0]
        start_date_1 = start_date_1.replace('-', '')
        start_date_2 = get_data \
            .get_data_from_list_view_ui(
                column=TasksModuleConstantsUI.COLUMN_START_DATE,
                row='2')
        start_date_2 = start_date_2.split(' ')[0]
        start_date_2 = start_date_2.replace('-', '')

        """ Sorting by 'Created Time' column """
        if start_date_1 > start_date_2:
            GlobalModulePageUI(self.driver) \
                .click_arrow_up(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE) \
                .click_arrow_up(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE)
            start_date_1 = get_data \
                .get_data_from_list_view_ui(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE,
                    row='1')
            start_date_1 = start_date_1.split(' ')[0]
            start_date_1 = start_date_1.replace('-', '')
            start_date_2 = get_data \
                .get_data_from_list_view_ui(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE,
                    row='2')
            start_date_2 = start_date_2.split(' ')[0]
            start_date_2 = start_date_2.replace('-', '')
            assert start_date_1 <= start_date_2
        else:
            GlobalModulePageUI(self.driver) \
                .click_arrow_down(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE) \
                .click_arrow_down(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE)
            start_date_1 = get_data \
                .get_data_from_list_view_ui(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE,
                    row='1')
            start_date_1 = start_date_1.split(' ')[0]
            start_date_1 = start_date_1.replace('-', '')
            start_date_2 = get_data \
                .get_data_from_list_view_ui(
                    column=TasksModuleConstantsUI.COLUMN_START_DATE,
                    row='2')
            start_date_2 = start_date_2.split(' ')[0]
            start_date_2 = start_date_2.replace('-', '')
            assert start_date_1 >= start_date_2
