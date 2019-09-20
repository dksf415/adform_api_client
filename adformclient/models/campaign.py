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
        creatives = []
        offset = 0
        limit = 100
        scope = 'https://api.adform.com/scope/buyer.campaigns.api'

        while True:

            url = "{}/campaigns?offset={}&limit={}&advertisers={}".format(self.url_metadata, offset, limit, id)
            response = self.make_request("GET", url, scope)
            print(response.__dict__.keys())  
            data = json.loads(response.text)
            print(data)
            if response.status_code == 200:
                for creative in response.get('data').get('response'):
                    creatives.append(creative)

            if len(creatives) < int(response.headers['Total-Count']):
                offset = offset + limit
            else:
                break


        #return self.get_response_list(response)

    def get_campaigns(self):
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.campaigns.api'
        url = "{0}/campaigns".format(self.url_metadata)
        response = self.make_request("GET", url, scope)

        return self.get_response_list(response)
    
