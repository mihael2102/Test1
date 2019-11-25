from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants


class Trading_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def close_order(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login()
        if global_var.current_brand_name == "ptbanc":
            WebTraderPage(self.driver).ptbanc_webtrader()
        first_id_order = WebTraderPage(self.driver).get_id_order()
        WebTraderPage(self.driver).click_close_order()
        WebTraderPage(self.driver).close_pop_up_close_trade(CRMConstants.YES)
        second_id_order = WebTraderPage(self.driver).get_id_order()
        assert first_id_order != second_id_order

    def edit_order_stop_loss_take_profit(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.FIRST_NAME])
            CAPage(self.driver).open_manage_accounts() \
                               .open_demo_section() \
                               .open_new_account_btn() \
                               .select_account_type(CAConstants.ACCOUNT_DEMO)

            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).select_currency(CAConstants.CURRENCY_CRYPTO)
            else:
                CAPage(self.driver).select_currency(CAConstants.CURRENCY)

            if (global_var.current_brand_name == "swiftcfd") or (global_var.current_brand_name == "jonesmutual")\
                    or (global_var.current_brand_name == "royal_cfds"):
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL2)
            else:
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL)

            CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT0) \
                               .verify_init_deposit_error() \
                               .set_initial_deposit(CAConstants.INITIAL_DEPOSIT1) \
                               .verify_init_deposit_error()
            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT_BTC)
            elif global_var.current_brand_name == "ptbanc":
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT_PTBANC)
            else:
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT)
            CAPage(self.driver).click_create_account()
            account_number = WebTraderPage(self.driver).get_number_account()
            number1 = account_number.replace('#', '')
            number2 = number1.replace('DEMO', '')
            CAPage(self.driver).click_close_client_area()
            WebTraderPage(self.driver).click_select_account() \
                .select_demo_account_by_number(number2)
            WebTraderPage(self.driver).select_asset(CRMConstants.ASSET_M)
            WebTraderPage(self.driver).select_volume_in_lot(CRMConstants.VOLUME_FUNDS)
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
            if global_var.current_brand_name != "ptbanc":
                number = WebTraderPage(self.driver).check_hight_low()
                WebTraderPage(self.driver).click_submit_changes()
                check_stop_loss_in_table = WebTraderPage(self.driver).check_stop_loss_in_table()
                assert check_stop_loss_in_table == number

    def open_order_stop_loss_take_profit(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.FIRST_NAME])
            CAPage(self.driver).open_manage_accounts() \
                               .open_demo_section() \
                               .open_new_account_btn() \
                               .select_account_type(CAConstants.ACCOUNT_DEMO)

            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).select_currency(CAConstants.CURRENCY_CRYPTO)
            else:
                CAPage(self.driver).select_currency(CAConstants.CURRENCY)

            if (global_var.current_brand_name == "swiftcfd") or (global_var.current_brand_name == "jonesmutual")\
                    or (global_var.current_brand_name == "royal_cfds"):
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL2)
            else:
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL)

            CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT0) \
                               .verify_init_deposit_error() \
                               .set_initial_deposit(CAConstants.INITIAL_DEPOSIT1) \
                               .verify_init_deposit_error()
            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT_BTC)
            elif global_var.current_brand_name == "ptbanc":
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT_PTBANC)
            else:
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT)
            CAPage(self.driver).click_create_account()
            CAPage(self.driver).click_close_client_area()
            # WebTraderPage(self.driver).click_select_account() \
            #     .select_demo_account_by_number(account_number)
            account_number = WebTraderPage(self.driver).get_number_account()
            number1 = account_number.replace('#', '')
            number2 = number1.replace('DEMO', '')
            if global_var.current_brand_name == "ptbanc":
                WebTraderPage(self.driver).ptbanc_webtrader()

            WebTraderPage(self.driver).select_asset(CRMConstants.ASSET_M)
            WebTraderPage(self.driver).select_volume_in_lot(CRMConstants.VOLUME_FUNDS)
            pips_right_panel = WebTraderPage(self.driver).check_pips_right_panel()
            WebTraderPage(self.driver).click_sell()
            WebTraderPage(self.driver).click_invest()
            # order = WebTraderPage(self.driver).get_msg_succsessfull_order()
            # assert CRMConstants.ORDER in order

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
            ClientProfilePage(self.driver).click_link_trading_account(number2)

            equity = ClientProfilePage(self.driver).get_equity_text()
            open_p_l = ClientProfilePage(self.driver).get_open_p_l_text()
            balance = ClientProfilePage(self.driver).get_balance()

            v1 = account_value_number.replace('.', '')
            v2 = v1.replace(',', '')
            v3 = v2.replace('€', '')

            e1 = equity.replace('.', '')
            e2 = e1.replace(',', '')

            result = int(v3) - int(e2)
            result1 = float(open_p_l_number.replace('-€', '').replace(',', '')) - float(
                open_p_l.replace('-', '').replace(',', ''))
            result2 = float(margin_level_number.replace('%', '').replace(',', '')) - float(
                margin_lvl.replace('%', '').replace(',', ''))

            assert -5000 <= result <= 5000
            assert -100 <= result1 <= 100
            assert -100 <= result2 <= 100

    def trade_with_insufficient_funds(self):

        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login()
        CAPage(self.driver)\
            .open_accounts_list()\
            .switch_to_account(CAConstants.DEMO_ACCOUNT_NUMBER, CAConstants.ACCOUNT_DEMO)
        if global_var.current_brand_name == "ptbanc":
            WebTraderPage(self.driver)\
                .ptbanc_webtrader()

        WebTraderPage(self.driver)\
            .select_asset(CRMConstants.ASSET)
        WebTraderPage(self.driver)\
            .select_volume_in_lot(CRMConstants.VOLUME_INSUFFICIENT_FUNDS)\
            .click_sell()\
            .click_invest()\
            .check_msg_insufficient_funds()

    def open_order_buy_sell(self):

        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login()
        # CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        # CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
        #                                          LeadsModuleConstants.EMAIL]) \
        #     .enter_password(CAConstants.PASSWORD) \
        #     .click_login()
        # ca_balance = CAPage(self.driver).get_balance()
        # CAPage(self.driver).click_actions_launch()
        # WebTraderPage(self.driver).click_select_account() \
        #     .select_demo_account()
        if global_var.current_brand_name == "ptbanc":
            WebTraderPage(self.driver).ptbanc_webtrader()
        WebTraderPage(self.driver).select_asset(CRMConstants.ASSET_M)
        WebTraderPage(self.driver).select_volume_in_lot(CRMConstants.VOLUME_FUNDS) \
            .click_sell() \
            .click_invest()
        order = WebTraderPage(self.driver).get_msg_succsessfull_order()

        assert CRMConstants.ORDER in order
        WebTraderPage(self.driver).choose_asset(CRMConstants.ASSET_M)
        WebTraderPage(self.driver).select_volume_in_lot(CRMConstants.VOLUME_FUNDS) \
            .click_buy() \
            .click_invest()
        order = WebTraderPage(self.driver).get_msg_succsessfull_order()

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
        number1 = number.replace('#', '')
        number2 = number1.replace('DEMO', '')
        ClientProfilePage(self.driver).click_link_trading_account(number2)
        ClientProfilePage(self.driver).click_display_open_transactions()

        # type_transaction = ClientProfilePage(self.driver).get_type_transaction()
        # size_transaction = ClientProfilePage(self.driver).get_size_transaction()
        # symbol_transaction = ClientProfilePage(self.driver).get_symbol_transaction()
        #
        # assert type_transaction == CRMConstants.TYPE_TRANSACTIONS
        # assert size_transaction == CRMConstants.SIZE_TRANSACTIONS
        # assert symbol_transaction == CRMConstants.SYMBOL_TRANSACTIONS

        ClientProfilePage(self.driver).click_close_display_transactions()

        equity = ClientProfilePage(self.driver).get_equity_text()
        open_p_l = ClientProfilePage(self.driver).get_open_p_l_text()
        balance = ClientProfilePage(self.driver).get_balance()

        # assert ca_balance.replace('.', '') == balance.replace(',', '').replace('.', '')

        v1 = account_value_number.replace('.','')
        v2 = v1.replace(',', '')
        v3 = v2.replace('€','')

        e1 = equity.replace('.','')
        e2 = e1.replace(',', '')

        result = int(v3) - int(e2)

        assert -5000 <= result <= 5000
        assert CRMConstants.ORDER in order

    def trading_process_open_position_ca(self):
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .login()\
            .enter_email(CAConstants.EMAIL_CA)\
            .enter_password(CAConstants.PASSWORD)\
            .click_login()\
            .verify()

        # Check if demo account and crypto position was opened
        try:
            assert TradingConstants.IS_DEMO_EXIST == "yes"
            Logging().reportDebugStep(self, "DEMO account was opened")
        except:
            if TradingConstants.IS_DEMO_EXIST == "no":
                Logging().reportDebugStep(self, "There is no DEMO account")
                assert TradingConstants.IS_DEMO_EXIST == "yes"

        CAPage(self.driver)\
            .open_accounts_list()\
            .switch_to_account(CAConstants.DEMO_ACCOUNT_NUMBER, CAConstants.ACCOUNT_DEMO)\
            .open_accounts_list()\
            .verify_active_account_number(CAConstants.DEMO_ACCOUNT_NUMBER)
        WebTraderPage(self.driver)\
            .open_trading_page()\
            .open_asset_group(TradingConstants.ASSET_GROUP_CRYPTO)\
            .select_asset(TradingConstants.ASSET_XRPUSD)\
            .select_volume_in_lot(TradingConstants.VOLUME_IN_LOT_001)\
            .click_buy()\
            .click_invest()\
            .get_msg_succsessfull_order()\
            .close_succsessfull_order_popup()\
            .get_id_order()\
            .get_order_created_time()\
            .get_symbol()\
            .get_open_price()

    def verify_open_position_crm(self):
        # Login CRM
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(CAConstants.EMAIL_CA)

        # Check if demo account and crypto position was opened
        try:
            assert TradingConstants.IS_DEMO_EXIST == "yes" and \
                   TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            if TradingConstants.IS_DEMO_EXIST == "no":
                Logging().reportDebugStep(self, "There is no DEMO account")
                assert TradingConstants.IS_DEMO_EXIST == "yes"
            elif TradingConstants.IS_ASSET_EXIST == "no":
                Logging().reportDebugStep(self, "There is no crypto assets")
                assert TradingConstants.IS_ASSET_EXIST == "yes"

        # Open demo account details and get open orders data
        open_orders_data = ClientProfilePage(self.driver)\
            .perform_scroll_down()\
            .open_trading_accounts_tab()\
            .open_trading_account_by_number(CAConstants.DEMO_ACCOUNT_NUMBER)\
            .click_display_open_transactions()\
            .get_open_orders_data()

        expected_order_id = TradingConstants.ORDER_ID_OPEN.replace('#', '')
        expected_created_time_order = TradingConstants.ORDER_CREATED_TIME.split(' ')
        expected_date = expected_created_time_order[0].split('/')
        expected_date = "20" + expected_date[2] + "-" + expected_date[1] + "-" + expected_date[0]
        expected_time = expected_created_time_order[1]
        expected_symbol = TradingConstants.ORDER_SYMBOL
        expected_open_price = TradingConstants.ORDER_OPEN_PRICE

        assert expected_order_id in open_orders_data
        assert expected_date in open_orders_data
        assert expected_time in open_orders_data
        assert expected_symbol in open_orders_data
        assert expected_open_price in open_orders_data

    def trading_process_close_position_ca(self):
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .login() \
            .enter_email(CAConstants.EMAIL_CA) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login() \
            .verify()

        # Check if demo account and crypto position was opened
        try:
            assert TradingConstants.IS_DEMO_EXIST == "yes" and \
                   TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            if TradingConstants.IS_DEMO_EXIST == "no":
                Logging().reportDebugStep(self, "There is no DEMO account")
                assert TradingConstants.IS_DEMO_EXIST == "yes"
            elif TradingConstants.IS_ASSET_EXIST == "no":
                Logging().reportDebugStep(self, "There is no crypto assets")
                assert TradingConstants.IS_ASSET_EXIST == "yes"

        CAPage(self.driver) \
            .open_accounts_list() \
            .switch_to_account(CAConstants.DEMO_ACCOUNT_NUMBER, CAConstants.ACCOUNT_DEMO) \
            .open_accounts_list() \
            .verify_active_account_number(CAConstants.DEMO_ACCOUNT_NUMBER)
        WebTraderPage(self.driver) \
            .open_trading_page()\
            .click_close_order()\
            .close_pop_up_close_trade(CRMConstants.YES)\
            .close_succsessfull_order_popup()\
            .open_trade_tab(TradingConstants.TRADES_TAB_TRADE_HISTORY)\
            .get_id_closed_order()\
            .get_closed_order_created_time()\
            .get_closed_order_symbol()\
            .get_closed_order_open_price()\
            .get_closed_order_closed_price()\
            .get_closed_order_closed_time()\
            .get_closed_order_profit()

    def verify_close_position_crm(self):
        # Login CRM
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(CAConstants.EMAIL_CA)

        # Check if demo account and crypto position was opened
        try:
            assert TradingConstants.IS_DEMO_EXIST == "yes" and \
                   TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            if TradingConstants.IS_DEMO_EXIST == "no":
                Logging().reportDebugStep(self, "There is no DEMO account")
                assert TradingConstants.IS_DEMO_EXIST == "yes"
            elif TradingConstants.IS_ASSET_EXIST == "no":
                Logging().reportDebugStep(self, "There is no crypto assets")
                assert TradingConstants.IS_ASSET_EXIST == "yes"

        # Open demo account details and get open orders data
        close_orders_data = ClientProfilePage(self.driver)\
            .perform_scroll_down()\
            .open_trading_accounts_tab()\
            .open_trading_account_by_number(CAConstants.DEMO_ACCOUNT_NUMBER)\
            .open_closed_transactions_tab()\
            .get_closed_order_data()

        # Verify data of closed trade:
        expected_order_id = TradingConstants.ORDER_ID_CLOSED.replace('#', '')
        expected_created_time_order = TradingConstants.CLOSED_ORDER_CREATED_TIME.split(' ')
        expected_date = expected_created_time_order[0].split('/')
        expected_date = expected_date[2] + "-" + expected_date[1] + "-" + expected_date[0]
        expected_time = expected_created_time_order[1]
        expected_symbol = TradingConstants.CLOSED_ORDER_SYMBOL
        expected_open_price = TradingConstants.CLOSED_ORDER_OPEN_PRICE
        while expected_open_price.endswith('0'):
            expected_open_price = expected_open_price[:-1]
        expected_closed_time_order = TradingConstants.CLOSED_ORDER_CLOSED_TIME.split(' ')
        expected_closed_order_date = expected_closed_time_order[0].split('/')
        expected_closed_order_date = expected_closed_order_date[2] + "-" + expected_closed_order_date[1] + "-" \
                                     + expected_closed_order_date[0]
        expected_closed_order_time = expected_closed_time_order[1]
        expected_closed_price = TradingConstants.CLOSED_ORDER_CLOSED_PRICE
        while expected_closed_price.endswith('0'):
            expected_closed_price = expected_closed_price[:-1]
        expected_profit = TradingConstants.CLOSED_ORDER_PROFIT.replace('€', '')

        assert expected_order_id in close_orders_data
        assert expected_date in close_orders_data
        assert expected_time in close_orders_data
        assert expected_symbol in close_orders_data
        assert expected_open_price in close_orders_data
        assert expected_closed_order_date in close_orders_data
        assert expected_closed_order_time in close_orders_data
        assert expected_closed_price in close_orders_data
        assert expected_profit in close_orders_data
