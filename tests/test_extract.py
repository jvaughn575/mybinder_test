import unittest
from extract_load import multiple_csv_to_dict_df
from extract_load import get_file_names

class TestExtractLoad(unittest.TestCase):
    def setUp(self):
        self.path = "./data"              

    def test_get_file_names(self):        
        file_names = get_file_names(self.path)
        for file_name in file_names:
            self.assertEquals(True, file_name.endswith(".csv"))

    def test_multiple_csv_to_dict_df(self):
        df_dict = multiple_csv_to_dict_df(self.path)
        self.assertIsInstance(df_dict, dict)
        
            