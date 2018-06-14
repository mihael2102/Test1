import re
from time import sleep
import autoit
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class CaVerificationCenter(BrandBasePage):

    def __init__(self):
        super().__init__()

    '''
        Perform the upload document
        :parameter id client account ID 
        returns Client Profile instance   
    '''

    def perform_front_upload(self):
        front_upload_picture = super().wait_load_element_present("//label[@for='upload_photo_id_front']")
        front_upload_picture.click()
        sleep(2)
        autoit.control_set_text("Open", "Edit1",
                                r"automation-newforexqa\src\main\python\utils\documents\bear.jpg")
        autoit.control_send("Open", "Edit1", "{ENTER}")
        Logging().reportDebugStep(self, "The  document was uploaded ")
        return CaVerificationCenter()

    '''
         Returns the document status 
    '''

    def get_document_status(self):
        front_upload_picture = super().wait_load_element_present("//div[@class='document-wrapper-pandats']//span")
        re_front_upload_picture = re.sub('Front ', '', front_upload_picture.text)
        Logging().reportDebugStep(self,
                                  "Returns the document status: the  document status is :" + re_front_upload_picture)
        return re_front_upload_picture
