from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.main_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class TabTasksModuleCRM(BaseTest):

    def test_check_tab_tasks_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        show_all_tab_name = task_module.click_show_all_tab()
        show_mine_tab_name = task_module.click_show_mine_tab()
        today_tab_name = task_module.click_today_tab()
        this_week_tab_name = task_module.click_this_week_tab()
        history_tab_name = task_module.click_history_tab()

        assert show_all_tab_name == Config.data.get_data_task_module(CRMTaskModuleConstants.FIRST_TAB)
        assert show_mine_tab_name == Config.data.get_data_task_module(CRMTaskModuleConstants.SECOND_TAB)
        assert today_tab_name == Config.data.get_data_task_module(CRMTaskModuleConstants.THIRD_TAB)
        assert this_week_tab_name == Config.data.get_data_task_module(CRMTaskModuleConstants.FOURTH_TAB)
        assert history_tab_name == Config.data.get_data_task_module(CRMTaskModuleConstants.FIFTH_TAB)
