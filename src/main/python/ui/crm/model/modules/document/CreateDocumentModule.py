from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CreateDocumentModule(CRMBasePage):

    def perform_create_document(self, type, status, description):
        self.perform_download_document()
        self.set_attach_to()
        self.switch_first_window_page()
        self.set_document_type(type)
        self.set_status(status)
        self.set_description(description)
        self.click_save_button_document_module()
        return CreateDocumentModule()

    def perform_create_document_client_profile(self, type, status, description):
        self.perform_download_document()
        self.set_document_type(type)
        self.set_status(status)
        self.set_description(description)
        self.click_save_button_document_module()
        return CreateDocumentModule()

    def perform_download_document(self):
        front_upload_picture = super().wait_element_to_be_clickable("//span[contains(text(),'Browse')]")
        front_upload_picture.click()
        sleep(2)
        autoit.control_set_text("Open", "Edit1",
                                r"C:\Users\Administrator\.jenkins\workspace\%s\src\main\python\utils\documents\Bear.jpg" % Config.test)
        autoit.control_send("Open", "Edit1", "{ENTER}")
        Logging().reportDebugStep(self, "The  document was uploaded ")
        return CreateDocumentModule()

    def set_attach_to(self):
        attach_to = super().wait_element_to_be_clickable("//img[@title='Select Attached To']")
        attach_to.click()
        handle = self.driver.window_handles[1]
        self.driver.switch_to_window(handle)
        search_button = super().wait_element_to_be_clickable("//a[contains(text(),'TestQa Li')]")
        search_button.click()
        return CreateDocumentModule()

    def switch_first_window_page(self):
        super().switch_first_window_page()
        return CreateDocumentModule()

    def set_document_type(self, type):
        super().wait_element_to_be_clickable("//select[@id='doctype']")
        type_document = Select(self.driver.find_element(By.XPATH, "//select[@id='doctype']"))
        type_document.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The document type was set ")
        return CreateDocumentModule()

    def set_status(self, status):
        status_document = Select(self.driver.find_element(By.XPATH, "//select[@id='doc_status']"))
        status_document.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The  document status was set ")
        return CreateDocumentModule()

    def set_expire_date(self, ):
        expire_date_drop_down = self.driver.find_element(By.XPATH, "//input[@id='crm_expiry_date']")
        hoverer = ActionChains(self.driver).move_to_element(expire_date_drop_down).click(expire_date_drop_down)
        hoverer.perform()
        expire_date_drop_down.click()
        Logging().reportDebugStep(self, "The expiry date was set ")
        return CreateDocumentModule()

    def set_description(self, description):
        description_field = self.driver.find_element(By.XPATH, "//textarea[@id='notecontent']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "The description was set ")
        return CreateDocumentModule()

    def click_save_button_document_module(self):
        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()
        return CreateDocumentModule()
