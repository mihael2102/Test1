from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.pages.ca.CAPage import CAPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage


class Trading_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def edit_order_stop_loss_take_profit(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_demo_account()
        CAPage(self.driver).select_currency()
        CAPage(self.driver).select_leverage()
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "finmarket" and global_var.current_brand_name != "itrader_global":
            CAPage(self.driver).select_deposit()
        CAPage(self.driver).click_submit()
        if global_var.current_brand_name != "triomarkets" and global_var.current_brand_name != "itrader" and global_var.current_brand_name != "finmarket":
            account_number = CAPage(self.driver).get_account_number()
            CAPage(self.driver).finish_button()
            CAPage(self.driver).click_actions_launch_by_account(account_number)
            WebTraderPage(self.driver).select_asset()
            WebTraderPage(self.driver).select_volume_in_lot()
            pips_right_panel = WebTraderPage(self.driver).check_pips_right_panel()
            WebTraderPage(self.driver).click_sell()
            WebTraderPage(self.driver).click_invest()
            order = WebTraderPage(self.driver).get_msg_succsessfull_order()
            assert CRMConstants.ORDER in order
            WebTraderPage(self.driver).click_stop_loss()

            WebTraderPage(self.driver).check_button_set_stop_loss()
            WebTraderPage(self.driver).enter_stop_loss(CRMConstants.STOP_LOSS)
            pips = WebTraderPage(self.driver).check_pips_stop_loss()
            assert CRMConstants.PIPS_CONTAINS in pips
            number = WebTraderPage(self.driver).check_hight_low()
            WebTraderPage(self.driver).click_submit_changes()
            check_stop_loss_in_table = WebTraderPage(self.driver).check_stop_loss_in_table()
            assert check_stop_loss_in_table == number


    def open_order_stop_loss_take_profit(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_demo_account()
        CAPage(self.driver).select_currency()
        CAPage(self.driver).select_leverage()
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "finmarket" and global_var.current_brand_name != "itrader_global":
            CAPage(self.driver).select_deposit()
        CAPage(self.driver).click_submit()
        if global_var.current_brand_name != "triomarkets" and global_var.current_brand_name != "itrader" and global_var.current_brand_name != "finmarket":
            account_number = CAPage(self.driver).get_account_number()
            CAPage(self.driver).finish_button()
            CAPage(self.driver).click_actions_launch_by_account(account_number)
            WebTraderPage(self.driver).select_asset()
            WebTraderPage(self.driver).select_volume_in_lot()
            pips_right_panel = WebTraderPage(self.driver).check_pips_right_panel()
            WebTraderPage(self.driver).click_sell()
            WebTraderPage(self.driver).click_invest()
            order = WebTraderPage(self.driver).get_msg_succsessfull_order()
            assert CRMConstants.ORDER in order

            avaliable_funds_number = WebTraderPage(self.driver).check_avaliable_funds_number()
            used_funds_number = WebTraderPage(self.driver).check_used_funds_number()
            account_value_number = WebTraderPage(self.driver).check_account_value_number()
            open_p_l_number = WebTraderPage(self.driver).check_total_p_l_number()
            margin_level_number = WebTraderPage(self.driver).check_margin_level_number()

            pips_bottom_panel = WebTraderPage(self.driver).check_pips_bottom_panel()
            assert pips_right_panel == pips_bottom_panel

            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET)) \
                .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

            sleep(2)
            ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.EMAIL])
            ClientProfilePage(self.driver).open_trading_accounts_tab()
            margin_lvl = ClientProfilePage(self.driver).get_last_margin_lvl()
            open_p_l = ClientProfilePage(self.driver).get_open_p_l()
            equity_trading_funds = ClientProfilePage(self.driver).get_equity_trading_accounts()
            ClientProfilePage(self.driver).click_link_trading_account(account_number)

            equity = ClientProfilePage(self.driver).get_equity_text()
            open_p_l = ClientProfilePage(self.driver).get_open_p_l_text()
            balance = ClientProfilePage(self.driver).get_balance()

            v1 = account_value_number.replace('.', '')
            v2 = v1.replace(',', '')
            v3 = v2.replace('€', '')

            e1 = equity.replace('.', '')
            e2 = e1.replace(',', '')

            result = int(v3) - int(e2)
            result1 = float(open_p_l_number.replace('-€','').replace(',','')) - float(open_p_l.replace('-','').replace(',',''))
            result2 = float(margin_level_number.replace('%','').replace(',','')) - float(margin_lvl.replace('%','').replace(',',''))

            assert -5000 <= result <= 5000
            assert -10 <= result1 <= 10
            assert -2 <= result2 <= 2








    def trade_with_insufficient_funds(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()
        ca_balance = CAPage(self.driver).get_balance()
        CAPage(self.driver).click_actions_launch()
        avaliable_funds_int = WebTraderPage(self.driver).get_avaliable_funds()
        avaliable_funds_int1 = avaliable_funds_int.replace('.','')
        assert ca_balance.replace('.','') in avaliable_funds_int1.replace(',', '')
        avaliable_funds = WebTraderPage(self.driver).check_avaliable_funds()
        used_funds = WebTraderPage(self.driver).check_used_funds()
        account_value = WebTraderPage(self.driver).check_account_value()
        total_p_l = WebTraderPage(self.driver).check_total_p_l()
        margin_level = WebTraderPage(self.driver).check_margin_level()
        assert avaliable_funds == CAConstants.AVALIABLE_FUNDS
        assert used_funds == CAConstants.USED_FUNDS
        assert account_value == CAConstants.ACCOUNT_VALUE
        assert total_p_l == CAConstants.TOTAL_P_L
        assert margin_level == CAConstants.MARGIN_LVL
        WebTraderPage(self.driver).select_asset()
        WebTraderPage(self.driver).select_volume_in_lot()\
                                  .click_sell()\
                                  .click_invest()
        order = WebTraderPage(self.driver).get_msg_succsessfull_order()
        assert CRMConstants.ORDER in order


    def open_order_buy_sell(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()
        ca_balance = CAPage(self.driver).get_balance()
        CAPage(self.driver).click_actions_launch()


        WebTraderPage(self.driver).select_volume_in_lot() \
            .click_sell() \
            .click_invest()
        order = WebTraderPage(self.driver).get_msg_succsessfull_order()
        assert CRMConstants.ORDER in order
        WebTraderPage(self.driver).choose_asset()
        WebTraderPage(self.driver).select_volume_in_lot() \
            .click_buy() \
            .click_invest()
        order = WebTraderPage(self.driver).get_msg_succsessfull_order()
        assert CRMConstants.ORDER in order

        avaliable_funds_number = WebTraderPage(self.driver).check_avaliable_funds_number()
        used_funds_number = WebTraderPage(self.driver).check_used_funds_number()
        account_value_number = WebTraderPage(self.driver).check_account_value_number()
        total_p_l_number = WebTraderPage(self.driver).check_total_p_l_number()
        margin_level_number = WebTraderPage(self.driver).check_margin_level_number()
        number = WebTraderPage(self.driver).get_number_account()
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        ClientProfilePage(self.driver).open_trading_accounts_tab()
        ClientProfilePage(self.driver).click_link_trading_account(number)
        ClientProfilePage(self.driver).click_display_open_transactions()

        type_transaction = ClientProfilePage(self.driver).get_type_transaction()
        size_transaction = ClientProfilePage(self.driver).get_size_transaction()
        symbol_transaction = ClientProfilePage(self.driver).get_symbol_transaction()

        assert type_transaction == CRMConstants.TYPE_TRANSACTIONS
        assert size_transaction == CRMConstants.SIZE_TRANSACTIONS
        assert symbol_transaction == CRMConstants.SYMBOL_TRANSACTIONS

        ClientProfilePage(self.driver).click_close_display_transactions()

        equity = ClientProfilePage(self.driver).get_equity_text()
        open_p_l = ClientProfilePage(self.driver).get_open_p_l_text()
        balance = ClientProfilePage(self.driver).get_balance()

        assert ca_balance.replace('.', '') == balance.replace(',', '').replace('.', '')

        v1 = account_value_number.replace('.','')
        v2 = v1.replace(',', '')
        v3 = v2.replace('€','')

        e1 = equity.replace('.','')
        e2 = e1.replace(',', '')

        result = int(v3) - int(e2)

        assert -5000 <= result <= 5000











