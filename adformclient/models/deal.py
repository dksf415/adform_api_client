import json
import requests
import datetime

from adformclient.models.base import Base

class Deal(Base):

    object = "deals"
    scope = 'https://api.adform.com/scope/buyer.campaigns.api'

    def find_by_id(self, id):
        pass
