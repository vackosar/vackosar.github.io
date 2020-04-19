#!/bin/bash

wget -O time_series_covid19_confirmed_global.csv https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
wget -O time_series_covid19_deaths_global.csv https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
sed -e "s/2020-04-09/$(date +%F)/g" templates/index.html > index.html;
sed -e "s/2020-04-09/$(date +%F)/g" templates/sitemap.xml > sitemap.xml;