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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import os


class ModuleSearchPage(CRMBasePage):

    def set_search_for_field(self, data):
        sleep(0.2)
        search_for_field = super().wait_load_element("//*[@id='searchAcc']//input[@name='search_text']")
        search_for_field.clear()
        search_for_field.send_keys(data)
        Logging().reportDebugStep(self, "Set data to 'Search for' field: " + data)
        return ModuleSearchPage(self.driver)

    def select_in_list(self, item):
        sleep(0.2)
        in_field = Select(super().wait_load_element
                          ("//div[@id='basicsearchcolumns_real']/select[@id='bas_searchfield']"))
        in_field.select_by_visible_text(item)
        Logging().reportDebugStep(self, "Select item from 'In' pick list: " + item)
        return ModuleSearchPage(self.driver)

    def click_search_now_btn(self):
        sleep(0.1)
        search_now_btn = super().wait_element_to_be_clickable("//*[@id='searchAcc']//input[@value=' Search Now ']")
        search_now_btn.click()
        Logging().reportDebugStep(self, "Click 'Search Now' button")
        self.wait_vtiger_loading_to_finish_custom(35)
        return ModuleSearchPage(self.driver)
