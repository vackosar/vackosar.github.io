import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/vackosar/downloads/capacity.csv')
print()
region_col = df.columns.values[0]

col_i = 13
precent_col_i = col_i + 2
total_col = df.columns.values[col_i]
available_1_col = df.columns.values[col_i + 1]
available_2_col = df.columns.values[col_i + 2]
# percent_col = df.columns.values[col_i]

title = df.iloc[2, col_i]
fig = plt.figure(figsize=(15, 8), dpi=200)
for region in ('PHA', 'LBK'):
    pha_df = df.loc[df[region_col] == region, [total_col, available_1_col, available_2_col]]
    pha_df['percent'] = ((pd.to_numeric(pha_df[available_1_col]) + pd.to_numeric(pha_df[available_2_col])) / pd.to_numeric(pha_df[total_col])) * 100
    dates = [(pd.Timestamp('2020-10-27') - pd.Timedelta(days=i)).date().isoformat() for i in range(len(pha_df))]
    pha_df['date'] = dates
    pha_df = pha_df.iloc[::-1]
    # pha_df = pha_df.reindex(index=pha_df.index[::-1])
    # print(pha_df)
    pha_df.to_csv('pha_capacity.csv')

    # pha_df[['date', 'percent']].plot()
    plt.plot(pha_df['date'].values, pha_df['percent'].values, label=region)
    plt.tight_layout()
    plt.xticks(pha_df['date'].values, rotation='vertical')

fig.autofmt_xdate()
plt.ylabel('Kapacita [%]')
plt.legend()
plt.title(title)
plt.show()

"""
Data "Kapacity lůžkové péče" jsou na https://onemocneni-aktualne.mzcr.cz/covid-19 Celorepublikove nevidim katastrofu. V regionech se to v nekterych okamzicich zdalo byt horsi, ale porad tam vidim nejaky buffer. Da se pripadne vyuzit kapacit s sousednich regionech?

"""