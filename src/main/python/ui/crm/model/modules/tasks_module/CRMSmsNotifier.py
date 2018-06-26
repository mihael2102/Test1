import re

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CRMSmsNotifierModule(CRMBasePage):
    def __init__(self):
        super().__init__()

    def get_sms_text(self):
        sms_message = super().wait_element_to_be_clickable("//div[@id='tblSMSInformation']//tr[1]//td[2]")
        parser_sms_message_text = re.sub('[" "]', '', sms_message.text, 1)
        Logging().reportDebugStep(self, "Returns the sms message " + parser_sms_message_text)
        return parser_sms_message_text
