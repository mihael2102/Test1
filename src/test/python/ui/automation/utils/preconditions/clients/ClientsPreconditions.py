from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.ApiConstants import ApiConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.api.ApiPage import ApiPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config


class ClientsPreconditions():
    def create_client_via_api(self):
        api = ApiPage(ApiConstants.PARTNER_ID, ApiConstants.PARTNER_SECRET_KEY, ApiConstants.MILLIS_TIME, Config.url_api_authorization)
        api.api_create_client(api.get_generated_token_api(), Config.url_api_create_client)

ClientsPreconditions().create_client_via_api()