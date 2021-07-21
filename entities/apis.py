import logging
from urllib3.exceptions import ConnectionError, NewConnectionError, MaxRetryError, TimeoutError


logger = logging.getLogger(__name__)


def get_api_urls():
    """
    URL Links by the API
    Return:
        dict: A dictionary of all links provided by the API
    """
    return {"wsdl": "https://test.payway.bi/avs/services/external/v3?wsdl"}

def paypal_pay():
    pass
