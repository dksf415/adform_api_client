import logging
import json
import requests
import datetime

class Base:

    url_metadata = "https://api.adform.com/v1/buyer"
    object = None
    access_token = None
    connection = None

    def __init__(self, connection=None):
        self.connection = connection

    def api_headers(self, scope):
        """
        :return:
        """
        self.access_token = self.connection.get_access_token(scope)

        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Return-Total-Count'] = 'true'
        headers['Authorization'] = 'Bearer {0}'.format(self.access_token)

        return headers

    def make_request(self, method, url, scope, payload=None):
        """

        :param method: String
        :param url:
        :param payload:
        :return: Response object
        """
        headers = self.api_headers(scope)

        if method == "GET":
            self.curl = "curl -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' '{1}'".format(
                headers,
                url
            )
            response = requests.get(
                url,
                headers=headers,
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

    def get_by_id(self, id):
        """
        :param id:
        :return: JSON object
        """
        url = "{0}/{1}/{2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url, self.scope)

        return self.get_response_object(response)

    def get_response_list(self, response_text, response_status_code):
        """
        :param response:
        :return: JSON object
        """
        data = json.loads(response_text)
        rval = {}
        rval["response_code"] = response_status_code
        rval["request_body"] = self.curl
        if response_status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('errors')
            rval["data"] = data

        return json.dumps(rval)

    def get_response_object(self, response):
        """
        :param response:
        :return: JSON object
        """
        data = json.loads(response.text)
        print("client data: {}".format(data))
        rval = {}
        rval["response_code"] = response.status_code
        rval["request_body"] = self.curl
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('errors')
            rval["data"] = data

        return json.dumps(rval)
