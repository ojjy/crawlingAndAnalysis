import transfermarkt_crawler as trcr
import pandas as pd

# 파일로 Dataframe 부터 읽어오기
df_load = trcr.df

rows, cols = df_load.shape #unpacking
print(rows, cols)
print(df_load.info())