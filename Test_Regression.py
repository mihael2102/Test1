from src.test.python.ui.automation.implementation.crm.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.Test_Change_Password import ChangePasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Check_Password import CheckPasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Create_Filter import CreateFilterTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Mass_Assign import MassAssignTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Mass_Edit import MassEditTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Searching_Clients import TestSearchingClientsTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Transfer_Between_Ta import TransferBetweenTa


class TestRegression(object):

    def run_transfer_between_ta_crm(self):
        TransferBetweenTa()

    def run_check_password_crm(self):
        CheckPasswordTestCRM()

    def run_change_password_crm(self):
        ChangePasswordTestCRM()

    def run_add_interaction_crm(self):
        AddInteraction()

    def run_perform_searching_crm(self):
        TestSearchingClientsTestCRM()

    def run_perform_create_filter_crm(self):
        CreateFilterTestCRM()

    def run_perform_mass_edit_clients_module(self):
        MassEditTestCRM()

    def run_perform_mass_assigned_to_clients_module(self):
        MassAssignTestCRM()
