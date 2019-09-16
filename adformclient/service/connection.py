import requests
import json

class Connection(object):

    access_token = None
    response = None
    url_token = "https://id.adform.com/sts/connect/token"

    def __init__(self, client_id=None, client_secret=None, grant_type="client_credentials"):

        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
            
    def get_access_token(self, scope):

        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': self.grant_type,
            'scope': self.scope
        }

        response = requests.post(self.url_token, data=data)

        if response is not None:
            obj = json.loads(response.text)
            if 'access_token' in obj:
                return obj['access_token']
