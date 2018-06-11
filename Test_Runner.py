import pytest

from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.automation.implementation.ca.Test_Change_Password import ChangePasswordTestCA
from src.test.python.ui.automation.implementation.ca.Test_Download_Documents import DownloadDocumentsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Make_Deposit import DepositTestCa
from src.test.python.ui.automation.implementation.ca.Test_Make_Transfer_Funds import TransferFundsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Make_Withdraw import WithdrawTestCA
from src.test.python.ui.automation.implementation.ca.Test_Personal_Details_Update import PersonalDetailsUpdateTestCA
from src.test.python.ui.automation.implementation.ca.Test_SignUp import SignUpTest
from src.test.python.ui.automation.implementation.ca.Test_Support_Ticket import CreateSupportTicketTestCa
from src.test.python.ui.automation.implementation.crm.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.Test_Change_Password import ChangePasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Check_Password import CheckPasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Credit_In import CreditInTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Credit_Out import CreditOutTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Deposit import DepositTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Transfer_Between_Ta import TransferBetweenTa


class TestRunner(BaseTest):

    @pytest.mark.run(order=1)
    def run_sign_up(self):
        SignUpTest().test_check_sign_up()

    @pytest.mark.run(order=2)
    def run_live_accounts(self):
        live_accounts = AddNewLiveAccountTestCA()
        live_accounts.test_check_add_live_account_eur_currency()
        live_accounts.test_check_add_live_account_cad_currency()
        live_accounts.test_check_add_live_account_gbr_currency()
        live_accounts.test_check_add_live_account_jpy_currency()

    @pytest.mark.run(order=3)
    def run_demo_accounts(self):
        demo_accounts = AddDemoAccountsTestCA()
        demo_accounts.test_check_add_demo_account_usd_currency()
        demo_accounts.test_check_add_demo_account_eur_currency()
        demo_accounts.test_check_add_demo_account_gbr_currency()
        demo_accounts.test_check_add_demo_account_cad_currency()

    @pytest.mark.run(order=4)
    def run_create_ticket(self):
        create_ticket = CreateSupportTicketTestCa()
        create_ticket.test_create_ticket()

    @pytest.mark.run(order=5)
    def run_deposit_ca(self):
        deposit_ca = DepositTestCa()
        deposit_ca.test_make_deposit_from_ca()

    @pytest.mark.run(order=6)
    def run_withdraw(self):
        withdraw = WithdrawTestCA()
        withdraw.test_make_withdraw_ca()

    @pytest.mark.run(order=7)
    def run_transfer_funds(self):
        transfer = TransferFundsTestCA()
        transfer.test_make_transfer_funds()

    @pytest.mark.run(order=8)
    def run_upload_documents(self):
        upload_documents = DownloadDocumentsTestCA()
        upload_documents.test_make_dowload_documents()

    @pytest.mark.run(order=9)
    def run_upload_documents(self):
        upload_documents = DownloadDocumentsTestCA()
        upload_documents.test_make_dowload_documents()

    @pytest.mark.run(order=10)
    def run_change_password(self):
        change_password = ChangePasswordTestCA()
        change_password.test_change_password_from_ca()

    @pytest.mark.run(order=11)
    def run_client_update(self):
        client_update = PersonalDetailsUpdateTestCA()
        client_update.test_perform_client_update_from_CA()
        client_update.test_perform_client_update_from_CRM()

    @pytest.mark.run(order=12)
    def run_client_update(self):
        client_update = PersonalDetailsUpdateTestCA()
        client_update.test_perform_client_update_from_CA()
        client_update.test_perform_client_update_from_CRM()

    @pytest.mark.run(order=13)
    def run_deposit_crm(self):
        deposit_crm = DepositTestCRM()
        deposit_crm.test_make_deposit()

    @pytest.mark.run(order=14)
    def test_run_credit_in_crm(self):
        credit_in_crm = CreditInTestCRM()
        credit_in_crm.test_make_credit_in_crm()

    @pytest.mark.run(order=15)
    def run_credit_out_crm(self):
        credit_out_crm = CreditOutTestCRM()
        credit_out_crm.test_make_credit_out_crm()

    @pytest.mark.run(order=16)
    def test_run_transfer_between_ta_crm(self):
        transfer_between = TransferBetweenTa()
        transfer_between.test_make_transfer_between_ta()

    @pytest.mark.run(order=17)
    def run_check_password_crm(self):
        check_password = CheckPasswordTestCRM()
        check_password.test_check_password_crm()

    @pytest.mark.run(order=18)
    def run_change_password_crm(self):
        change_password = ChangePasswordTestCRM()
        change_password.test_make_change_password_from_crm()

    @pytest.mark.run(order=19)
    def run_change_password_crm(self):
        add_interaction = AddInteraction()
        add_interaction.test_add_interaction()
