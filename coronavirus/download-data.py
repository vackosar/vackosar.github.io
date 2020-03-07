import pandas as pd
import requests
import io

r = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
s = r.content.decode()
with io.StringIO(s) as f:
    df = pd.read_csv(f)


eu = pd.read_csv('european-countries.csv')
df['country'] = df['Country/Region'].str.lower()
eu = eu['country'].str.lower()


print(df.query("country == 'czech republic'"))
