import json
import requests
import datetime

from adformclient.models.base import Base

class Campaign(Base):

    object = "campaigns"
    scope = 'https://api.adform.com/scope/buyer.campaigns.api'

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

        while True:

            url = "{}/campaigns?subtypes=Rtb&offset={}&limit={}&advertisers={}".format(self.url_metadata, offset, limit, id)
            response = self.make_request("GET", url, self.scope)

            if response.status_code == 200:

                # Not enough records to paginate
                if int(response.headers['Total-Count']) == 0 or int(response.headers['Total-Count']) <= limit:
                    return self.get_response_list(response.text, response.status_code)
                else:
                    creative_data = json.loads(response.text)
                    for creative in creative_data:
                        creatives.append(creative)

            if len(creatives) < int(response.headers['Total-Count']):
                offset = offset + limit
            else:
                break

        return self.get_response_list(json.dumps(creatives), response.status_code)

    def get_campaigns(self):
        """

        :param id:
        :return: JSON array
        """
        url = "{0}/campaigns?subtypes=Rtb".format(self.url_metadata)
        response = self.make_request("GET", url, self.scope)

        return self.get_response_list(response)
    
