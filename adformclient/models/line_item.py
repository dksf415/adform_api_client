import json
import requests
import datetime

from adformclient.models.base import Base

class LineItem(Base):

    object = "lineItems"

    def find_by_insertion_order(self, id):
        pass
