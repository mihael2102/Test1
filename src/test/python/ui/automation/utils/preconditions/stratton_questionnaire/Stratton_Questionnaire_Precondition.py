from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
import poplib
from email import parser
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.ca.model.constants.CAconstants.QuestionnaireConstants import QuestionnaireConstants
from src.main.python.ui.ca.model.pages.ca.QuestionnairePage import QuestionnairePage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule


class StrattonQuestionnairePrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def customer_classification_empty(self):
        assert global_var.current_brand_name == "strattonmarkets-eu"
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .click_sign_up()\
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])\
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_LAST_NAME])\
            .fill_email(QuestionnaireConstants.MAIL_CLIENT_EMPTY)\
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.PHONE])\
            .fill_password(CAConstants.PASSWORD)\
            .fill_confirm_password(CAConstants.PASSWORD)\
            .check_box_accept()\
            .click_submit()\
            .verify()

        # Check status of customer_classification in CRM
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url'))\
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(QuestionnaireConstants.MAIL_CLIENT_EMPTY)
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()
        assert customer_classification.strip() == QuestionnaireConstants.CUSTOMER_CLASSIFICATION_EMPTY

        ClientProfilePage(self.driver) \
            .verify_clean_questionnaire_btn_visible()

    def customer_classification_blocked(self):
        assert global_var.current_brand_name == "strattonmarkets-eu"
        # Registration
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .click_sign_up()\
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])\
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_LAST_NAME])\
            .fill_email(QuestionnaireConstants.MAIL_CLIENT_BLOCKED)\
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.PHONE])\
            .fill_password(CAConstants.PASSWORD)\
            .fill_confirm_password(CAConstants.PASSWORD)\
            .check_box_accept()\
            .click_submit()\
            .verify()\
            .click_hi_guest() \
            .click_transactions_history() \
            .select_data_birth_day(CAConstants.DAY_BIRTH) \
            .select_data_birth_month(CAConstants.MONTH_BIRTH) \
            .select_data_birth_year(CAConstants.YEAR_BIRTH) \
            .choose_currency(CAConstants.CURRENCY) \
            .choose_citizenship(CAConstants.CITIZENSHIP3) \
            .fill_city(CAConstants.CITY) \
            .fill_zip_code(CAConstants.ZIP_CODE) \
            .fill_address(CAConstants.ADDRESS) \
            .click_next()\
            .select_us_reportable(CAConstants.US_REPORTABLE_YES)\
            .confirm_us_reportable() \
            .came_back_on_previous_page() \
            .login() \
            .enter_email(QuestionnaireConstants.MAIL_CLIENT_BLOCKED) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()\
            .verify_registration_blocked()

        # Check status of customer_classification in CRM
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(QuestionnaireConstants.MAIL_CLIENT_BLOCKED)
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()

        assert customer_classification.strip() == QuestionnaireConstants.CUSTOMER_CLASSIFICATION_BLOCKED

        # Check 'Clean Questionnaire' button is visible
        ClientProfilePage(self.driver) \
            .verify_clean_questionnaire_btn_visible()

        # Check MT Actions contain only 9 items (there is no Create MT User)
        ClientProfilePage(self.driver)\
            .wait_element_to_be_disappear("//div[@id='mt4_act_box']/a[10]")

    def customer_classification_negative(self):
            assert global_var.current_brand_name == "strattonmarkets-eu"
            # Registration
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .click_sign_up() \
                .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                     LeadsModuleConstants.FIRST_NAME]) \
                .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                    LeadsModuleConstants.FIRST_LAST_NAME]) \
                .fill_email(QuestionnaireConstants.MAIL_CLIENT_NEGATIVE) \
                .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                LeadsModuleConstants.PHONE]) \
                .fill_password(CAConstants.PASSWORD) \
                .fill_confirm_password(CAConstants.PASSWORD) \
                .check_box_accept() \
                .click_submit() \
                .verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_currency(CAConstants.CURRENCY) \
                .choose_citizenship(CAConstants.CITIZENSHIP3) \
                .fill_city(CAConstants.CITY) \
                .fill_zip_code(CAConstants.ZIP_CODE) \
                .fill_address(CAConstants.ADDRESS) \
                .click_next() \
                .enter_ssn_tin(QuestionnaireConstants.SSN_TIN) \
                .enter_id(QuestionnaireConstants.NAT_ID) \
                .select_country_tax(QuestionnaireConstants.COUNTRY_TAX) \
                .enter_company_name(QuestionnaireConstants.COMPANY_NAME) \
                .select_us_reportable(CAConstants.US_REPORTABLE_NO) \
                .click_save_changes_btn()

            # Questionnaire: Financial Information
            QuestionnairePage(self.driver)\
                .select_employment_status(QuestionnaireConstants.EMPLOYMENT_STATUS_STUDENT) \
                .select_education_level(QuestionnaireConstants.EDUCATION_LEVEL_NO_EDUCATION) \
                .select_politically_exposed_person(QuestionnaireConstants.POLITICALLY_EXPOSED_PERSON_NO) \
                .select_total_annual_income(QuestionnaireConstants.TOTAL_ANNUAL_INCOME_UNDER_15) \
                .select_approximate_net_wealth(QuestionnaireConstants.APPROXIMATE_NET_WEALTH_UNDER_15) \
                .select_expected_deposit(QuestionnaireConstants.EXPECTED_DEPOSIT_UNDER_10) \
                .select_source_of_trading_funds(QuestionnaireConstants.SOURCE_TRADING_FUNDS_EMPLOYMENT) \
                .select_why_want_trade(QuestionnaireConstants.WHY_WANT_TRADE_SPECULATIVE) \
                .select_react_on_losses(QuestionnaireConstants.REACT_ON_LOSSES_EXPECT_TO_LOSE) \
                .click_next_btn()

            # Questionnaire: Knowledge and experience
            QuestionnairePage(self.driver) \
                .select_instruments_traded_before(QuestionnaireConstants.INSTRUMENTS_TRADED_BEFORE_NO_EXPERIENCE) \
                .select_if_applicable(QuestionnaireConstants.IF_APPLICABLE_NONE) \
                .select_correct_regarding_cfd(QuestionnaireConstants.REGARDING_CFD) \
                .select_factor_affect_prices(QuestionnaireConstants.FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS) \
                .select_close_bmw_position(QuestionnaireConstants.WHERE_CLOSE_BMW_POSITION_LONDON) \
                .select_required_margin(QuestionnaireConstants.REQUIRED_MARGIN_100) \
                .select_loss(QuestionnaireConstants.LOSS_AMOUNT_800) \
                .click_next_btn() \
                .verify_questionnaire_message(QuestionnaireConstants.MESSAGE_NEGATIVE) \
                .click_next_btn()

            # Verify was opened DEMO account
            CAPage(self.driver)\
                .open_accounts_list()\
                .verify_active_account_server(CAConstants.ACCOUNT_DEMO)

            # Check status of customer_classification in CRM
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET)) \
                .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           TestDataConstants.FILTER))

            sleep(2)
            ClientsPage(self.driver).find_client_by_email(QuestionnaireConstants.MAIL_CLIENT_NEGATIVE)
            customer_classification = ClientProfilePage(self.driver).get_customer_classification()

            assert customer_classification.strip() == QuestionnaireConstants.CUSTOMER_CLASSIFICATION_NEGATIVE

            # Check client able open only demo account
            ClientProfilePage(self.driver) \
                .verify_clean_questionnaire_btn_visible() \
                .open_mt4_actions(CRMConstants.CREATE_MT4_USER)
            MT4CreateAccountModule(self.driver) \
                .verify_server_not_available(CRMConstants.SERVER_LIVE)

    def customer_classification_retail(self):
        assert global_var.current_brand_name == "strattonmarkets-eu"
        # Registration
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .click_sign_up() \
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.FIRST_NAME]) \
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                LeadsModuleConstants.FIRST_LAST_NAME]) \
            .fill_email(QuestionnaireConstants.MAIL_CLIENT_RETAIL) \
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                            LeadsModuleConstants.PHONE]) \
            .fill_password(CAConstants.PASSWORD) \
            .fill_confirm_password(CAConstants.PASSWORD) \
            .check_box_accept() \
            .click_submit() \
            .verify() \
            .click_hi_guest() \
            .click_transactions_history() \
            .select_data_birth_day(CAConstants.DAY_BIRTH) \
            .select_data_birth_month(CAConstants.MONTH_BIRTH) \
            .select_data_birth_year(CAConstants.YEAR_BIRTH) \
            .choose_currency(CAConstants.CURRENCY) \
            .choose_citizenship(CAConstants.CITIZENSHIP3) \
            .fill_city(CAConstants.CITY) \
            .fill_zip_code(CAConstants.ZIP_CODE) \
            .fill_address(CAConstants.ADDRESS) \
            .click_next() \
            .enter_ssn_tin(QuestionnaireConstants.SSN_TIN) \
            .enter_id(QuestionnaireConstants.NAT_ID) \
            .select_country_tax(QuestionnaireConstants.COUNTRY_TAX) \
            .enter_company_name(QuestionnaireConstants.COMPANY_NAME) \
            .select_us_reportable(CAConstants.US_REPORTABLE_NO) \
            .click_save_changes_btn()

        # Questionnaire: Financial Information
        QuestionnairePage(self.driver) \
            .select_employment_status(QuestionnaireConstants.EMPLOYMENT_STATUS_STUDENT) \
            .select_education_level(QuestionnaireConstants.EDUCATION_LEVEL_NO_EDUCATION) \
            .select_politically_exposed_person(QuestionnaireConstants.POLITICALLY_EXPOSED_PERSON_NO) \
            .select_total_annual_income(QuestionnaireConstants.TOTAL_ANNUAL_INCOME_UNDER_15) \
            .select_approximate_net_wealth(QuestionnaireConstants.APPROXIMATE_NET_WEALTH_UNDER_15) \
            .select_expected_deposit(QuestionnaireConstants.EXPECTED_DEPOSIT_UNDER_10) \
            .select_source_of_trading_funds(QuestionnaireConstants.SOURCE_TRADING_FUNDS_EMPLOYMENT) \
            .select_why_want_trade(QuestionnaireConstants.WHY_WANT_TRADE_SPECULATIVE) \
            .select_react_on_losses(QuestionnaireConstants.REACT_ON_LOSSES_EXPECT_TO_LOSE) \
            .click_next_btn()

        # Questionnaire: Knowledge and experience
        QuestionnairePage(self.driver) \
            .select_instruments_traded_before(QuestionnaireConstants.INSTRUMENTS_TRADED_BEFORE_NO_EXPERIENCE) \
            .select_if_applicable(QuestionnaireConstants.IF_APPLICABLE_NONE) \
            .select_correct_regarding_cfd(QuestionnaireConstants.REGARDING_CFD_RETAIL) \
            .select_factor_affect_prices(QuestionnaireConstants.FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS_RETAIL) \
            .select_close_bmw_position(QuestionnaireConstants.WHERE_CLOSE_BMW_POSITION_RETAIL) \
            .select_required_margin(QuestionnaireConstants.REQUIRED_MARGIN_1000) \
            .select_loss(QuestionnaireConstants.LOSS_AMOUNT_800) \
            .click_next_btn() \
            .verify_questionnaire_message(QuestionnaireConstants.MESSAGE_RETAIL) \
            .click_next_btn()

        # Verify was opened LIVE account
        CAPage(self.driver)\
            .open_accounts_list()\
            .verify_active_account_server(CAConstants.ACCOUNT_LIVE)

        # Check status of customer_classification in CRM
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver)\
            .find_client_by_email(QuestionnaireConstants.MAIL_CLIENT_RETAIL)
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()

        assert customer_classification.strip() == QuestionnaireConstants.CUSTOMER_CLASSIFICATION_RETAIL

        # Check client able open live account
        ClientProfilePage(self.driver) \
            .verify_clean_questionnaire_btn_visible() \
            .open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        MT4CreateAccountModule(self.driver) \
            .select_server(QuestionnaireConstants.STRATTON_LIVE)\
            .select_currency(QuestionnaireConstants.CURRENCY_EUR)\
            .verify_group_not_available(QuestionnaireConstants.GROUP_STR_VGOLD_EUR)\
            .select_group(QuestionnaireConstants.GROUP_STR_VLGOLD_EUR)\
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_100)\
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_200)\
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_300)\
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_400)\
            .set_leverage(QuestionnaireConstants.LEVERAGE_1_30)\
            .click_create()

        # Verify successful message
        confirmation_message = ClientProfilePage(self.driver) \
            .get_confirm_message()
        assert CRMConstants.SUCCESSFUL_MESSAGE in confirmation_message

    def customer_classification_professional_eligible(self):
        assert global_var.current_brand_name == "strattonmarkets-eu"
        # Registration
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .click_sign_up() \
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.FIRST_NAME]) \
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                LeadsModuleConstants.FIRST_LAST_NAME]) \
            .fill_email(QuestionnaireConstants.MAIL_CLIENT_PROFESSIONAL_ELIGIBLE) \
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                            LeadsModuleConstants.PHONE]) \
            .fill_password(CAConstants.PASSWORD) \
            .fill_confirm_password(CAConstants.PASSWORD) \
            .check_box_accept() \
            .click_submit() \
            .verify() \
            .click_hi_guest() \
            .click_transactions_history() \
            .select_data_birth_day(CAConstants.DAY_BIRTH) \
            .select_data_birth_month(CAConstants.MONTH_BIRTH) \
            .select_data_birth_year(CAConstants.YEAR_BIRTH) \
            .choose_currency(CAConstants.CURRENCY) \
            .choose_citizenship(CAConstants.CITIZENSHIP3) \
            .fill_city(CAConstants.CITY) \
            .fill_zip_code(CAConstants.ZIP_CODE) \
            .fill_address(CAConstants.ADDRESS) \
            .click_next() \
            .enter_ssn_tin(QuestionnaireConstants.SSN_TIN) \
            .enter_id(QuestionnaireConstants.NAT_ID) \
            .select_country_tax(QuestionnaireConstants.COUNTRY_TAX) \
            .enter_company_name(QuestionnaireConstants.COMPANY_NAME) \
            .select_us_reportable(CAConstants.US_REPORTABLE_NO) \
            .click_save_changes_btn()

        # Questionnaire: Financial Information
        QuestionnairePage(self.driver) \
            .select_employment_status(QuestionnaireConstants.EMPLOYMENT_STATUS_STUDENT) \
            .select_education_level(QuestionnaireConstants.EDUCATION_LEVEL_NO_EDUCATION) \
            .select_politically_exposed_person(QuestionnaireConstants.POLITICALLY_EXPOSED_PERSON_NO) \
            .select_total_annual_income(QuestionnaireConstants.TOTAL_ANNUAL_INCOME_OVER_700) \
            .select_approximate_net_wealth(QuestionnaireConstants.APPROXIMATE_NET_WEALTH_OVER_700) \
            .select_expected_deposit(QuestionnaireConstants.EXPECTED_DEPOSIT_OVER_350) \
            .select_source_of_trading_funds(QuestionnaireConstants.SOURCE_TRADING_FUNDS_EMPLOYMENT) \
            .select_why_want_trade(QuestionnaireConstants.WHY_WANT_TRADE_ADDITIONAL_INCOME) \
            .select_react_on_losses(QuestionnaireConstants.REACT_ON_LOSSES_NO_BIG_DEAL) \
            .click_next_btn()

        # Questionnaire: Knowledge and experience
        QuestionnairePage(self.driver) \
            .select_instruments_traded_before(QuestionnaireConstants.INSTRUMENTS_TRADED_BEFORE_BOTH_ABOVE) \
            .select_average_frequency(QuestionnaireConstants.AVERAGE_FREQUENCY_20) \
            .select_trade_size(QuestionnaireConstants.TRADE_SIZE_MORE_10000) \
            .select_common_level(QuestionnaireConstants.COMMON_LEVEL_ABOVE_30)\
            .select_if_applicable(QuestionnaireConstants.IF_APPLICABLE_BOTH_ABOVE) \
            .select_correct_regarding_cfd(QuestionnaireConstants.REGARDING_CFD_RETAIL) \
            .select_factor_affect_prices(QuestionnaireConstants.FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS_RETAIL) \
            .select_close_bmw_position(QuestionnaireConstants.WHERE_CLOSE_BMW_POSITION_RETAIL) \
            .select_required_margin(QuestionnaireConstants.REQUIRED_MARGIN_1000) \
            .select_loss(QuestionnaireConstants.LOSS_AMOUNT_450) \
            .click_next_btn()

        # Verify was opened LIVE account
        CAPage(self.driver)\
            .open_accounts_list()\
            .verify_active_account_server(CAConstants.ACCOUNT_LIVE)

        # Check status of customer_classification in CRM
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver) \
            .find_client_by_email(QuestionnaireConstants.MAIL_CLIENT_PROFESSIONAL_ELIGIBLE)
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()

        assert customer_classification.strip() == QuestionnaireConstants.CUSTOMER_CLASSIFICATION_PROF_ELIGIBLE

        # Check client able open live account
        ClientProfilePage(self.driver) \
            .verify_clean_questionnaire_btn_not_visible() \
            .open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        MT4CreateAccountModule(self.driver) \
            .select_server(QuestionnaireConstants.STRATTON_LIVE) \
            .select_currency(QuestionnaireConstants.CURRENCY_EUR) \
            .verify_group_not_available(QuestionnaireConstants.GROUP_STR_VGOLD_EUR) \
            .select_group(QuestionnaireConstants.GROUP_STR_VLGOLD_EUR) \
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_100) \
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_200) \
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_300) \
            .verify_leverage_not_available(QuestionnaireConstants.LEVERAGE_400) \
            .set_leverage(QuestionnaireConstants.LEVERAGE_1_30) \
            .click_create()

        # Verify successful message
        confirmation_message = ClientProfilePage(self.driver) \
            .get_confirm_message()
        assert CRMConstants.SUCCESSFUL_MESSAGE in confirmation_message

    def customer_classification_professional_elective(self):
        # Check status of customer_classification in CRM
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver) \
            .find_client_by_email(QuestionnaireConstants.MAIL_CLIENT_PROFESSIONAL_ELIGIBLE)
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()

        assert customer_classification.strip() == QuestionnaireConstants.CUSTOMER_CLASSIFICATION_PROF_ELIGIBLE

        # Update customer_classification to 'elective'
        update_questionnaire_msg = ClientProfilePage(self.driver)\
            .click_view_edit_questionnaire_btn() \
            .set_professional_classification(QuestionnaireConstants.PROF_CLASSIFICATION_ELECTIVE) \
            .click_save_questionnaire_btn() \
            .get_confirm_message()
        assert update_questionnaire_msg == QuestionnaireConstants.UPDATE_QUESTIONNAIRE_MSG
        ClientProfilePage(self.driver) \
            .click_ok()

        # Check client able open live account
        ClientProfilePage(self.driver) \
            .open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        MT4CreateAccountModule(self.driver) \
            .select_server(QuestionnaireConstants.STRATTON_LIVE) \
            .select_currency(QuestionnaireConstants.CURRENCY_EUR) \
            .verify_group_not_available(QuestionnaireConstants.GROUP_STR_VLGOLD_EUR) \
            .select_group(QuestionnaireConstants.GROUP_STR_VGOLD_EUR) \
            .verify_leverage_available(QuestionnaireConstants.LEVERAGE_100) \
            .verify_leverage_available(QuestionnaireConstants.LEVERAGE_200) \
            .verify_leverage_available(QuestionnaireConstants.LEVERAGE_300) \
            .verify_leverage_available(QuestionnaireConstants.LEVERAGE_400) \
            .set_leverage(QuestionnaireConstants.LEVERAGE_1_400) \
            .click_create()

        # Verify successful message
        confirmation_message = ClientProfilePage(self.driver) \
            .get_confirm_message()
        assert CRMConstants.SUCCESSFUL_MESSAGE in confirmation_message
