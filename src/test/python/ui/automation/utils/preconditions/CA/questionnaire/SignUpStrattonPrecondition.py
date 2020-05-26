from src.main.python.ui.ca.model.pages.ca.QuestionnairePage import QuestionnairePage
from src.main.python.ui.ca.model.constants.questionnaire.QuesStrattonConstants import QuesStrattonConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage


class SignUpStrattonPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sign_up_stratton(self):
        """ Registration form """
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .close_campaign_banner() \
            .click_sign_up() \
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)
                             [LeadsModuleConstants.FIRST_NAME]) \
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)
                            [LeadsModuleConstants.FIRST_LAST_NAME]) \
            .fill_email(CAConstants.EMAIL_CA) \
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.PHONE]) \
            .fill_password(CAConstants.PASSWORD) \
            .fill_confirm_password(CAConstants.PASSWORD) \
            .check_box_accept() \
            .risk_check_box_accept() \
            .select_country_first_step(CAConstants.COUNTRY1) \
            .click_submit() \
            .close_payment_popup()

        """ Check graphs """
        WebTraderPage(self.driver) \
            .open_trading_page() \
            .check_chart_loaded()

        """ Personal details form """
        CALoginPage(self.driver) \
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
            .enter_ssn_tin(QuesStrattonConstants.SSN_TIN) \
            .enter_id(QuesStrattonConstants.NAT_ID) \
            .select_country_tax(QuesStrattonConstants.COUNTRY_TAX) \
            .enter_company_name(QuesStrattonConstants.COMPANY_NAME) \
            .select_us_reportable(CAConstants.US_REPORTABLE_NO) \
            .click_save_changes_btn()

        """ Questionnaire: Financial Information """
        QuestionnairePage(self.driver) \
            .select_employment_status(QuesStrattonConstants.EMPLOYMENT_STATUS_STUDENT) \
            .select_education_level(QuesStrattonConstants.EDUCATION_LEVEL_NO_EDUCATION) \
            .select_politically_exposed_person(QuesStrattonConstants.POLITICALLY_EXPOSED_PERSON_NO) \
            .select_total_annual_income(QuesStrattonConstants.TOTAL_ANNUAL_INCOME_UNDER_15) \
            .select_approximate_net_wealth(QuesStrattonConstants.APPROXIMATE_NET_WEALTH_UNDER_15) \
            .select_expected_deposit(QuesStrattonConstants.EXPECTED_DEPOSIT_UNDER_10) \
            .select_source_of_trading_funds(QuesStrattonConstants.SOURCE_TRADING_FUNDS_EMPLOYMENT) \
            .select_why_want_trade(QuesStrattonConstants.WHY_WANT_TRADE_SPECULATIVE) \
            .select_react_on_losses(QuesStrattonConstants.REACT_ON_LOSSES_EXPECT_TO_LOSE) \
            .click_next_btn()

        """ Questionnaire: Knowledge and experience """
        QuestionnairePage(self.driver) \
            .select_instruments_traded_before(QuesStrattonConstants.INSTRUMENTS_TRADED_BEFORE_NO_EXPERIENCE) \
            .select_if_applicable(QuesStrattonConstants.IF_APPLICABLE_NONE) \
            .select_correct_regarding_cfd(QuesStrattonConstants.REGARDING_CFD_RETAIL) \
            .select_factor_affect_prices(QuesStrattonConstants.FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS_RETAIL) \
            .select_close_bmw_position(QuesStrattonConstants.WHERE_CLOSE_BMW_POSITION_RETAIL) \
            .select_required_margin(QuesStrattonConstants.REQUIRED_MARGIN_1000) \
            .select_loss(QuesStrattonConstants.LOSS_AMOUNT_800) \
            .click_next_btn() \
            .verify_questionnaire_message(QuesStrattonConstants.MESSAGE_RETAIL) \
            .close_questionnaire_message()
        CALoginPage(self.driver) \
            .verify() \
            .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                               LeadsModuleConstants.FIRST_NAME]) \
            .sign_out()
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .login() \
            .enter_email(CAConstants.EMAIL_CA) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login() \
            .verify()

        sleep(2)
        existing_client = CALoginPage(self.driver).verify_client(self.load_lead_from_config(
            TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME])
        expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

        assert existing_client.lower() == expected_client.lower()
