from src.test.python.ui.automation.implementation.crm.test_my_dashboard.Test_My_Dashboard_Actions import \
    MyDashboardActionsTest
from src.test.python.ui.automation.implementation.crm.tests_affiliates_module.Test_Affiliates_Module import \
    AffiliateModule
from src.test.python.ui.automation.implementation.crm.tests_audit_logs_module.Test_Audit_Logs import AuditLogs
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Change_Password import \
    ChangePasswordTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Check_Password import \
    CheckPasswordTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Download_Documents_Client_Module import \
    DownloadDocumentsClientModule
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Credit_In import CreditInTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Credit_Out import CreditOutTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Withdraw import WithdrawTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Mass_Assign import MassAssignTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Mass_Edit import MassEditTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Send_Email import SendEmailTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Send_SMS_Clients_Module import \
    SendSMSClientsModuleTest
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Transfer_Between_Ta import \
    TransferBetweenTa
from src.test.python.ui.automation.implementation.crm.tests_document_module.Test_Document_Module import CreateDocument

from src.test.python.ui.automation.implementation.crm.tests_document_module.Test_Tab_Document_Module import \
    TabDocumentModule
from src.test.python.ui.automation.implementation.crm.tests_financial_transactions.Test_Tab_Financial_Transaction_Module import \
    TabFinancialTransaction
from src.test.python.ui.automation.implementation.crm.tests_help_desk_module.Test_Help_Desk_Module import HelpDeskTest
from src.test.python.ui.automation.implementation.crm.tests_help_desk_module.Test_Tab_Help_Desk import TabHelpDeskTest
from src.test.python.ui.automation.implementation.crm.tests_leads_module.Test_Import_Lead import ImportLeadTest
from src.test.python.ui.automation.implementation.crm.tests_leads_module.Test_Leads_Module import LeadModule
from src.test.python.ui.automation.implementation.crm.tests_leads_module.Test_Tab_Leads_Module import TabLeadsModuleCRM
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Email import MassEmailTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Tasks_Actions import ActionsTaskModuleTest
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Add_New_Task_Calendar_View import \
    AddNewTaskCalendarView
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Calendar_View import CalendarView
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Event import AddEventTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Delete import MassDeleteTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Edit import MassEditTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Sms import MassSmsTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Tab_Task_Module import TabTasksModuleCRM
from src.test.python.ui.automation.implementation.crm.tests_trading_account.Test_Tab_Trading_Account_Module import \
    TradingAccountTest
from src.test.python.ui.automation.implementation.crm.user_management.Test_Create_User import CreateUserTest


class TestRegression(object):

    def test_run_credit_in_crm(self):
        CreditInTestCRM()

    def test_run_credit_out_crm(self):
        CreditOutTestCRM()

    def run_transfer_between_ta_crm(self):
        TransferBetweenTa()

    def run_check_password_crm(self):
        CheckPasswordTestCRM()

    def run_change_password_crm(self):
        ChangePasswordTestCRM()

    def run_add_interaction_crm(self):
        AddInteraction()

    def create_user(self):
        CreateUserTest()

    def run_perform_mass_edit_clients_module(self):
        MassEditTestCRM()

    def run_withdraw_clients_module(self):
        WithdrawTestCRM()

    def run_perform_mass_assigned_to_clients_module(self):
        MassAssignTestCRM()

    def run_perform_send_sms(self):
        SendSMSClientsModuleTest()

    def run_perform_upload_document_client_module(self):
        DownloadDocumentsClientModule()

    def run_perform_check_tabs(self):
        TabTasksModuleCRM()

    def run_perform_add_event(self):
        AddEventTaskModule()

    def run_perform_calendar_view(self):
        CalendarView()

    def run_perform_mass_edit_task_module(self):
        MassEditTaskModule()

    def run_perform_mass_delete_task_module(self):
        MassDeleteTaskModule()

    def run_mass_sms_task_module(self):
        MassSmsTaskModule()

    def run_add_new_task(self):
        AddNewTaskCalendarView()

    def run_actions_task_module(self):
        ActionsTaskModuleTest()

    def run_mass_email_task_module(self):
        MassEmailTaskModule()

    def run_create_delete_document(self):
        CreateDocument()

    def run_check_tabs(self):
        TabDocumentModule()

    def run_check_lead_test(self):
        LeadModule()

    def run_import_lead(self):
        ImportLeadTest()

    def run_tab_lead_test(self):
        TabLeadsModuleCRM()

    def run_check_tab_financial_transaction(self):
        TabFinancialTransaction()

    def run_check_my_dashboard_test(self):
        MyDashboardActionsTest()

    def run_check_audit_logs_test(self):
        AuditLogs()

    def run_send_email_clients_module(self):
        SendEmailTestCRM()

    def run_help_desk_test(self):
        HelpDeskTest()

    def run_tab_help_desk(self):
        TabHelpDeskTest()

    def run_affiliate_module(self):
        AffiliateModule()

    def run_trading_account_module(self):
        TradingAccountTest()
