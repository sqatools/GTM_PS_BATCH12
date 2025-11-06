from ....base.api_base import APIBase
from .ready_use_api_data import *


class ReadyToUseAPI(APIBase):
    def __init__(self):
        super().__init__()


    def get_all_get_entries(self):
       res, st_code = self.get_method(url=com_url)
       return res, st_code

    def create_new_entry(self):
        res, st_code = self.post_method(url=com_url, headers=headers, payload=new_entry_payload)
        id = res['id']
        return res, st_code, id
