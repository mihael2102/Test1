from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.ApiConstants import ApiConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.api.ApiPage import ApiPage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config
from src.test.python.ui.automation.BaseTest import BaseTest


class ClientsPreconditions():
    def create_client_via_api(self, partner_id, partner_secret_key, millis_time, url_api_authorization, generated_token, url_create_client, content_type, client_email, client_password, client_country, client_first_name, client_last_name, client_phone):
        api_entity = ApiPage(partner_id, partner_secret_key, millis_time, url_api_authorization)
        api_entity.api_create_client(generated_token, url_create_client, content_type, client_email, client_password, client_country, client_first_name, client_last_name, client_phone)



api_entity = ClientsPreconditions()
ap = ApiPage(Config.data.get_data_api_affiliate_information(ApiConstants.FIELD_NAME_PARTNER_ID),
             Config.data.get_data_api_affiliate_information(ApiConstants.PARTNER_SECRET_KEY),
             ApiConstants.MILLIS_TIME,
             Config.url_api_authorization)

api_entity.create_client_via_api(Config.data.get_data_api_affiliate_information(ApiConstants.FIELD_NAME_PARTNER_ID),
                                 Config.data.get_data_api_affiliate_information(ApiConstants.PARTNER_SECRET_KEY),
                                 ApiConstants.MILLIS_TIME,
                                 Config.url_api_authorization,
                                 ap.get_generated_token_api(),
                                 Config.url_api_create_client,
                                 Config.data.get_data_api_affiliate_information(
                                     ApiConstants.FIELD_NAME_CONTENT_TYPE),
                                 Config.data.get_data_api_client_information(ApiConstants.FIELD_NAME_EMAIL),
                                 Config.data.get_data_api_client_information(ApiConstants.FIELD_NAME_PASSWORD),
                                 Config.data.get_data_api_client_information(ApiConstants.FIELD_NAME_COUNTRY),
                                 Config.data.get_data_api_client_information(ApiConstants.FIELD_NAME_FIRSTNAME),
                                 Config.data.get_data_api_client_information(ApiConstants.FIELD_NAME_LASTNAME),
                                 Config.data.get_data_api_client_information(ApiConstants.FIELD_NAME_PHONE))