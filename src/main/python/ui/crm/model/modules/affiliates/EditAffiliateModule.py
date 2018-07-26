from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.webdriver.support.ui import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC


class EditAffiliateModule(CRMBasePage):

    def __init__(self):
        super().__init__()



