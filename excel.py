import pandas as pd
df = pd.read_excel('sample_file.xlsx')
for id in df['id'].unique():
    df.loc[df['id'] == id].copy().to_excel(f'{id}.xlsx')
