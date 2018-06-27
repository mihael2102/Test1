from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document_module.CRMDocumentModule import DocumentModule
from src.main.python.ui.crm.model.modules.tasks_module.CRMTaskModule import CRMTaskModule
from src.main.python.utils.logs.Loging import Logging


class ActionsChains(object):
    pass


class CRMHomePage(CRMBasePage):

    def __init__(self):
        super().__init__()

    ''' 
         Open the task module 
         return Help Desk instance
     '''

    def open_task_module(self):
        task_module = super().wait_load_element("//span[@class='glyphicon glyphicon-Tasks']")
        task_module.click()
        Logging().reportDebugStep(self, "Task module is opened")
        return CRMTaskModule()

    def open_more_list_modules(self):
        hover_mouse = ActionChains(self.driver)
        more_list_element = super().wait_element_to_be_clickable("//a[contains(text(),'More')]")
        hover_mouse.move_to_element(more_list_element)
        hover_mouse.perform()
        return CRMHomePage()

    def select_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        return DocumentModule()
