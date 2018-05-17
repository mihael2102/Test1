from scr.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class MT4DropDown(CRMBasePage):

    def __init__(self):
        super().__init__()

    def mt4_actions(self, module):
        if module == "6":
            self.open_module(module)
        if module == "2":
            self.open_module(module)

    def open_module(self, module):
        selected_module = super().wait_load_element("//a[@class='webMnu act_btn btn btn-primary'][%s]" % module)
        selected_module.click()
