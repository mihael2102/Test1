from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
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
        type_document = Select(self.driver.find_element(By.XPATH, "//select[@id='doctype']"))
        type_document.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The document type was set ")
        return CRMAddDocumentModule()

    def set_status(self, status):
        status_document = Select(self.driver.find_element(By.XPATH, "//select[@id='doc_status']"))
        status_document.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The  document status was set ")
        return CRMAddDocumentModule()

    def set_expire_date(self, ):
        expire_date_drop_down = self.driver.find_element(By.XPATH, "//input[@id='crm_expiry_date']")
        hoverer = ActionChains(self.driver).move_to_element(expire_date_drop_down).click(expire_date_drop_down)
        hoverer.perform()
        expire_date_drop_down.click()
        Logging().reportDebugStep(self, "The expiry date was set ")
        return CRMAddDocumentModule()

    def set_description_date(self, description):
        description_field = self.driver.find_element(By.XPATH, "//textarea[@id='notecontent']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "The description was set ")
        return CRMAddDocumentModule()
