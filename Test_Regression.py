from src.test.python.ui.automation.implementation.crm.clients_module.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.clients_module.Test_Create_Filter import CreateFilterTestCRM
from src.test.python.ui.automation.implementation.crm.clients_module.Test_Send_SMS_Clients_Module import \
    SendSMSClientsModule
from src.test.python.ui.automation.implementation.crm.tasks_module.Test_Event import AddEventTaskModule
from src.test.python.ui.automation.implementation.crm.tasks_module.Test_Mass_Sms import MassSmsTaskModule


class TestRegression(object):

    def run_add_interaction_crm(self):
        AddInteraction()

    def run_perform_create_filter_crm(self):
        CreateFilterTestCRM()

    def run_perform_send_sms(self):
        SendSMSClientsModule()

    def run_add_event_calendar_view(self):
        AddEventTaskModule()

    def run_mass_sms(self):
        MassSmsTaskModule()
