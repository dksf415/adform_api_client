import json
import requests
import datetime

from adformclient.models.base import Base

class Campaign(Base):

    object = "campaigns"

    def find_by_id(self, id):
        pass

    def find_by_advertiser(self, id):
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.campaigns.api'
        url = "{0}/campaigns?advertisers={1}".format(self.url_metadata, id)
        print('API URL: {}'.format(url))
        response = self.make_request("GET", url, scope)

        return self.get_response_list(response)

    def get_campaigns(self):
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.campaigns.api'
        url = "{0}/campaigns".format(self.url_metadata)
        response = self.make_request("GET", url, scope)

        return self.get_response_list(response)
    
