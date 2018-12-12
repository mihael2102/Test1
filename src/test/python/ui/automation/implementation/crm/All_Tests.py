from src.main.python.ui.crm.model.mt4.password.MT4UpdatePasswordModule import MT4UpdatePasswordModule
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsPage import TradingAccountsPage

from src.test.python.ui.automation.utils.preconditions.affiliates.Affiliates_Precondition import AffiliatesPrecondition
from src.test.python.ui.automation.utils.preconditions.filter.FilterPrecondition import FilterPrecondition
from src.main.python.ui.crm.model.mt4.password.MT4CheckPasswordModule import MT4CheckPasswordModule
from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.mt4.credit_in.MT4CreditInModule import MT4CreditInModule
from src.test.python.ui.automation.utils.preconditions.credit_in.Credit_In_Precondition import \
    CreditInPrecondition
import time
from src.main.python.ui.crm.model.modules.client_modules.client_deposit.CRMClientDeposit import CRMClientDeposit
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition
from src.test.python.ui.automation.utils.preconditions.task_module.EventPrecondition import EventPrecondition
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.main.python.ui.crm.model.side_bar.create_event.CreateEvent import CreateEvent
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants

class AllTest(BaseTest):

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def setUp(self):
        super(AllTest, self).setUp()
        self.lead1 = self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)
        self.lead2 = self.load_lead_from_config(LeadsModuleConstants.SECOND_LEAD_INFO)
        self.client1 = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)

    def all_test(self):
        # CLIENT FILTER TEST
        try:
            Logging().reportDebugStep(self, "Create client filter")

            clients_module_page = CRMLoginPage(self.driver) \
                .open_first_tab_page_one(self.config.get_value('url')) \
                .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                           self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                           self.config.get_data_client(TestDataConstants.OTP_SECRET))

            FilterPrecondition(self.driver, self.config).create_filter_clients_module()

            first_name__column = clients_module_page.get_first_name_column()
            second_name_column = clients_module_page.get_second_name_column()
            third_name__column = clients_module_page.get_third_name_column()
            fourth_name_column = clients_module_page.get_fourth_name_column()
            fifth_name_column = clients_module_page.get_fifth_name_column()
            sixth_name_column = clients_module_page.get_sixth_name_column()
            seventh_name_column = clients_module_page.get_seventh_name_column()
            eighth_name_column = clients_module_page.get_eighth_name_column()
            ninth_name_column = clients_module_page.get_ninth_name_column()
            tenth_name_column = clients_module_page.get_tenth_name_column()
            eleventh_name_column = clients_module_page.get_eleventh_name_column()

            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                               CRMConstants.FIRST_COLUMN) == first_name__column
            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                               CRMConstants.SECOND_COLUMN) == second_name_column
            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                               CRMConstants.THIRD_COLUMN) == third_name__column
            assert CRMConstants.FOURTH_COLUMN_OTHER_TYPE == fourth_name_column
            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIFTH_COLUMN) == fifth_name_column
            assert CRMConstants.SIXTH_COLUMN_OTHER_TYPE == sixth_name_column
            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                               CRMConstants.SEVENTH_COLUMN) == seventh_name_column
            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                               CRMConstants.EIGHTH_COLUMN) == eighth_name_column
            assert CRMConstants.NINTH_COLUMN_OTHER_TYPE == ninth_name_column
            assert CRMConstants.TENTH_COLUMN_OTHER_TYPE == tenth_name_column
            assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                               CRMConstants.ELEVENTH_COLUMN) == eleventh_name_column

        except Exception:
            Logging().reportDebugStep(self, "Test create client filter is failed")

        # # DOCUMENT FILTER TEST
        try:
            Logging().reportDebugStep(self, "Create documents filter")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            FilterPrecondition(self.driver, self.config).create_filter_documents_module()

            documents_module_page = DocumentsPage(self.driver)
            first_name__column = documents_module_page.get_first_name_column()
            second_name_column = documents_module_page.get_second_name_column()
            third_name__column = documents_module_page.get_third_name_column()
            fourth_name_column = documents_module_page.get_fourth_name_column()

            assert self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                        DocumentModuleConstants.FIRST_COLUMN) == first_name__column
            assert self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                        DocumentModuleConstants.SECOND_COLUMN) == second_name_column
            assert self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                        DocumentModuleConstants.THIRD_COLUMN) == third_name__column
            self.assertEqual(fourth_name_column, DocumentModuleConstants.FOURTH_COLUMN_TEXT,
                             "Filter columns are different in Documents module")

        except Exception:
            Logging().reportDebugStep(self, "Test create documents filter is failed")

        # LEAD FILTER TEST
        try:
            Logging().reportDebugStep(self, "Create lead filter")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            if global_var.current_brand_name == "marketsplus":
                FilterPrecondition(self.driver, self.config).create_filter_leads_module_new()

                leads_module_page = LeadsModule(self.driver)

                first_name__column = leads_module_page.get_first_name_column()
                second_name_column = leads_module_page.get_second_name_column()
                third_name__column = leads_module_page.get_third_name_column()
                fourth_name_column = leads_module_page.get_fourth_name_column()
                fifth_name_column = leads_module_page.get_fifth_name_column()
                sixth_name_column = leads_module_page.get_sixth_name_column()
                seventh_name_column = leads_module_page.get_seventh_name_column()

            else:

                FilterPrecondition(self.driver, self.config).create_filter_leads_module()

                leads_module_page = LeadsModule(self.driver)

                first_name__column = leads_module_page.get_first_name_column()
                second_name_column = leads_module_page.get_second_name_column()
                third_name__column = leads_module_page.get_third_name_column()
                fourth_name_column = leads_module_page.get_fourth_name_column()
                fifth_name_column = leads_module_page.get_fifth_name_column()
                sixth_name_column = leads_module_page.get_sixth_name_column()
                seventh_name_column = leads_module_page.get_seventh_name_column()
                eighth_name_column = leads_module_page.get_eighth_name_column()

            assert self.config.get_data_lead_info_from_json(LeadsModuleConstants.FIRST_COLUMN) == first_name__column
            assert LeadsModuleConstants.LAST_NAME_COLUMN_TEXT == second_name_column
            assert self.config.get_data_lead_info_from_json(LeadsModuleConstants.THIRD_COLUMN) == third_name__column
            assert LeadsModuleConstants.ASSIGNED_TO_COLUMN_TEXT == fourth_name_column
            assert self.config.get_data_lead_info_from_json(LeadsModuleConstants.FIFTH_COLUMN) == fifth_name_column
            assert self.config.get_data_lead_info_from_json(LeadsModuleConstants.SIXTH_COLUMN) == sixth_name_column
            assert self.config.get_data_lead_info_from_json(LeadsModuleConstants.SEVENTH_COLUMN) == seventh_name_column
            if global_var.current_brand_name != "marketsplus":
                assert self.config.get_data_lead_info_from_json(LeadsModuleConstants.EIGHT_COLUMN) == eighth_name_column

        except Exception:
            Logging().reportDebugStep(self, "Test create lead filter is failed")

        # HELP DESK FILTER TEST
        try:
            Logging().reportDebugStep(self, "Create help desk filter")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            FilterPrecondition(self.driver, self.config).create_filter_help_desk()

            help_desk_module_page = HelpDeskPage(self.driver)

            first_name__column = help_desk_module_page.get_first_name_column()
            second_name_column = help_desk_module_page.get_second_name_column()
            third_name__column = help_desk_module_page.get_third_name_column()
            fourth_name_column = help_desk_module_page.get_fourth_name_column()
            fifth_name_column = help_desk_module_page.get_fifth_name_column()
            sixth_name_column = help_desk_module_page.get_sixth_name_column()
            seventh_name_column = help_desk_module_page.get_seventh_name_column()
            eighth_name_column = help_desk_module_page.get_eighth_name_column()
            tenth_name_column = help_desk_module_page.get_tenth_name_column()
            eleventh_name_column = help_desk_module_page.get_eleventh_name_column()

            assert self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS,
                                                  HelpDeskConstants.FIRST_COLUMN) == first_name__column
            assert HelpDeskConstants.TITLE == second_name_column
            assert self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS,
                                                  HelpDeskConstants.THIRD_COLUMN) == third_name__column
            assert HelpDeskConstants.ASSIGNED_TO_TYPE == fourth_name_column
            assert HelpDeskConstants.STATUS == fifth_name_column
            assert self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS,
                                                  HelpDeskConstants.SIXTH_COLUMN) == sixth_name_column
            assert HelpDeskConstants.CATEGORY == seventh_name_column
            assert self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS,
                                                  HelpDeskConstants.EIGHTH_COLUMN) == eighth_name_column
            assert HelpDeskConstants.DESCRIPTION == tenth_name_column
            assert HelpDeskConstants.ACCOUNT_NAME == eleventh_name_column

        except Exception:
            Logging().reportDebugStep(self, "Test create help desk filter is failed")

        # TRADING ACCOUNT FILTER TEST
        try:
            Logging().reportDebugStep(self, "Create trading account filter")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            FilterPrecondition(self.driver, self.config).create_filter_trading_account_module()

            trading_account_module_page = TradingAccountsPage(self.driver)

            first_name__column = trading_account_module_page.get_first_name_column()
            second_name_column = trading_account_module_page.get_second_name_column()
            third_name__column = trading_account_module_page.get_third_name_column()
            fourth_name_column = trading_account_module_page.get_fourth_name_column()
            fifth_name_column = trading_account_module_page.get_fifth_name_column()
            sixth_name_column = trading_account_module_page.get_sixth_name_column()
            seventh_name_column = trading_account_module_page.get_seventh_name_column()
            eighth_name_column = trading_account_module_page.get_eighth_name_column()

            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.FIRST_COLUMN)[:-2],
                             first_name__column, "Name of the column is wrong")
            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.SECOND_COLUMN),
                             second_name_column, "Name of the column is wrong")
            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.THIRD_COLUMN),
                             third_name__column, "Name of the column is wrong")
            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.FOURTH_COLUMN),
                             fourth_name_column, "Name of the column is wrong")
            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.FIFTH_COLUMN),
                             fifth_name_column, "Name of the column is wrong")
            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.SIXTH_COLUMN),
                             sixth_name_column, "Name of the column is wrong")
            self.assertEqual(self.config.get_data_columns_trading_module(TradingAccountConstants.SEVENTH_COLUMN),
                             seventh_name_column, "Name of the column is wrong")
            self.assertEqual(
                self.config.get_data_columns_trading_module(TradingAccountConstants.EIGHTH_COLUMN)[:-2],
                eighth_name_column, "Name of the column is wrong")

        except Exception:
            Logging().reportDebugStep(self, "Test create trading account filter is failed")

        # SEARCHING LEAD MODULES TEST

        try:
            Logging().reportDebugStep(self, "Searching lead modules")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            LeadPrecondition(self.driver, self.config).create_lead(self.lead1)

            CRMHomePage(self.driver)\
                .refresh_page()\
                .open_client_module()

            lead_module = CRMHomePage(self.driver)\
                .open_lead_module()

            lead_module.select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))

            lead_module.perform_searching_lead_module(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_ASSIGNED_TO),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LEAD_SOURCE),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LEAD_STATUS),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE))

            result_count = lead_module.get_results_count()
            self.assertEqual(1, result_count, "The number of expected search results does not match")

        except Exception:
            Logging().reportDebugStep(self, "Test searching lead modules is failed")

        # CREATE LEAD TEST

        try:
            Logging().reportDebugStep(self, "Create lead")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
            self.verify_lead(self.lead1)

        except Exception:
            Logging().reportDebugStep(self, "Test create lead is failed")

        # EDIT LEAD TEST

        try:
            Logging().reportDebugStep(self, "Edit lead")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
            self.verify_lead(self.lead1)
            LeadPrecondition(self.driver, self.config).edit_lead_profile(self.lead2)
            self.verify_lead(self.lead2)

        except Exception:
            Logging().reportDebugStep(self, "Test edit lead is failed")

        # CONVERT LEAD TEST

        try:
            Logging().reportDebugStep(self, "Convert lead")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
            lead_view_profile_page = LeadViewInfo(self.driver)

            lead_view_profile_page.open_convert_lead_module() \

            if global_var.current_brand_name == "mpcrypto":
                ConvertLeadModule(self.driver).perform_convert_lead(
                    self.client1[LeadsModuleConstants.FIRST_NAME],
                    self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                    self.client1[LeadsModuleConstants.EMAIL],
                    self.client1[LeadsModuleConstants.PHONE],
                    self.client1[LeadsModuleConstants.BIRTHDAY],
                    self.client1[LeadsModuleConstants.CITIZENSHIP],
                    self.client1[LeadsModuleConstants.STREET],
                    self.client1[LeadsModuleConstants.POSTAL_CODE],
                    self.client1[LeadsModuleConstants.CITY],
                    self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                    self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD_BCH],
                    self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                    self.client1[LeadsModuleConstants.BRAND],
                    self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                    self.client1[LeadsModuleConstants.PHONE_AREA_CODE])

            else:

                ConvertLeadModule(self.driver).perform_convert_lead(
                    self.client1[LeadsModuleConstants.FIRST_NAME],
                    self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                    self.client1[LeadsModuleConstants.EMAIL],
                    self.client1[LeadsModuleConstants.PHONE],
                    self.client1[LeadsModuleConstants.BIRTHDAY],
                    self.client1[LeadsModuleConstants.CITIZENSHIP],
                    self.client1[LeadsModuleConstants.STREET],
                    self.client1[LeadsModuleConstants.POSTAL_CODE],
                    self.client1[LeadsModuleConstants.CITY],
                    self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                    self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                    self.client1[LeadsModuleConstants.BRAND],
                    self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                    self.client1[LeadsModuleConstants.PHONE_AREA_CODE])


            convert_verified = False
            try:
                confirmation_message = lead_view_profile_page.get_confirm_message_lead_view_profile()
                assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
                lead_view_profile_page.click_ok()
                convert_verified = True
            except TimeoutException:
                Logging().reportDebugStep(self, "Lead convert message was not picked up")
            if not convert_verified:
                lead_detail_view = LeadDetailViewInfo(self.driver)
                lead_detail_view.wait_element_to_be_clickable("//input[@name='Edit']")
                self.assertEqual(' yes ', lead_detail_view.get_exists_text(), "Lead is not at exists state")

        except Exception:
            Logging().reportDebugStep(self, "Test convert lead is failed")

        # SEARCHING CLIENT MODULES

        try:
            Logging().reportDebugStep(self, "Searching client")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

            if (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "swiftcfd") \
                    or (global_var.current_brand_name == "ptbanc"):
                    sleep(15)
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif global_var.current_brand_name == "4xfx":
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_C_NEW),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif (global_var.current_brand_name == "safemarkets") or (global_var.current_brand_name == "uft") or (global_var.current_brand_name == "q8"):
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_NEW),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif global_var.current_brand_name == "goldenmarkets":
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif global_var.current_brand_name == "ptbanc":
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))
            else:
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            # TODO: verify that only one client was found

            ClientsPage(self.driver).perform_scroll_up()
            ClientsPage(self.driver).open_client_id()

            first_name_crm = ClientProfilePage(self.driver).get_first_name()
            last_name_crm = ClientProfilePage(self.driver).get_last_name()
            email = ClientProfilePage(self.driver).get_email_text()

            assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME) == first_name_crm
            assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME) == last_name_crm
            assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL) == email

        except Exception:

            Logging().reportDebugStep(self, "Test searching client is failed")


        # ADD INTERACTION TEST
        try:
            Logging().reportDebugStep(self, "Add interaction")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

            if (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "swiftcfd"):
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif global_var.current_brand_name == "4xfx":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_C_NEW),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif (global_var.current_brand_name == "safemarkets") or (global_var.current_brand_name == "uft"):
                    ClientsPage(self.driver).perform_searching(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_NEW),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif global_var.current_brand_name == "q8":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            elif global_var.current_brand_name == "goldenmarkets":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))
            else:
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

            ClientsPage(self.driver).perform_scroll_up()
            ClientsPage(self.driver).open_client_id()

            SidebarModules(self.driver)\
                .open_create_event_module() \

            if global_var.current_brand_name == "4xfx":
                CreateEvent(self.driver).create_event(self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_STATUS),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TYPE_TASK),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DURATION),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TIME),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DATE),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_ASSIGN_TO),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_PRIORITY),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DESCRIPTION))
            else:

                CreateEvent(self.driver).create_event(self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_STATUS),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TYPE),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DURATION),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TIME),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DATE),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_ASSIGN_TO),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_PRIORITY),
                              self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DESCRIPTION))

            confirmation_message = ClientsPage(self.driver).get_confirm_message()
            assert confirmation_message == CRMConstants.INTERACTION_SUCCESSFULLY
            ClientsPage(self.driver).click_ok()

        except Exception:

            Logging().reportDebugStep(self, "Test add interaction is failed")

        # INTERACTIONS SEARCH TEST

        try:
            Logging().reportDebugStep(self, "Interaction search")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            res_count = CRMHomePage(self.driver)\
                .open_task_module()\
                .open_show_all_tab()\
                .find_event_by_subject(self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TYPE))\
                .get_results_count()

            self.assertGreaterEqual(res_count, 1)

        except Exception:
            Logging().reportDebugStep(self, "Test interaction search is failed")


        # ADD EVENT TEST

        try:
            Logging().reportDebugStep(self, "Add event")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            EventPrecondition(self.driver, self.config).create_first_event()

        except Exception:
            Logging().reportDebugStep(self, "Test add event is failed")


        # EDIT EVENT TEST

        try:
            Logging().reportDebugStep(self, "Edit event")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            EventPrecondition(self.driver, self.config).edit_first_event()
        except Exception:
            Logging().reportDebugStep(self, "Test edit event is failed")

        # OPEN TRADING ACCOUNT TEST

        try:
            Logging().reportDebugStep(self, "Open trading account")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            TradingAccountPrecondition(self.driver, self.config) \
                .add_demo_account_from_crm()
            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)

        except Exception:
            Logging().reportDebugStep(self, "Test open trading account is failed")

        # CHECK CLIENT PASSWORD CRM

        try:
            Logging().reportDebugStep(self, "Check client password crm")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

            SidebarModules(self.driver)\
                .open_check_client_password() \
                .set_password_to_check(self.config.get_value(TestDataConstants.CLIENT_ONE,
                                                             LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
                .click_check()

            confirmation_message = ClientsPage(self.driver).get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.CUSTOMER_PASSWORD_VALID_MESSAGE)
            ClientsPage(self.driver).click_ok()

        except Exception:
            Logging().reportDebugStep(self, "Test check client password crm is failed")

        # CHECK MT4 PASSWORD CRM
        try:
            Logging().reportDebugStep(self, "Check mt4 password crm")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            ClientProfilePage(self.driver).perform_scroll_up().open_mt4_actions(CRMConstants.CHECK_PASSWORD)

            MT4CheckPasswordModule(self.driver).select_account(account_number) \
                .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                            LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
                .click_check_button()

            message = ClientProfilePage(self.driver).get_confirm_message()
            ClientProfilePage(self.driver).click_ok()

            self.assertEqual(message, CRMConstants.MT4_PASSWORD_VALID_MESSAGE)

        except Exception:
            Logging().reportDebugStep(self, "Test check mt4 password crm is failed")

        # CHANGE CLIENTS PASSWORD CRM

        try:
            Logging().reportDebugStep(self, "Change client password crm")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
            # change the password to a new password
            SidebarModules(self.driver) \
                .open_change_client_password() \
                .set_password(self.config.get_value(TestDataConstants.CLIENT_ONE,
                                                    TestDataConstants.NEW_PASSWORD)) \
                .click_change()

            message_confirm = ClientProfilePage(self.driver).get_confirm_message()
            ClientProfilePage(self.driver).click_ok()

            self.assertEqual(message_confirm, CRMConstants.CRM_CLIENT_AREA_PASSWORD_CHANGE)

            # check the new password
            ClientProfilePage(self.driver).refresh_page()

            SidebarModules(self.driver) \
                .open_check_client_password() \
                .set_password_to_check(self.config.get_value(TestDataConstants.CLIENT_ONE,
                                                             TestDataConstants.NEW_PASSWORD)) \
                .click_check()

            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.CUSTOMER_PASSWORD_VALID_MESSAGE)
            ClientProfilePage(self.driver).click_ok()

            # change the password back to the original password
            ClientProfilePage(self.driver).refresh_page()

            SidebarModules(self.driver) \
                .open_change_client_password() \
                .set_password(self.config.get_value(TestDataConstants.CLIENT_ONE,
                                                    LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
                .click_change()

            message_confirm = ClientProfilePage(self.driver).get_confirm_message()
            ClientProfilePage(self.driver).click_ok()

            self.assertEqual(message_confirm, CRMConstants.CRM_CLIENT_AREA_PASSWORD_CHANGE)

        except Exception:
            Logging().reportDebugStep(self, "Test change client password crm is failed")

        # CHANGE MT4 PASSWORD CRM
        try:
            Logging().reportDebugStep(self, "Change mt4 password")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            # change the password to a new password
            ClientProfilePage(self.driver).perform_scroll_up().open_mt4_actions(CRMConstants.CHANGE_PASSWORD)

            MT4UpdatePasswordModule(self.driver).select_account(account_number) \
                .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.NEW_PASSWORD)) \
                .click_check_button()

            message_confirm = ClientProfilePage(self.driver).get_confirm_message()
            ClientProfilePage(self.driver).click_ok()

            self.assertEqual(message_confirm, CRMConstants.PASSWORD_CHANGE)

            # check the new password
            ClientProfilePage(self.driver).refresh_page().open_mt4_actions(CRMConstants.CHECK_PASSWORD)

            MT4CheckPasswordModule(self.driver).select_account(account_number) \
                .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.NEW_PASSWORD)) \
                .click_check_button()

            message_confirm = ClientProfilePage(self.driver).get_confirm_message()
            ClientProfilePage(self.driver).click_ok()

            self.assertEqual(message_confirm, CRMConstants.MT4_PASSWORD_VALID_MESSAGE)

            # change the password back to the original password
            ClientProfilePage(self.driver).refresh_page().open_mt4_actions(CRMConstants.CHANGE_PASSWORD)

            MT4UpdatePasswordModule(self.driver).select_account(account_number) \
                .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                            LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
                .click_check_button()

            message_confirm = ClientProfilePage(self.driver).get_confirm_message()
            ClientProfilePage(self.driver).click_ok()
            self.assertEqual(message_confirm, CRMConstants.PASSWORD_CHANGE)

        except Exception:
            Logging().reportDebugStep(self, "Test change mt4 password is failed")

        # DEPOSIT CRM
        try:
            Logging().reportDebugStep(self, "Create deposit")
            client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            CRMHomePage(self.driver).open_client_module()\
                                    .select_filter(self.config.get_value(
                                                                TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                                    .find_client_by_email(client1[LeadsModuleConstants.EMAIL])

            # Create LIVE account for client using MT4 Actions
            crm_client_profile = ClientProfilePage(self.driver)
            crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

            if (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "newforexstaging"):
                MT4CreateAccountModule(self.driver) \
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                    .click_ok()

            elif (global_var.current_brand_name == "q8"):
                MT4CreateAccountModule(self.driver)\
                    .create_account_with_platform(
                    self.config.get_value(TestDataConstants.TRADING_PLATFORMS, TestDataConstants.TRADING_PLATFORM_MT4),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                    .click_ok()

            elif (global_var.current_brand_name == "axa_markets"):
                MT4CreateAccountModule(self.driver)\
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_400)) \
                    .click_ok()

            elif (global_var.current_brand_name == "xtraderfx"):
                MT4CreateAccountModule(self.driver)\
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_EUR),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_EUR),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                    .click_ok()

            else:
                MT4CreateAccountModule(self.driver) \
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE))\
                    .click_ok()

            # Get account number to make deposit in future
            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            # Make deposit for account number using MT4 Actions
            crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.DEPOSIT)

            MT4DepositModule(self.driver).make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                                       CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                                       CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT)

            # Check confirmation message
            confirmation_message = crm_client_profile.get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY)

            # Close popup
            crm_client_profile.click_ok()\
                              .refresh_page()

            deposit_amount_text = crm_client_profile.click_trading_accounts_tab() \
                                                    .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)

            self.assertEqual(
                        CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT, deposit_amount_text, "Wrong deposit sum is displayed")

        except Exception:
            Logging().reportDebugStep(self, "Test create deposit is failed")

        # DEPOSIT FOR CLIENT CRM

        try:
            Logging().reportDebugStep(self, "Create deposit for client")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

            # Get account number to make deposit in future. And get initial amount
            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            # Use when you need to compare amount before and after deposit
            # amount_initial = crm_client_profile.get_initial_amount()

            ClientProfilePage(self.driver) \
                .perform_scroll_up() \
                .open_deposit_for_client_in_menu() \
                .fill_client_deposit_pop(account_number)

            # Check that CLIENT DEPOSIT CONFIRMATION page is closed and popup is still displayed
            self.assertTrue(CRMClientDeposit(self.driver).is_client_deposit_confirmation_page_not_displayed(),
                            "CLIENT DEPOSIT CONFIRMATION page is still displayed. But Payment Frame is expected")

            self.assertEqual(CRMConstants.TITLE_OF_CLIENT_DEPOSIT_POPUP,
                             CRMClientDeposit(self.driver).client_deposit_popup_title_text(),
                             "Client deposit popup is not displayed, but should")
        except Exception:
            Logging().reportDebugStep(self, "Test create deposit for client is failed")

        # CREDIT IN
        try:
            Logging().reportDebugStep(self, "Make credit in")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            CreditInPrecondition(self.driver, self.config).add_live_account_in_crm().click_ok()

            # Take number of account
            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            ClientProfilePage(self.driver).perform_scroll_up().open_mt4_actions(CRMConstants.CREDIT_IN)

            MT4CreditInModule(self.driver).make_credit_in(account_number, CRMConstants.AMOUNT_CREDIT_IN,
                                               CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                                               CRMConstants.CREDIT_IN_COMMENT) \
                .click_ok() \
                .refresh_page()
            time.sleep(3)
            MT4CreditInModule(self.driver).refresh_page()
            # Check the Credit In amount
            credit_in_amount = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .get_amount_of_credit_in()     # Get amount from block 'Trading Accounts'

            time.sleep(3)
            MT4CreditInModule(self.driver).refresh_page()
            self.assertEqual(CRMConstants.AMOUNT_CREDIT_IN, credit_in_amount[1:], "Wrong Credit In amount is displayed")

        except Exception:
            Logging().reportDebugStep(self, "Test make credit in is failed")

        # EDIT TRADING ACCOUNT

        try:
            Logging().reportDebugStep(self, "Edit trading account")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            TradingAccountPrecondition(self.driver, self.config) \
                .add_demo_account_from_crm()

            # Close pop up and update popup
            ClientProfilePage(self.driver).close_popup_new_trading_account()
            TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)

        except Exception:
            Logging().reportDebugStep(self, "Test edit trading account in is failed")

        # CREATE AFFILIATE
        try:
            Logging().reportDebugStep(self, "Create affiliate")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            AffiliatesPrecondition(self.driver, self.config).create_affiliate()

        except Exception:
            Logging().reportDebugStep(self, "Test create affiliate is failed")

        # CREATE TASK IN CALENDAR VIEW
        try:
            Logging().reportDebugStep(self, "Create task in calendar view")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            task_module = CRMHomePage(self.driver).open_task_module()

            calendar_module = task_module.open_calendar_view_module()

            calendar_module.add_new_task().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                        TaskModuleConstants.FIRST_EVENT_TYPE,
                                                        TaskModuleConstants.FIRST_DURATION,
                                                        CRMConstants.SECOND_DATE.strftime(
                                                            CRMConstants.SECOND_FORMAT_DATE),
                                                        CRMConstants.TIME_ZERO,
                                                        TaskModuleConstants.FIRST_ASSIGN_TO,
                                                        self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                            LeadsModuleConstants.FIRST_NAME],
                                                        self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                            LeadsModuleConstants.FIRST_NAME],
                                                        TaskModuleConstants.FIRST_PRIORITY,
                                                        TaskModuleConstants.DESCRIPTION_ADD_EVENT)

            assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT

            assert task_module.get_task_subject(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.FIRST_NAME]) == \
                   self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                       LeadsModuleConstants.FIRST_NAME]

        except Exception:
            Logging().reportDebugStep(self, "Test create task in calendar view is failed")


        # CHECK DAY TAB
        try:
            Logging().reportDebugStep(self, "Check day tab")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            calendar_module = CRMHomePage(self.driver)\
                .open_task_module() \
                .open_calendar_view_module() \
                .open_day_tab()

            current_day = calendar_module.get_current_date()
            day_of_week = calendar_module.get_day_of_week()

            assert current_day == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT)
            assert day_of_week == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT_DATE)

        except Exception:
            Logging().reportDebugStep(self, "Test check day tab is failed")
        # CHECK MONTH TAB

        try:
            Logging().reportDebugStep(self, "Check month tab")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            calendar_module = CRMHomePage(self.driver)\
                .open_task_module() \
                .open_calendar_view_module() \
                .open_month_tab()

            sun_day = calendar_module.get_sunday_text()
            mon_day = calendar_module.get_monday_text()
            tue_day = calendar_module.get_tuesday_text()
            wed_day = calendar_module.get_wednesday_text()
            thu_day = calendar_module.get_thursday_text()
            fri_day = calendar_module.get_friday_text()
            sat_day = calendar_module.get_saturday_text()

            assert sun_day == TaskModuleConstants.SUNDAY
            assert mon_day == TaskModuleConstants.MONDAY
            assert tue_day == TaskModuleConstants.TUESDAY
            assert wed_day == TaskModuleConstants.WEDNESDAY
            assert thu_day == TaskModuleConstants.THURSDAY
            assert fri_day == TaskModuleConstants.FRIDAY
            assert sat_day == TaskModuleConstants.SATURDAY

        except Exception:
            Logging().reportDebugStep(self, "Test check month tab is failed")
        # CHECK WEEK TAB

        try:
            Logging().reportDebugStep(self, "Check week tab")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            CRMHomePage(self.driver)\
                .open_task_module() \
                .open_calendar_view_module() \
                .open_week_tab() \
                # .perform_screen_shot()
        except Exception:
            Logging().reportDebugStep(self, "Test check week tab is failed")

        # CHECK ALL TAB FINANCIAL TRANSACTIONS
        try:
            Logging().reportDebugStep(self, "Check all tab FT")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            financial_transaction_module = CRMHomePage(self.driver).open_more_list_modules() \
                .select_financial_transactions_module_more_list(
                FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

            all_tab_name = financial_transaction_module.get_all_tab_text()
            credit_in_tab_name = financial_transaction_module.get_credit_in_tab_text()
            credit_out_name = financial_transaction_module.get_credit_out_tab_text()
            demo_accounts_name = financial_transaction_module.get_demo_accounts_transactions_tab_text()
            deposit_name = financial_transaction_module.get_deposits_tab_text()
            withdraw = financial_transaction_module.get_withdraw_tab_text()

            assert all_tab_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.FIRST_TAB)
            assert credit_in_tab_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.SECOND_TAB)
            assert credit_out_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.THIRD_TAB)
            assert demo_accounts_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.FOURTH_TAB)
            assert deposit_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.FIFTH_TAB)
            assert withdraw == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.SIX_TAB)

        except Exception:
            Logging().reportDebugStep(self, "Test check all tab FT is failed")

        # SEARCH BY COLUMN
        try:
            Logging().reportDebugStep(self, "Check search by column FT")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

            financial_transaction_list_page = CRMHomePage(self.driver) \
                                                    .select_financial_transactions_module_more_list(
                                                        FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)


            transaction_number = financial_transaction_list_page.get_transaction_id_by_position_from_list()
            client_name = financial_transaction_list_page.get_client_name_by_position_from_list()
            transaction_type_text = financial_transaction_list_page.get_transaction_type_by_position_from_list()

            try:
                modified_time = financial_transaction_list_page.get_modified_time_by_position_from_list()[:10] + " - " + \
                                                financial_transaction_list_page.get_modified_time_by_position_from_list()[:10]
            except NoSuchElementException:
                modified_time = None

            transaction_number_from_its_details_page = financial_transaction_list_page\
                                                .perform_searching_trading_account_via_filters(transaction_number,
                                                                                               client_name,
                                                                                               transaction_type_text,
                                                                                               modified_time)\
                                                .open_first_financial_transaction_in_list()\
                                                .get_transaction_number_text()

            self.assertEqual(transaction_number, transaction_number_from_its_details_page,
                                                "Wrong financial transaction was found. They have diffent transaction ID")
        except Exception:
            Logging().reportDebugStep(self, "Test check search by column FT is failed")


        # SEARCH VIA BUTTON
        try:
            Logging().reportDebugStep(self, "Check search via button FT")
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            # Open module
            financial_transaction_list_page = CRMHomePage(self.driver) \
                .open_more_list_modules() \
                .select_financial_transactions_module_more_list(
                FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

            # Collect data for searching
            transaction_number = financial_transaction_list_page.get_transaction_id_by_position_from_list()
            client_name = financial_transaction_list_page.get_client_name_by_position_from_list()
            transaction_type_text = financial_transaction_list_page.get_transaction_type_by_position_from_list()
            modified_time = financial_transaction_list_page.get_modified_time_by_position_from_list()
            # trading_account = financial_transaction_list_page.get_trading_account_by_position_from_list()

            # Open search form
            financial_transaction_list_page.open_search_form()
            # Search for transaction Id
            transaction_id_after_searching = financial_transaction_list_page.search_for_transaction_id(transaction_number)\
                                                                                .get_transaction_id_by_position_from_list(1)
            self.assertEqual(transaction_number, transaction_id_after_searching, "Wrong transaction ID was found")

            # Search for client name. Search form is opened
            client_name_after_searching = financial_transaction_list_page.search_for_client_name(client_name).get_client_name_by_position_from_list(1)
            self.assertEqual(client_name, client_name_after_searching, "Wrong client name was found")

            # Search for transaction type. Search form is opened
            transaction_type_after_searching = financial_transaction_list_page.search_for_transaction_type(
                transaction_type_text).get_transaction_type_by_position_from_list(1)
            self.assertEqual(transaction_type_text, transaction_type_after_searching, "Wrong transaction type was found")

            # Search for modified time. Search form is opened
            is_modified_time_found = financial_transaction_list_page.search_for_modified_time(modified_time)\
                                                                    .is_modified_time_in_search_results(modified_time)
            self.assertTrue(is_modified_time_found, "Wrong modified time was found")

        except Exception:
            Logging().reportDebugStep(self, "Test check search via button FT is failed")



    def verify_lead(self, lead_data, converted=None):
        """
        Verify the lead displayed in the detail view against a lead_data dictionary
        :param lead_data: a dictionary containing lead data
        :return: returns True if the lead displayed matches the given lead_data
        :raise: asserts on non matching fields
        """
        lead_detail_view = LeadDetailViewInfo(self.driver)
        lead_detail_view.wait_element_to_be_clickable("//input[@name='Edit']")
        Logging().reportDebugStep(self, "Verifying lead data")

        first_name = lead_detail_view.get_first_name_text()
        last_name = lead_detail_view.get_last_name_text()
        mobile = lead_detail_view.get_mobile_text()
        fax = lead_detail_view.get_fax_text()
        email = lead_detail_view.get_email_text()
        secondary_email = lead_detail_view.get_secondary_email_text()
        source_name = lead_detail_view.get_source_name_text()
        panda_partner_id = lead_detail_view.get_panda_partner_id_text()
        referral = lead_detail_view.get_referral_text()
        street = lead_detail_view.get_street_text()
        postal_code = lead_detail_view.get_postal_code_text()
        country = lead_detail_view.get_country_text()
        description = lead_detail_view.get_description_text()
        phone = lead_detail_view.get_phone_text()
        tittle = lead_detail_view.get_tittle_text()
        lead_source = lead_detail_view.get_lead_source_text()
        lead_status = lead_detail_view.get_lead_status_text()
        if global_var.current_brand_name != "marketsplus":
            language = lead_detail_view.get_language_text()
        # brand = lead_detail_view.get_brand_text()
        po_box = lead_detail_view.get_po_box_text()
        city = lead_detail_view.get_city_text()
        state = lead_detail_view.get_state_text()

        self.assertEqual(first_name, lead_data[LeadsModuleConstants.FIRST_NAME])
        self.assertEqual(last_name, lead_data[LeadsModuleConstants.FIRST_LAST_NAME])
        self.assertEqual(mobile, lead_data[LeadsModuleConstants.FIRST_MOBILE])
        self.assertEqual(fax, lead_data[LeadsModuleConstants.FAX])
        self.assertEqual(email, lead_data[LeadsModuleConstants.EMAIL])
        self.assertEqual(secondary_email, lead_data[LeadsModuleConstants.SECONDARY_EMAIL])
        if global_var.current_brand_name != "marketsplus":
            self.assertEqual(source_name, lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME])
        if lead_data[LeadsModuleConstants.PANDA_PARTNER] and global_var.current_brand_name != "marketsplus":
            self.assertEqual(panda_partner_id, lead_data[LeadsModuleConstants.PANDA_PARTNER])
        if lead_data[LeadsModuleConstants.FIRST_REFERRAL] and global_var.current_brand_name != "marketsplus":
            self.assertEqual(referral, lead_data[LeadsModuleConstants.FIRST_REFERRAL])
        self.assertEqual(street, lead_data[LeadsModuleConstants.STREET])
        self.assertEqual(postal_code, lead_data[LeadsModuleConstants.POSTAL_CODE])
        self.assertEqual(country, lead_data[LeadsModuleConstants.FIRST_COUNTRY])
        self.assertEqual(description, lead_data[LeadsModuleConstants.FIRST_DESCRIPTION])
        self.assertEqual(phone, lead_data[LeadsModuleConstants.PHONE])
        self.assertEqual(tittle, lead_data[LeadsModuleConstants.FIRST_TITTLE])
        if global_var.current_brand_name != "marketsplus":
            self.assertEqual(lead_source, lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE])

        if global_var.current_brand_name == "safemarkets":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW])

        elif global_var.current_brand_name == "uft":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_UFT])

        elif global_var.current_brand_name == "gxfx":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_B_TEST])

        else:
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS])

        if global_var.current_brand_name != "marketsplus":
            self.assertEqual(language, lead_data[LeadsModuleConstants.FIRST_LANGUAGE])
        # if lead_data[LeadsModuleConstants.BRAND]:
        #     self.assertEqual(brand, lead_data[LeadsModuleConstants.BRAND])
        self.assertEqual(po_box, lead_data[LeadsModuleConstants.PO_BOX])
        self.assertEqual(city, lead_data[LeadsModuleConstants.CITY])
        self.assertEqual(state, lead_data[LeadsModuleConstants.FIRST_STATE])
        return True