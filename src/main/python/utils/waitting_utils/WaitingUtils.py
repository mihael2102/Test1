import re
from time import sleep
from pytest import fail
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging


class WaitingUtils(object):
    def __init__(self) -> None:
        super().__init__()

    def wait_until_element_present_ca(self, account, amount_crm, driver):
        for Config.counter in range(20):
            try:
                sleep(2)
                account_present = driver.find_element(By.XPATH,
                                                      "//div[@class='tbody-wrap-pandats']//td[contains(text(),'%s')]" % account)
                driver.execute_script("arguments[0].scrollIntoView();", account_present)

                account_id = account_present.text
                amount = driver.find_element(By.XPATH,
                                             "//td[contains(text(),'%s')]//following-sibling::*[3]" % account_id)

                amount_without_symbol = re.sub('[$£CA€¥]', '', amount.text)
                Logging().reportDebugStep(self, "Returns the amount \n" + amount_without_symbol + " from CA")
                if amount_without_symbol == amount_crm:
                    return amount_without_symbol
                else:
                    raise NoSuchElementException()
            except (NoSuchElementException, StaleElementReferenceException):
                sleep(10)
                driver.refresh()
        fail("There is no such element after the page reloads")

    def wait_until_element_present_crm(self, element, total_amount_crm, driver):
        for Config.counter in range(9):
            try:
                sleep(2)
                amount_present = driver.find_element(By.XPATH, element)
                amount_reg = re.sub('[$£CA€¥ [ ]', '', amount_present.text)
                Logging().reportDebugStep(self, "Returns the amount \n" + amount_reg + " from CRM")
                if amount_reg == total_amount_crm:
                    return amount_reg
                else:
                    raise NoSuchElementException()
            except (NoSuchElementException, StaleElementReferenceException):
                Logging().reportDebugStep(self, "Element is not displayed on the page or show old value. Updating page and waiting for correct value")
                sleep(10)
                driver.refresh()
        fail("There is no such element after the page reloads")

    def get_amount_by_account_text(self, account, driver):
        sleep(3)
        account_present = driver.find_element(By.XPATH,
                                              "//div[@class='tbody-wrap-pandats']//td[contains(text(),'%s')]" % account)

        driver.execute_script("arguments[0].scrollIntoView();", account_present)
        account_id = account_present.text

        amount = driver.find_element(By.XPATH,
                                     "//td[contains(text(),'%s')]//following-sibling::*[3]" % account_id)
        amount_without_symbol = re.sub('[$£CA€]', '', amount.text)

        Logging().reportDebugStep(self, "Getting the amount : " + amount_without_symbol + " from client area: ")
        return amount_without_symbol

    def wait_util_element_is_displayed(self, element, driver):
        for Config.counter in range(20):
            try:
                sleep(2)
                last_name_element = driver.find_element(By.XPATH,
                                                        "*//a[contains(text(),'%s')]" % element)

                if last_name_element.is_displayed():
                    Logging().reportDebugStep(self, "Returns the: " + element)
                    return True
                else:
                    raise NoSuchElementException()
            except (NoSuchElementException, StaleElementReferenceException):
                sleep(5)
                driver.refresh()
        fail("There is no such element after the page reloads")

    def wait_util_report_is_displayed(self, element, driver):
        for Config.counter in range(2):
            try:
                sleep(2)
                report_element = driver.find_element(By.XPATH,
                                                     "//tr[@class='tableRow'][1]//a")

                if report_element.text == element:
                    Logging().reportDebugStep(self, "Returns the: " + element)
                    return True
                else:
                    raise NoSuchElementException()
            except (NoSuchElementException, StaleElementReferenceException):
                sleep(5)
                driver.refresh()
        fail("There is no such element after the page reloads")

    def wait_until_JS_and_AJAX_are_loaded(self, driver):
        # Read the JS script from file
        with open('D:\\automation-newforexqa\\src\\test\\python\\ui\\automation\\implementation\\ca\\js_waiter_for_selenium.txt','r') as content_file:
            content = content_file.read()

        driver.execute_script(content)
