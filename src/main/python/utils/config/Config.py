from src.main.python.utils.data.providers.DataProviders import DataProviders

timeout = 4
data = None  # DataProviders()
url_client_area = "https://newforexqa.pandats.com/"
url_crm = "https://newforexstaging.ptscrm.com/"
url_gmail = "https://mail.google.com"
url_api_general = "https://newforexqa.pandats-api.io"
url_api_authorization = url_api_general + "/api/v3/authorization"   # POST
url_api_create_client = url_api_general + "/api/v3/customers"       # POST
window_after = None
window_before = None
counter = 1
logger = None
handler = None
