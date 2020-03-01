from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class QuestionnairePage(CRMBasePage):

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return QuestionnairePage(self.driver)

    def select_employment_status(self, status):
        sleep(2)
        status_item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % status)
        self.driver.execute_script("arguments[0].click();", status_item)
        Logging().reportDebugStep(self, "What’s your employment status?: " + status)
        return QuestionnairePage(self.driver)

    def select_education_level(self, level):
        level_item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % level)
        self.driver.execute_script("arguments[0].click();", level_item)
        Logging().reportDebugStep(self, "What's your level of education?: " + level)
        return QuestionnairePage(self.driver)

    def select_politically_exposed_person(self, answer):
        answer_item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", answer_item)
        Logging().reportDebugStep(self, "Are you a politically exposed person?: " + answer)
        return QuestionnairePage(self.driver)

    def select_total_annual_income(self, amount):
        amount_item = self.driver.find_element_by_xpath(
            "(//span[@class='item-pandats ng-star-inserted']/span[text()='%s'])[1]" % amount)
        self.driver.execute_script("arguments[0].click();", amount_item)
        Logging().reportDebugStep(self, "What's your Total Annual Income?: " + amount)
        return QuestionnairePage(self.driver)

    def select_approximate_net_wealth(self, amount):
        amount_item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % amount)
        self.driver.execute_script("arguments[0].click();", amount_item)
        Logging().reportDebugStep(self, "What's your approximate Net Wealth (financial instruments + cash)?: " + amount)
        return QuestionnairePage(self.driver)

    def select_expected_deposit(self, amount):
        amount_item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % amount)
        self.driver.execute_script("arguments[0].click();", amount_item)
        Logging().reportDebugStep(self, "How much do you expect to deposit in the next year with us?: " + amount)
        return QuestionnairePage(self.driver)

    def select_source_of_trading_funds(self, source):
        source_item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % source)
        self.driver.execute_script("arguments[0].click();", source_item)
        Logging().reportDebugStep(self, "What will be the main source of your trading funds?: " + source)
        return QuestionnairePage(self.driver)

    def select_why_want_trade(self, why):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % why)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Why do you want to trade?: " + why)
        return QuestionnairePage(self.driver)

    def select_react_on_losses(self, react):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % react)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "How do you think you will react if you incur trading losses?: " + react)
        return QuestionnairePage(self.driver)

    def click_next_btn(self):
        sleep(0.2)
        next_btn = super().wait_element_to_be_clickable("//button[text()=' Next ']")
        next_btn.click()
        Logging().reportDebugStep(self, "NEXT button clicked")
        return QuestionnairePage(self.driver)

    def select_instruments_traded_before(self, instrument):
        sleep(1)
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % instrument)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Which of the following instruments have you traded before?: " + instrument)
        return QuestionnairePage(self.driver)

    def select_average_frequency(self, answer):
        sleep(1)
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Average frequency of your annual past transactions: " + answer)
        return QuestionnairePage(self.driver)

    def select_trade_size(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Average trade size (volume) of your annual past transactions: " + answer)
        return QuestionnairePage(self.driver)

    def select_common_level(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Common level of leverage used: " + answer)
        return QuestionnairePage(self.driver)

    def select_if_applicable(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Please select if applicable: " + answer)
        return QuestionnairePage(self.driver)

    def select_correct_regarding_cfd(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Which of the following is correct regarding "
                                        "Contracts for Difference (CFDs)?: " + answer)
        return QuestionnairePage(self.driver)

    def select_factor_affect_prices(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "What is the main factor that can affect the prices of the underlying currency "
                                        "exchange (forex) markets?: " + answer)
        return QuestionnairePage(self.driver)

    def select_close_bmw_position(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "If you open a position on the BMW share "
                                        "through our platform, where can you close it?: " + answer)
        return QuestionnairePage(self.driver)

    def select_required_margin(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "What would be the required margin to open a CFD of 1 Lot (€100,000) "
                                        "on EUR/USD, assuming your leverage is 1:100 (i.e. margin 1%)?: " + answer)
        return QuestionnairePage(self.driver)

    def select_loss(self, answer):
        item = self.driver.find_element_by_xpath(
            "//span[@class='item-pandats ng-star-inserted']/span[text()='%s']" % answer)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "A Trader has a trading capital/equity of €10,000 and opens a CFD position on "
                                        "EUR/USD at 1.1000. What will be the loss when the price moves against the "
                                        "Trader by 10 pips if the pip value is €45 and the leverage is 1:50: " + answer)
        return QuestionnairePage(self.driver)

    def verify_questionnaire_message(self, expected_msg):
        sleep(1)
        actual_msg = super().wait_load_element("//div[@class='negative-scoring-pandats']").text
        assert expected_msg == actual_msg
        Logging().reportDebugStep(self, "Message is verified: " + actual_msg)
        return QuestionnairePage(self.driver)

    def close_questionnaire_message(self):
        sleep(1)
        self.wait_element_to_be_disappear("//div[contains(@class,'spinner')]")
        sleep(0.1)
        close_btn = super().wait_load_element("//div[@class='close-pandats cmicon-close3']")
        close_btn.click()
        Logging().reportDebugStep(self, "Message is closed")
        return QuestionnairePage(self.driver)

    def select_item_pick_list(self, question, answer):
        sleep(0.1)
        item = super().wait_load_element(
            "//label[text()='%s']//following-sibling::custom-select//div[@class='wrap-list-pandats ng-star-inserted']/"
            "span/span[text()='%s']" % (question, answer))
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, question + ": " + answer)
        return QuestionnairePage(self.driver)
