from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class FinancialTransactionInformationPage(CRMBasePage):

    # def __init__(self):
    #     super().__init__()

    def get_trading_account_text(self):
        account_text = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Trading Account')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the trading account name " + account_text.text)
        return account_text.text

    def get_login_text(self):
        login = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Login')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the login account name " + login.text)
        return login.text

    def get_client_text(self):
        client = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Client')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the client account name " + client.text)
        return client.text

    def get_amount_text(self):
        amount = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Amount')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the amount name " + amount.text)
        return amount.text

    def get_currency_text(self):
        currency = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Currency')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the currency name " + currency.text)
        return currency.text

    def get_transaction_type_text(self):
        transaction_type = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Transaction Type')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the transaction type " + transaction_type.text)
        return transaction_type.text

    def get_transaction_number_text(self):
        transaction_number = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Transaction No')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the transaction number " + transaction_number.text)
        return transaction_number.text

    def get_assigned_to_text(self):
        assigned_to = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Assigned To')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the assigned to " + assigned_to.text)
        return assigned_to.text

    def get_brand_text(self):
        brand = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Brand')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the brand " + brand.text)
        return brand.text

    def get_modified_time(self):
        modified_time = super().wait_element_to_be_clickable(
            "//td[contains(text(),'Modified Time')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the modified time " + modified_time.text)
        return modified_time.text

    def get_crm_id(self):
        crm_id = super().wait_element_to_be_clickable(
            "//td[contains(text(),'CRM Id')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the modified time " + crm_id.text)
        return crm_id.text
