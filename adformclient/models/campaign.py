import json
import requests
import datetime

from adformclient.models.base import Base

class Campaign(Base):

    object = "campaigns"

    def find_by_id(self, id):
        """
        :param id:
        :return: JSON array
        """
        url = "{0}/{1}/{2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_list(response)

    def get_response_list(self, response):
        """
        :param response:
        :return: JSON object
        """
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        rval["request_body"] = self.curl
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data.get('data')
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('errors')
            rval["data"] = data

        return json.dumps(rval)