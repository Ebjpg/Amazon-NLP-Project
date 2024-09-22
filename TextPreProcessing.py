import pandas as pd

df = pd.read_excel('amazon.xlsx')
print(df['Review'].str.lower())



