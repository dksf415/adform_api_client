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
        url = "{0}/campaigns/{1}".format(self.url_metadata, id)
        response = self.make_request("GET", url)
        print('Hello from the package------------')
        print(response)

        return self.get_response_list(response)
