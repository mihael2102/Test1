import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class TradingConstants(object):
    ASSET_GROUP_CRYPTO = "Crypto"
    ASSET_GROUP_FAVORITES = "Favorites"
    ASSET_GROUP_FOREX = "Forex"
    ASSET_BTCEUR = "BTCEUR"
    ASSET_XRPUSD = "XRPUSD"
    VOLUME_IN_LOT_001 = "0.01"
    ORDER_ID_OPEN = ""
    ORDER_ID_CLOSED = ""
    ORDER_CREATED_TIME = ""
    CLOSED_ORDER_CREATED_TIME = ""
    ORDER_SYMBOL = ""
    CLOSED_ORDER_SYMBOL = ""
    ORDER_OPEN_PRICE = ""
    CLOSED_ORDER_OPEN_PRICE = ""
    CLOSED_ORDER_CLOSED_PRICE = ""
    CLOSED_ORDER_CLOSED_TIME = ""
    CLOSED_ORDER_PROFIT = ""
    IS_ASSET_EXIST = ""
    IS_DEMO_EXIST = ""
    TRADES_TAB_TRADE_HISTORY = "Trade History"
    TRADES_TAB_OPEN_TRADES = "Open Trades"
    LIVE_ACCOUNT_EMAIL = "pandaqa+trading_test@pandats.com"
    LIVE_ACCOUNT_PASSWORD = "q1w2e3"
    LIVE_ACCOUNT_NUMBER = "5015"
    GRAPH_TAB_5MIN = "5 Minutes"
    GRAPH_TAB_15MIN = "15 Minutes"
    GRAPH_TAB_30MIN = "30 Minutes"
    GRAPH_TAB_HOURLY = "Hourly"
    GRAPH_TAB_4HOURS = "4 Hours"
    GRAPH_TAB_DAILY = "Daily"
    GRAPH_TAB_WEEKLY = "Weekly"
    GRAPH_TAB_MONTHLY = "Monthly"
