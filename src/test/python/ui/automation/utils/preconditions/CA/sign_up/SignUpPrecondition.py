import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from time import sleep
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.pages.ca_pages_ui.SignUpFirstStepPage import SignUpFirstStepPage
from src.main.python.ui.ca.model.constants.sign_up.SignUpFirstStepConstants import SignUpFirstStepConstants
from src.main.python.ui.ca.model.pages.ca_pages_ui.MainPage import MainPage
from src.main.python.ui.ca.model.constants.main_page.MainPageConstants import MainPageConstants
from src.main.python.ui.ca.model.pages.ca_pages_ui.PersonalDetailsPage import PersonalDetailsPage
from src.main.python.ui.ca.model.constants.client_area.PersonalDetailsConstants import PersonalDetailsConstants
from src.test.python.ui.automation.utils.preconditions.CA.questionnaire.QuesDualixPrecondition import QuesDualixPrecondition
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.ca.model.pages.ca_pages_ui.LoginPage import LoginPage


class SignUpPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sign_up_ca_ui(self):
        """ Registration 1st step """
        SignUpFirstStepPage(self.driver) \
            .first_step_sign_up(
                url=self.config.get_value('url_ca'),
                field1=SignUpFirstStepConstants.FIELD_FNAME, first_name=SignUpFirstStepConstants.F_NAME,
                field2=SignUpFirstStepConstants.FIELD_LNAME, last_name=SignUpFirstStepConstants.L_NAME,
                field3=SignUpFirstStepConstants.FIELD_EMAIL, email=SignUpFirstStepConstants.EMAIL,
                field4=SignUpFirstStepConstants.FIELD_PHONE, phone=SignUpFirstStepConstants.PHONE,
                field5=SignUpFirstStepConstants.FIELD_PASSWORD, password=SignUpFirstStepConstants.PASSWORD,
                field6=SignUpFirstStepConstants.FIELD_C_PASSWORD, password2=SignUpFirstStepConstants.PASSWORD,
                field7=SignUpFirstStepConstants.FIELD_PROMOCODE, promo_code=SignUpFirstStepConstants.PROMO,
                country=SignUpFirstStepConstants.COUNTRY)

        """ Check graphs """
        WebTraderPage(self.driver) \
            .open_trading_page() \
            .check_chart_loaded()

        """ Registration 2nd step """
        MainPage(self.driver)\
            .click_hi_user() \
            .click_main_menu_item(MainPageConstants.ITEM_PER_DETAILS)

        PersonalDetailsPage(self.driver)\
            .update_personal_information(
                list1=PersonalDetailsConstants.LIST_DAY, day=PersonalDetailsConstants.DAY_BIRTH,
                list2=PersonalDetailsConstants.LIST_MONTH, month=PersonalDetailsConstants.MONTH_BIRTH,
                list3=PersonalDetailsConstants.LIST_YEAR, year=PersonalDetailsConstants.YEAR_BIRTH,
                list4=PersonalDetailsConstants.LIST_COUNTRY, country=PersonalDetailsConstants.COUNTRY,
                list5=PersonalDetailsConstants.LIST_CITIZENSHIP, citizenship=PersonalDetailsConstants.CITIZENSHIP,
                field1=PersonalDetailsConstants.FIELD_CITY, city=PersonalDetailsConstants.CITY,
                field2=PersonalDetailsConstants.FIELD_ZIP, zip_code=PersonalDetailsConstants.ZIP_CODE,
                field3=PersonalDetailsConstants.FIELD_ADDRESS, address=PersonalDetailsConstants.ADDRESS)

        """ Questionnaire """
        if global_var.current_brand_name == "dualix":
            QuesDualixPrecondition(self.driver, self.config)\
                .questionnaire_dualix()

        """ Check Login """
        MainPage(self.driver)\
            .click_hi_user() \
            .click_main_menu_item(MainPageConstants.ITEM_SIGN_OUT)

        LoginPage(self.driver)\
            .login(
                email=SignUpFirstStepConstants.EMAIL,
                password=SignUpFirstStepConstants.PASSWORD)
        sleep(2)
        existing_client = MainPage(self.driver)\
            .get_client()
        expected_client = SignUpFirstStepConstants.F_NAME + SignUpFirstStepConstants.L_NAME

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(existing_client.lower(), expected_client.lower())
