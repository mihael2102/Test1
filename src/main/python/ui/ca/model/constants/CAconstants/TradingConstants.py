import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class TradingConstants(object):
    ASSET_GROUP_CRYPTO = "Crypto"
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
