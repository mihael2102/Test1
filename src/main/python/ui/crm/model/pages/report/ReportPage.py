from time import sleep

from selenium.webdriver import ActionChains

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.report.PerformanceByDate import PerformanceByDate
from src.main.python.utils.logs.Loging import Logging


class ReportPage(CRMBasePage):

    def __init__(self):
        super().__init__()

    def switch_first_tab_page(self):
        super().switch_first_window_page()
        return ReportPage()

    def open_performance_report_by_date_page(self, report):
        hover_mouse = ActionChains(self.driver)
        more_list_element = super().wait_element_to_be_clickable("//a[contains(text(),'Management Reports')]")
        hover_mouse.move_to_element(more_list_element)
        hover_mouse.perform()
        sleep(2)
        report_element = super().wait_element_to_be_clickable(
            "//ul[@class='dropdown-menu']//li//a[contains(text(),'%s')]" % report)
        report_element.click()
        Logging().reportDebugStep(self, "The report was opened : " + report)
        return PerformanceByDate()
