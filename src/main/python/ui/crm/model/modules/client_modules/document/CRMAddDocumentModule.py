from time import sleep

import autoit
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CRMAddDocumentModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_download_document(self):
        front_upload_picture = super().wait_element_to_be_clickable("//span[contains(text(),'Browse')]")
        front_upload_picture.click()
        sleep(2)
        autoit.control_set_text("Open", "Edit1",
                                r"D:\automation-newforexqa\src\main\python\utils\documents\bear.jpg")
        autoit.control_send("Open", "Edit1", "{ENTER}")
        Logging().reportDebugStep(self, "The  document was uploaded ")
        return CRMAddDocumentModule()

    def set_document_type(self, type):
        super().wait_element_to_be_clickable("//select[@id='doctype']")
        type_document = Select(self.driver.find_element("//select[@id='doctype']"))
        type_document.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The  document type was set ")
        return CRMAddDocumentModule()

    def set_status(self, status):
        status_document = Select(self.driver.find_element("//select[@id='doc_status']"))
        status_document.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The  document status was set ")
        return CRMAddDocumentModule()

    def set_expire_date(self, expiry_date):
        expire_date = Select(self.driver.find_element("//select[@id='doc_status']"))
        expire_date.select_by_visible_text(expiry_date)
        Logging().reportDebugStep(self, "The  expiry date was set ")
        return CRMAddDocumentModule()

    def set_description_date(self, description):
        expire_date = Select(self.driver.find_element("//textarea[@id='notecontent']"))
        expire_date.select_by_visible_text(description)
        Logging().reportDebugStep(self, "The  description  was set ")
        return CRMAddDocumentModule()
