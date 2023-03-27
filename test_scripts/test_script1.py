from generic.base_setup import BaseSetup
from generic.excel import Excel


class TestScript1(BaseSetup):

    def test_script1(self):
        print('this is test script')
        print(self.driver.title)
        v = Excel.get_data(self.xl_path, "login", 2, 1)
        print(v)