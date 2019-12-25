from time import sleep
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
import autoit
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import os


class ModuleSearchPage(CRMBasePage):

    def set_search_for_field(self, data):
        sleep(0.2)
        search_for_field = super().wait_load_element("")
