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


class GlobalSearchPage(CRMBasePage):

    def get_email_search_page_vtiger(self):
        sleep(0.2)
        email = super().wait_load_element("//div[@class='searchResults']//div[@title='send mail']").text
        Logging().reportDebugStep(self, "Get Email from global searching page results: " + email)
        return email

    def get_created_time_search_page_vtiger(self):
        sleep(0.2)
        created_time = super().wait_load_element\
            ("//div[@class='searchResults']//a[contains(text(),'2019') or contains(text(),'2020')]")\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Created time from global searching page results: " + created_time)
        return created_time

    def get_crm_id_search_page_laravel(self):
        sleep(0.2)
        crm_id = super().wait_load_element("//div[@class='searchResults']//td[contains(text(),'ACC')]")\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get CRM ID from global searching page results: " + crm_id)
        return crm_id

    def get_created_time_search_page_laravel(self):
        sleep(0.2)
        created_time = super().wait_load_element\
            ("//div[@class='searchResults']//td[contains(text(),'2019') or contains(text(),'2020')]")\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Created time from global searching page results: " + created_time)
        return created_time
