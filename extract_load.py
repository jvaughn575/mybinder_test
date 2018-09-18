import os
import pandas as pd 
import re

def get_file_names(path):
    file_names = os.listdir(path)    
    file_names = [filename for filename in file_names if filename.endswith(".csv")]
    return file_names    

def multiple_csv_to_dict_df(path):
    df_dict = dict()    
    file_names = get_file_names(path)
    for file_name in file_names:
        year = re.search(r"\d{4}",file_name)[0]
        df_dict[year] = pd.read_csv(path + "/" + file_name)
    return df_dict    
    

