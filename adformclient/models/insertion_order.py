import json
import requests
import datetime

from adformclient.models.base import Base

class InsertionOrder(Base):

    object = "insertionOrders"

    def find_by_advertiser(self, id):
        pass
