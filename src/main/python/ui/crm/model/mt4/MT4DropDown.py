from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class MT4DropDown(CRMBasePage):

    def __init__(self):
        super().__init__()

    def mt4_actions(self, module):
        selected_module = super().wait_element_to_be_clickable("//a[@class='webMnu act_btn btn btn-primary'][%s]" % module)
        selected_module.click()

