import pandas as pd
import numpy as np

def split_columns(dataframe):
    new_df = dataframe
    lines_with_two_numbers_in_hate_speech = new_df[new_df['hate_speech'].str.contains(',')]
    new_df = new_df.drop(new_df[new_df['hate_speech'].str.contains(',')].index)
    lines_with_two_numbers_in_hate_speech[['col1', 'col2']] = lines_with_two_numbers_in_hate_speech['hate_speech'].str.split(',', expand=True)
    lines_with_two_numbers_in_hate_speech_with_col1 = lines_with_two_numbers_in_hate_speech[['instagram_comments', 'offensive_language', 'offensiveness_levels' ,'col1']]
    lines_with_two_numbers_in_hate_speech_with_col2 = lines_with_two_numbers_in_hate_speech[['instagram_comments', 'offensive_language', 'offensiveness_levels' ,'col2']]
    lines_with_two_numbers_in_hate_speech_with_col1 = lines_with_two_numbers_in_hate_speech_with_col1.rename(columns={'col1': 'hate_speech'})
    lines_with_two_numbers_in_hate_speech_with_col2 = lines_with_two_numbers_in_hate_speech_with_col2.rename(columns={'col2': 'hate_speech'})
    
    new_df = pd.concat([new_df, lines_with_two_numbers_in_hate_speech_with_col1, lines_with_two_numbers_in_hate_speech_with_col2])

    return new_df

def convert_to_binary(dataframe):
    df = split_columns(dataframe)
    df['hate_speech'] = np.where(df['hate_speech'].astype(int) <= 0, 0, 1)

    return df