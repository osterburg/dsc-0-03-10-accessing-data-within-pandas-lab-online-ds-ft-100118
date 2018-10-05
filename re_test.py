import re
import pandas as pd

df = pd.read_csv('/Users/stephanosterburg/git/learn_co/section_03/dsc-0-03-10-accessing-data-within-pandas-lab-online-ds-ft-100118/WorldCupMatches.csv')
df.replace(to_replace=r'Korea.*$', value=r'Korea', regex=True, inplace=True)
print(df.head())

print(df.loc[df["Home Team Name"].str.contains('Korea')])
