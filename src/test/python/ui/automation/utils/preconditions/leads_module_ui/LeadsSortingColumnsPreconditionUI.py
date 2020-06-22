from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class LeadsSortingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def leads_sorting_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS) \
            .open_tab_list_view_ui(LeadsModuleConstantsUI.TAB_ALL)

        """ Get 'Lead No' from 1st and 2nd row of list view """
        get_data = GlobalModulePageUI(self.driver)
        lead_no_1 = get_data \
            .get_data_from_list_view_ui(
                column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                row='1')
        lead_no_1 = lead_no_1.replace('LEA', '')
        lead_no_2 = get_data \
            .get_data_from_list_view_ui(
                column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                row='2')
        lead_no_2 = lead_no_2.replace('LEA', '')

        """ Sorting by 'Lead No' column """
        if lead_no_1 > lead_no_2:
            GlobalModulePageUI(self.driver)\
                .click_arrow_up(
                    column=LeadsModuleConstantsUI.COLUMN_LEAD_NO)
            lead_no_1 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                    row='1')
            lead_no_1 = lead_no_1.replace('LEA', '')
            lead_no_2 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                    row='2')
            lead_no_2 = lead_no_2.replace('LEA', '')
            assert lead_no_1 < lead_no_2
        else:
            GlobalModulePageUI(self.driver) \
                .click_arrow_down(
                    column=LeadsModuleConstantsUI.COLUMN_LEAD_NO)
            lead_no_1 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                    row='1')
            lead_no_1 = lead_no_1.replace('LEA', '')
            lead_no_2 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                    row='2')
            lead_no_2 = lead_no_2.replace('LEA', '')
            assert lead_no_1 > lead_no_2

        """ Get 'Last Name' from 1st row of list view """
        l_name_1 = get_data \
            .get_data_from_list_view_ui(
                column=LeadsModuleConstantsUI.COLUMN_LNAME,
                row='1')

        """ Sorting by 'First Name' column """
        GlobalModulePageUI(self.driver) \
            .click_arrow_up(
                column=LeadsModuleConstantsUI.COLUMN_FNAME)
        l_name_2 = get_data \
            .get_data_from_list_view_ui(
                column=LeadsModuleConstantsUI.COLUMN_LNAME,
                row='1')
        assert l_name_1 != l_name_2

        """ Get 'Created Time' from 1st and 2nd row of list view """
        created_time_1 = get_data \
            .get_data_from_list_view_ui(
                column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME,
                row='1')
        created_time_1 = created_time_1.split(' ')[0]
        created_time_1 = created_time_1.replace('-', '')
        created_time_2 = get_data \
            .get_data_from_list_view_ui(
                column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME,
                row='2')
        created_time_2 = created_time_2.split(' ')[0]
        created_time_2 = created_time_2.replace('-', '')

        """ Sorting by 'Created Time' column """
        if created_time_1 > created_time_2:
            GlobalModulePageUI(self.driver) \
                .click_arrow_up(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME) \
                .click_arrow_up(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME)
            created_time_1 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='1')
            created_time_1 = created_time_1.split(' ')[0]
            created_time_1 = created_time_1.replace('-', '')
            created_time_2 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='2')
            created_time_2 = created_time_2.split(' ')[0]
            created_time_2 = created_time_2.replace('-', '')
            assert created_time_1 <= created_time_2
        else:
            GlobalModulePageUI(self.driver) \
                .click_arrow_down(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME) \
                .click_arrow_down(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME)
            created_time_1 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='1')
            created_time_1 = created_time_1.split(' ')[0]
            created_time_1 = created_time_1.replace('-', '')
            created_time_2 = get_data \
                .get_data_from_list_view_ui(
                    column=LeadsModuleConstantsUI.COLUMN_CREATED_TIME,
                    row='2')
            created_time_2 = created_time_2.split(' ')[0]
            created_time_2 = created_time_2.replace('-', '')
            assert created_time_1 >= created_time_2
