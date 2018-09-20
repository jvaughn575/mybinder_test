import pandas as pd
import re

def _keyword_column_removal(df_dict,keyword_list):
    drop_columns = []

    for key,df in df_dict.items():
        for keyword in keyword_list:
            for column_name in df.columns:
                if re.search(keyword,column_name):
                    drop_columns.append(column_name)
                
    
        if len(drop_columns) > 0:
            df_dict[key] = df.drop(drop_columns,axis=1)
            drop_columns = []

    return df_dict

def combine_dataframes(dict_df):
    keywords = [r'^Maximum',r'^Minimum',r'^Standard']
    dict_df = _keyword_column_removal(dict_df,keywords)
    return pd.concat(dict_df.values()).reset_index()

