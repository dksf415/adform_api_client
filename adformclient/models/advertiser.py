import json
import requests
import datetime

from adformclient.models.base import Base

class Advertiser(Base):

    object = "advertisers"

    def find_by_name(self):
        pass
