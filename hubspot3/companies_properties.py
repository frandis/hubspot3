"""
hubspot companies properties api
"""
from hubspot3.base import BaseClient
from hubspot3.utils import get_log
from typing import List, Optional, Union


COMPANIES_PROPERTIES_API_VERSION = "1"


class CompaniesPropertiesClient(BaseClient):
    """
    The hubspot3 Companies Properties client uses the _make_request method to call the
    API for data.  It returns a python object translated from the json returned.
    """

    def __init__(self, *args, **kwargs):
        """initialize an companies properties client"""
        super(CompaniesPropertiesClient, self).__init__(*args, **kwargs)
        self.log = get_log("hubspot3.companies_properties")

    def _get_path(self, subpath: str) -> str:
        return "properties/v{}/companies/{}".format(
            COMPANIES_PROPERTIES_API_VERSION, subpath
        )

    def get_all_companies_properties(
        self, extra_properties: Union[str, List] = None, **options
    ) -> Optional[List]:
        """
        Retrieve all of the company properties, including their definition, for a given account.
        :see: https://developers.hubspot.com/docs/methods/companies/get_company_properties
        """
        return self._call(
            "properties".format(COMPANIES_PROPERTIES_API_VERSION), **options
        )
