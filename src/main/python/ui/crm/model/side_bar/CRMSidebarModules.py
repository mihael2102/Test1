from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.side_bar.create_event.CRMCreateEvent import CRMCreateEvent


class CRMSidebarModules(CRMBasePage):
    def __init__(self):
        super().__init__()

    def open_create_event_module(self, module):
        selected_module = super().wait_element_to_be_clickable("//div[@id='sidebar']//tr[%s]" % module)
        selected_module.click()
        return CRMCreateEvent()
