import pandas as pd
import requests
import io

r = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
s = r.content.decode()
with io.StringIO(s) as f:
    df = pd.read_csv(f)


eu = pd.read_csv('european-countries.csv')

df['latest'] = df['3/11/20'].copy()
nan_idx = pd.isnull(df['3/11/20'])
# this does not give correct sum
df.loc[nan_idx, 'latest'] = df.loc[nan_idx, '3/10/20']
tot = df['latest'].dropna().sum()
df['country'] = df['Country/Region'].str.lower()
eu = eu['country'].str.lower()


print(df.query("country == 'czech republic'"))


df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-11-2020.csv')
tot = df['Confirmed'].sum()
print(tot)

