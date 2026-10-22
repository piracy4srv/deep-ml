import pandas as pd

def solution(df):
    for col in df.columns:
        if df[col].isnull().mean()>0.5:
            df.drop([col],axis=1,inplace=True)
    for row in df.index:
      if df.loc[row].isnull().mean()>0.5:
        df.drop([row],axis=0,inplace=True)
    df=df.fillna(df.mean(numeric_only=True))
    for col in df.select_dtypes(include='object').columns:
      df.fillna({col:df[col].mode()[0]},inplace=True)
    return df