import json
import requests
import datetime

from adformclient.models.base import Base

class Campaign(Base):

    object = "campaigns"

    def find_by_id(self, id):
        pass
