import logging
import json
import requests
import datetime

class Base:

    url_metadata = "https://api.adform.com/v1/buyer"
    object = None

    def __init__(self, connection=None):
        self.connection = connection

    def api_headers(self):
        """
        :return:
        """
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        return headers

    def get_by_id(self, id):
        """
        :param id:
        :return: JSON object
        """
        url = "{0}/{1}/{2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_object(response)
