import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dask.dataframe as dd

# add -> commit -> push

df = dd.read_csv('chess_games_large.csv')

# print(df.info())
df_1 = df.groupby('Event').WhiteRatingDiff.mean().compute()
print(df_1)
df_2 = df.groupby('Event').BlackRatingDiff.mean().compute()
print(df_2)
