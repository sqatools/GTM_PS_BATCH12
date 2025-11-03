import pytest
from ...page_objects.api.ready_use_api.ready_user_api_class import ReadyToUseAPI


class TestReadyUserAPI:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.r_api = ReadyToUseAPI()


    def test_get_all_entries_verify(self):
        res, st_code = self.r_api.get_all_get_entries()
        assert len(res) == 13
        assert st_code == 200


    def test_create_new_entry_verify(self):
        res, st_code, id = self.r_api.create_new_entry()
        assert len(res) == 4
        assert st_code == 200
        assert id is not None
