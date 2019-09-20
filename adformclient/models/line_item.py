import json
import requests
import datetime

from adformclient.models.base import Base

class LineItem(Base):

    object = "lineItems"

    def find_by_insertion_order(self, id):
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.direct.lineitems'
        url = "{0}/orders?campaignId={1}".format(self.url_metadata, id)
        response = self.make_request("GET", url, scope)

        return self.get_response_list(response)

        pass
