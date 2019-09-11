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

    def make_request(self, method, url, payload=None):
        """

        :param method: String
        :param url:
        :param payload:
        :return: Response object
        """
        headers = self.api_headers()

        if method == "GET":
            self.curl = "curl -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' '{1}'".format(
                headers,
                url
            )
            response = requests.get(
                url,
                headers=headers,
                data=payload,
                verify=False
            )

        elif method == "POST":
            self.curl = "curl -XPOST -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' -d '{1}' '{2}'".format(
                headers,
                payload,
                url
            )
            response = requests.post(
                url,
                headers=headers,
                data=payload,
                verify=False
            )

        elif method == "PUT":
            self.curl = "curl -XPUT -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' -d '{1}' '{2}'".format(
                headers,
                payload,
                url
            )
            response = requests.post(
                url,
                headers=headers,
                data=payload,
                verify=False
            )

        return response

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
