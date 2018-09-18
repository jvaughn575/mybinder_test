import unittest
from extract_load import multiple_csv_to_dict_df
from preprocessing import keyword_column_removal

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.path = "./data"
        self.df_dict = multiple_csv_to_dict_df(self.path)
        self.keyword_list = ["Minimum","Maximum","Standard"]
    
    def test_keyword_column_removal(self):
        dropped_df_dict = keyword_column_removal(self.df_dict, self.keyword_list)

        df_compare_cols = None
        for _,df in dropped_df_dict.items():
            if df_compare_cols is None:
                df_compare_cols = df.columns            
            
            try:
                self.assertTrue((df_compare_cols == df.columns).all())
            except:
                self.assertTrue(False,"Dataframes must contain same number of columns for comparison!")     


        
    