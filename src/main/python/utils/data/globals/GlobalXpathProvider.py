# Brand name is initialized in MultiRunner class
from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider

current_brand_name = None
current_brand_xpath_dict = None


def __get_default_xpath_of_elements_of_current_page():
    # GET DEFAULT XPATH VALUES FOR ALL PAGES
    default_xpath_dict_for_all_pages = ConfigProvider().get_default_xpath_dictionary()
    return default_xpath_dict_for_all_pages

def __get_xpath_of_elements_of_current_page(current_page_name):
    # Get default xpath values for elements of current page
    FinancialTransactionsPage_default_dict = __get_default_xpath_of_elements_of_current_page[current_page_name]

    # Get xpath values for elements of current brand. If in file there is no xpath for page, return default dict 'as is'
    # without any changes
    try:
        FinancialTransactionsPage_mpcrypto_xpath_dict = ConfigProvider().get_xpath_for_brand_pages()[current_page_name]
    except TypeError:
        return FinancialTransactionsPage_default_dict

    # Rewrite default xpath values with relevant xpath values of current brand
    FinancialTransactionsPage_default_dict.update(FinancialTransactionsPage_mpcrypto_xpath_dict)
    return FinancialTransactionsPage_default_dict

# Add new brands and pages for brands here
def get_xpath_for_current_brand_element(page_name):
    if current_brand_name == "mpcrypto":
        if page_name == "FinancialTransactionsPage":
           return __get_xpath_of_elements_of_current_page(page_name)

    elif current_brand_name == "newforexstaging":
        if page_name == "FinancialTransactionsPage":
            return __get_xpath_of_elements_of_current_page(page_name)

    else:
        return __get_default_xpath_of_elements_of_current_page()[page_name]
