import json
import time

from adformclient.models.base import Base

class Creative(Base):

    def find_by_id(self, id):
        """

        :param id:
        :return: JSON array
        """
        print("POSSIBLE CREATIVE ID FROM CLIENT: {}".format(id))
        return
#        scope = 'https://api.adform.com/scope/buyer.rtb.lineitem'
#        url = "{}/rtb/lineitems?campaignIds={}".format(self.url_metadata, id)
#        response = self.make_request("GET", url, scope)
#
#        return self.get_response_list(response.text, response.status_code)
#
#        pass

    def find_by_line_item(self, id)
        """

        :param id:
        :return: JSON array
        """
        scope = 'https://api.adform.com/scope/buyer.rtb.lineitem'
        url = "{}/rtb/lineitems/{}".format(self.url_metadata, id)
        response = self.make_request("GET", url, scope)
        line_item_data = json.loads(response.text)
        print(line_item_data)
#        return self.get_response_list(response.text, response.status_code)
