from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage


class CreateAffiliateModule(CRMBasePage):
    """
    Methods which are related to "Create affiliate" popup
    """

    def __init__(self):
        super().__init__()

    def perform_create_affiliate(self, partner_name, brand, allowed_ip, is_enabled, allowed_methods, blocked_countries):
        """
        Fill fields of the "Add new affiliate" form
        """
        return None


    def set_partner_name(self, partner_name):
        partner_name_field = super().wait_load_element("//input[@name='partnerName']")
        partner_name_field.







