from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Change_Password import \
    ChangePasswordTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Check_Password import \
    CheckPasswordTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Create_Filter import CreateFilterTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Download_Documents_Client_Module import \
    DownloadDocumentsClientModule
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Credit_In import CreditInTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Credit_Out import CreditOutTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Mass_Assign import MassAssignTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Mass_Edit import MassEditTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Searching_Clients import \
    SearchingClientsTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Send_SMS_Clients_Module import \
    SendSMSClientsModule
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Transfer_Between_Ta import \
    TransferBetweenTa
from src.test.python.ui.automation.implementation.crm.tests_document_module.Test_Document_Module import DocumentModule
from src.test.python.ui.automation.implementation.crm.tests_document_module.Test_Tab_Document_Module import \
    TabDocumentModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Actions import ActionsTask
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Add_New_Task_Calendar_View import \
    AddNewTaskCalendarView
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Calendar_View import CalendarView
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Event import AddEventTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Delete import MassDeleteTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Edit import MassEditTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Mass_Sms import MassSmsTaskModule
from src.test.python.ui.automation.implementation.crm.tests_tasks_module.Test_Tab_Task_Module import TabTasksModuleCRM


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

    def run_perform_searching_crm(self):
        SearchingClientsTestCRM()

    def run_perform_create_filter_crm(self):
        CreateFilterTestCRM()

    def run_perform_mass_edit_clients_module(self):
        MassEditTestCRM()

    def run_perform_mass_assigned_to_clients_module(self):
        MassAssignTestCRM()

    def run_perform_send_sms(self):
        SendSMSClientsModule()

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
        ActionsTask()

    def run_create_delete_document(self):
        DocumentModule()

    def run_check_tabs(self):
        TabDocumentModule()
