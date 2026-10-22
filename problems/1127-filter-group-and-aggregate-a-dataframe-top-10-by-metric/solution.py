import pandas as pd

def solution(df):
    res=df[df['status']=='completed']
    res2=res.groupby('region')['amount'].sum()
    res2=res2.reset_index()
    return res2.head(10)
