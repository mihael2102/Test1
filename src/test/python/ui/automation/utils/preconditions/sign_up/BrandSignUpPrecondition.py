from src.main.python.ui.brand.model.forms.financial_transaction.BrandFinancialInformationForm import \
    BrandFinancialInformationForm
from src.main.python.ui.brand.model.forms.trading_experience.BrandTradingExperienceForm import \
    BrandTradingExperienceForm
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


class BrandSignUpPrecondition(object):

    def __init__(self):
        super().__init__()

    def perform_first_step(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area) \
            .open_sign_form() \
            .set_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL)) \
            .set_password(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .set_confirm_password(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CONFIRMATION_PASSWORD)) \
            .set_promo_code(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PROMO_CODE)) \
            .set_country(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY)) \
            .set_check_box() \
            .sign_up_button()
        return BrandSignUpPrecondition()

    def perform_second_step(self):
        self.fill_personal_profile()
        self.fill_financial_information()
        self.fill_trading_experience()

    def fill_personal_profile(self):
        BrandTradingPlatformPage() \
            .open_demo_drop_down(TestDataConstants.ADD_ACCOUNT) \
            .set_first_name(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME)) \
            .set_last_name(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME)) \
            .select_day(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.DAY)) \
            .select_month(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.MONTH)) \
            .select_year(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.YEAR)) \
            .select_country(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.SECOND_COUNTRY)) \
            .select_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
            .select_citizenship(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITIZEN_SHIP)) \
            .set_city(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITY)) \
            .set_post_code(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.POST_CODE)) \
            .set_address(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ADDRESS)) \
            .set_phone(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PHONE)) \
            .enter_next_button()

    def fill_financial_information(self):
        BrandFinancialInformationForm() \
            .select_annual_income(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ANNUAL_IN_COME)) \
            .select_employee_status(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EMPLOYMENT_STATUS)) \
            .select_risk(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.INVEST_MENT_KNOWLEDGE)) \
            .select_average_trade(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.AVERAGE_TRADE)) \
            .select_saving_investment(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.SAVING_INVESTMENT)) \
            .enter_next_button()

    def fill_trading_experience(self):
        BrandTradingExperienceForm() \
            .select_trading_frequency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.TRADING_FREQUENCY)) \
            .select_cfd_trading(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CFD_TRADING)) \
            .select_otcd_frequency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.OTCD_FREQUENCY)) \
            .select_etd_frequency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ETD_FREQUNCY)) \
            .select_us_citizen(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.US_CITIZEN)) \
            .set_us_taxid(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.US_TAXID)) \
            .enter_finish_button()
