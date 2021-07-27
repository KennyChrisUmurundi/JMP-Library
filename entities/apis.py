import logging
from urllib3.exceptions import (
    ConnectionError,
    NewConnectionError,
    MaxRetryError,
    TimeoutError,
)

logger = logging.getLogger(__name__)

fedex_test_key = '3kWyadILwhnan9fW'
Test_FedEx_Office_Integrator_ID=123
Test_Client_Product_ID='TEST'
Test_Client_Product_Version=9999 

def get_api_urls():
    """
    URL Links by the API
    Return:
        dict: A dictionary of all links provided by the API
    """
    return {"wsdl": "https://test.payway.bi/avs/services/external/v3?wsdl"}


def paypal_pay():
    pass


class FedexPlugin():

    def fedex_print(file,url):
        pass
