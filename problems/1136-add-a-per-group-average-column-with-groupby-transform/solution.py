import pandas as pd

def solution(df):
  df_group=df.groupby('group')['value'].mean()
  df['group_avg']=df['group'].map(df_group)
  return df