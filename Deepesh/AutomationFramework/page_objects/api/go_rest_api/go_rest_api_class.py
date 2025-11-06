from ....base.api_base import APIBase
from .go_rest_api_data import *


class GoRestAPI(APIBase):
    def __init__(self):
        super().__init__()

    def add_new_resource(self):
        res, st_code = self.post_method(url=users_api_url, headers=user_headers, payload=user_payload)
        return res, st_code



