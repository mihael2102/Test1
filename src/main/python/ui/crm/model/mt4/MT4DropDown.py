from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import time

class MT4DropDown(CRMBasePage):

    def mt4_actions(self, module):
        time.sleep(5)
        selected_module = super().wait_element_to_be_clickable(
            "//a[@class='webMnu act_btn btn btn-primary'][%s]" % module)
        selected_module.click()
