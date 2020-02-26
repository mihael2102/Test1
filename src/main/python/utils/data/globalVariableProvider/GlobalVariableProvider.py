# Brand name is initialized in MultiRunner class

current_brand_name = None
current_brand_xpath_dict = None


def get_default_variable_of_current_page():
    # GET DEFAULT VARS VALUES FOR ALL PAGES
    from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider
    default_vars_dict_for_all_pages = ConfigProvider().get_default_var_dictionary()
    return default_vars_dict_for_all_pages


def get_vars_of_current_page(current_page_name):
    # Get default vars values of current page
    default_dict = get_default_variable_of_current_page()[current_page_name]

    # Get vars values of current brand. If in file there is no vars for page, return default dict 'as is'
    # without any changes
    try:
        from src.main.python.utils.data.providers.ConfigProvider import ConfigProvider
        vars_dict = ConfigProvider().get_vars_for_brand_pages()[current_page_name]
    except (TypeError, KeyError, FileNotFoundError):
        return default_dict

    # Rewrite default vars values with relevant vars values of current brand
    default_dict.update(vars_dict)
    return default_dict


# Add new brands and pages for brands here
def get_var(page_name):
    return get_vars_of_current_page(page_name)
