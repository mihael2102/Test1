from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.side_bar.create_event.CreateEvent import CreateEvent
from src.main.python.utils.logs.Loging import Logging


class SidebarModules(CRMBasePage):
    def __init__(self):
        super().__init__()

    def open_create_event_module(self, module):
        selected_module = super().wait_element_to_be_clickable("//div[@id='sidebar']//tr[%s]" % module)
        selected_module.click()
        Logging().reportDebugStep(self, "The event module was opened")
        return CreateEvent()
