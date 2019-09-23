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
        scope = 'https://api.adform.com/scope/buyer.campaigns.api'
        url = "{0}/fastlineitems".format(self.url_metadata)
        payload = {'campaignId': id}
        response = self.make_request("POST", url, scope, json.dumps(payload))

        return self.get_response_list(response.text, response.status_code)

        pass
