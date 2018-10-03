# Brand name is initialized in MultiRunner class
current_brand_name = None
current_brand_xpath_dict = None


def get_xpath_for_current_brand_element(page_name, current_test_method_name):
    if page_name == "FinancialTransactionsPage":
        if current_brand_name == "mpcrypto":
            if current_test_method_name == "test_check_searching_by_column":
                # return dictionary with elements and their xpaths for specified page and brand
                return {
                    "client_name_element": "(//td[3]/div/a)[%s]",
                    "transaction_type_element": "(//*[@id='listBody']//tr/td[4])[%s]",
                    "transaction_type_field": "(//td/div/div[1]/ul/li[1]/div/input)[1]",
                    "transaction_type_drop_down": "//td[4]/div/div[1]/button"
                }
        if current_brand_name == "testBrand":
            if current_test_method_name == "test_check_searching_by_column":
                # return dictionary with elements and their xpaths for specified page and brand
                return {
                    "transaction_type_field": "(//td/div/div[1]/ul/li[1]/div/input)[1]",
                    "transaction_type_drop_down": "//td[4]/div/div[1]/button"
                }
        # elif current_brand_name == "jonesmutual":
        #     return {
        #         "client_name_element": "(//td[3]/div/a)[%s]",
        #         "transaction_type_element": "(//*[@id='listBody']//tr/td[5])[%s]",
        #         "transaction_type_field": "(//div/div[1]/ul/li[1]/div/input)[1]",
        #         "transaction_type_drop_down": "//td[5]/div/div[1]/button"
        #     }
        # Default XPath dictionary.
        # Add here the same 'key' as you will add to brand
        else:
            return {
                "client_name_element": "(//td[3]/div/a)[%s]",
                "transaction_type_element": "(//*[@id='listBody']//tr/td[5])[%s]",
                "transaction_type_field": "(//div/div[1]/ul/li[1]/div/input)[1]",
                "transaction_type_drop_down": "//td[5]/div/div[1]/button"
            }


