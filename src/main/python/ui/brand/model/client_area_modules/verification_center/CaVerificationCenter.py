import re
from time import sleep

import autoit

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class CaVerificationCenter(BrandBasePage):

    def __init__(self):
        super().__init__()

    def perform_front_upload(self):
        front_upload_picture = super().wait_load_element("//label[@for='upload_photo_id_front']")
        front_upload_picture.click()
        sleep(2)
        autoit.control_set_text("Open", "Edit1",
                                r"D:\MyWork\Develop\glo-project(last_version3)\glo-project(last_version)\glo-project\panda\scr\main\python\utils\documents\bear.jpg")
        autoit.control_send("Open", "Edit1", "{ENTER}")
        return CaVerificationCenter()

    def get_document_status(self):
        front_upload_picture = super().wait_load_element("//div[@class='document-wrapper-pandats']//span")
        re_front_upload_picture = re.sub('Front ', '', front_upload_picture.text)
        return re_front_upload_picture
