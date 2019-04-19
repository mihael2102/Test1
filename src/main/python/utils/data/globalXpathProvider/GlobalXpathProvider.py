# Brand name is initialized in MultiRunner class

current_brand_name = None
current_brand_xpath_dict = None

def __get_default_xpath_of_elements_of_current_page():
    # GET DEFAULT XPATH VALUES FOR ALL PAGES
    from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider
    default_xpath_dict_for_all_pages = ConfigProvider().get_default_xpath_dictionary()
    return default_xpath_dict_for_all_pages

def __get_xpath_of_elements_of_current_page(current_page_name):
    # Get default xpath values for elements of current page
    FinancialTransactionsPage_default_dict = __get_default_xpath_of_elements_of_current_page()[current_page_name]

    # Get xpath values for elements of current brand. If in file there is no xpath for page, return default dict 'as is'
    # without any changes
    try:
        from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider
        FinancialTransactionsPage_mpcrypto_xpath_dict = ConfigProvider().get_xpath_for_brand_pages()[current_page_name]
    except TypeError:
        return FinancialTransactionsPage_default_dict

    # Rewrite default xpath values with relevant xpath values of current brand
    FinancialTransactionsPage_default_dict.update(FinancialTransactionsPage_mpcrypto_xpath_dict)
    return FinancialTransactionsPage_default_dict

# Add new brands and pages for brands here
def get_xpath_for_current_brand_element(page_name):

    if current_brand_name == "coinstec_ca":
        if page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "sitalix_ca":
        if page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "tradospot_ca":
        if page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "firstindex_ca":
        if page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "ptbanc_ca":
        if page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    # elif current_brand_name == "q8trade_ca":
    #     if page_name == "CALoginPage":
    #         return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "2mercados_ca":
        if page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "mpcrypto":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CAPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "newforexstaging":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "newrichmarkets":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "forexbestmarket":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "solocapitals":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "lq-fx":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "optionstars":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "24btcmarket":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "jonesmutual":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "goldenmarkets":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "safemarkets":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "uft":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "brokerz":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "4xfx":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "herdos":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "ptbanc":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "WebTraderPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CAPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "royal_cfds":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "intelligent_capital":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "FXMarketPro":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "q8":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CAPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "axa_markets":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "xtraderfx":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "coinstec":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "marketsplus":
        if page_name == "TasksPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "ClientProfilePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "2mercados":
        if page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "firstindex":
        if page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "hizlifx":
        if page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "olympusmarkets":
        if page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "privat-trade":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "swiftcfd":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "tfxgo":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)


    elif current_brand_name == "eafx":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "gxfx":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "b-finance":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)
        elif page_name == "CALoginPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "uprofx":
        if page_name == "AffiliatePage":
            return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "aztrades":
        if page_name == "ClientsPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    return __get_default_xpath_of_elements_of_current_page()[page_name]
