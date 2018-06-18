from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class CRMMassEditModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_mass_edit(self, gender, assigned_to, client_source, compliance_agent, compliance_notes, client_status,
                          retention_status, description, referral):

        self.set_gender(gender)
        self.set_assigned_to(assigned_to)
        self.set_client_source(client_source)
        self.set_compliance_agent(compliance_agent)
        self.set_compliance_notes(compliance_notes)
        self.set_terms_conditions()
        self.set_client_status(client_status)
        self.set_retention_status(retention_status)
        self.set_description(description)
        self.set_referral(referral)
        return CRMMassEditModule()

    def set_gender(self, gender):
        pass

    def set_assigned_to(self, assigned_to):
        pass

    def set_client_source(self, client_source):
        pass

    def set_compliance_agent(self, compliance_agent):
        pass

    def set_compliance_notes(self, compliance_notes):
        pass

    def set_terms_conditions(self):
        pass

    def set_client_status(self, client_status):
        pass

    def set_retention_status(self, retention_status):
        pass

    def set_description(self, description):
        pass

    def set_referral(self, referral):
        pass
