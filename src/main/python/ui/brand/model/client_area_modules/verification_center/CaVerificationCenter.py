import re
from time import sleep
import autoit
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.config import Config


class CaVerificationCenter(BrandBasePage):

    def __init__(self):
        super().__init__()

    '''
        Perform the upload document
        :parameter id client account ID 
        returns Client Profile instance   
    '''

    def perform_front_upload(self):
        sleep(2)
        """
        Upload document to section: Proof of Identity -> Photo ID ->Front upload 
        """
        front_upload_picture = super().wait_visible_of_element(
            "(//label[contains(@for, '')])[4]")
        front_upload_picture.click()
        sleep(2)
        autoit.control_set_text("Open", "Edit1",
                                r"D:\automation-newforexqa\src\main\python\utils\documents\Bear.jpg")
        autoit.control_send("Open", "Edit1", "{ENTER}")
        Logging().reportDebugStep(self, "The  document was uploaded ")
        return CaVerificationCenter()

    '''
         Returns the document status 
    '''

    def get_document_status(self):
        front_upload_picture = super().wait_load_element_present("//span[contains(text(), 'Front Pending')]")
        re_front_upload_picture = re.sub('Front ', '', front_upload_picture.text)
        Logging().reportDebugStep(self,
                                  "Returns the status of document  : " + re_front_upload_picture)
        return re_front_upload_picture
