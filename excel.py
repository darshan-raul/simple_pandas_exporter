import pandas as pd
df = pd.read_excel('sample_file.xlsx')
for id in df['id'].unique():
    df.loc[df['cust_id'] == cust_id].copy().to_excel(f'{cust_id}.xlsx')
