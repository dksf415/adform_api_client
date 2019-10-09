import json
import requests
import datetime

from adformclient.models.base import Base

class LineItem(Base):

    object = "lineItems"

    def find_by_campaign(self, id):
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.rtb.lineitem'
        url = "{}/rtb/lineitems?campaignIds={}".format(self.url_metadata, id)
        response = self.make_request("GET", url, scope)

        return self.get_response_list(response.text, response.status_code)

    def get_by_id(self, id):
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.rtb.lineitem'
        url = "{}/rtb/lineitems/{}".format(self.url_metadata, id)
        response = self.make_request("GET", url, scope)

        return self.get_response_list(response.text, response.status_code)
