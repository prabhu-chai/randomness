# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K8hycCFNd074xrNNxsACWM9dfFJYPiZJ
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install pycountry_convert
import pandas as pd
import datascience as ds
import pycountry_convert as pc
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from datascience.predicates import are
z=pd.read_excel("/indicator hiv estimated prevalence% 15-49.xlsx")

r=z.rename(columns={2000: "2000",2001: "2001",2002: "2002",2003: "2003",2004: "2004",2005: "2005",2006: "2006",2007: "2007",2008:"2008",2009: "2009",1979: "1979",1980: "1980",1981:"1981",1982:"1982",1983:"1983",1984:"1984",1985:"1985",1986:"1986",1987:"1987",1988:"1988",1989:"1989",1990:"1990",1991:"1991",1992:"1992",1993:"1993",1994:"1994",1995:"1995",1996:"1996",1997:"1997",1998:"1998",1999:"1999"})

y=pd.DataFrame(r)
continent=[]
continent_dict = {"AS":"Asia", "EU": "Europe", "AF": "Africa", "OC": "Australia", "NA": "North America", "SA": "South America"}

for i in y['Estimated HIV Prevalence% - (Ages 15-49)']:
  try:
    country_code = pc.country_name_to_country_alpha2(i, cn_name_format="default")
    continent_name = pc.country_alpha2_to_continent_code(country_code)
    continent.append(continent_dict[continent_name])
  except KeyError:
    try:
      z=i.split(",")
      country_code = pc.country_name_to_country_alpha2(z[0], cn_name_format="default")
      continent_name = pc.country_alpha2_to_continent_code(country_code)
      continent.append(continent_dict[continent_name])
    except KeyError:
      print(z[0]+"not found")
      continent.append("not found")

y['continent']=continent

y.to_csv('/with_continents.csv')
y

p=y[['Estimated HIV Prevalence% - (Ages 15-49)','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','continent']]

data_table = ds.Table.from_df(p)

p=p.fillna(0)
p['average']=(p['2000']+p['2001']+p['2002']+p['2003']+p['2004']+p['2005']+p['2006']+p['2007']+p['2008']+p['2009']+p['2010']+p['2011'])/12
p.sort_values(by=['average'],inplace=True,ascending=False)

table = ds.Table.from_df(p)
t = ds.Table.from_df(p)
table.group("continent",max)

table.group("continent",max).barh('continent','average max')

table.group("continent",min).barh('continent','average min')

table1=table.group("continent",max)
table2=table.group("continent",min)

table2["average max"]=table1["average max"]
table1["average min"]=table2["average min"]
table2.select('continent','average max','average min').barh('continent')

dftemp=table1.to_df()
dftemp1=dftemp.sample(frac=0.70)
plt.plot(dftemp1['Estimated HIV Prevalence% - (Ages 15-49) max'])
plt.plot(dftemp1['average min'])
plt.plot(dftemp1['average max'])



t.sort("Estimated HIV Prevalence% - (Ages 15-49)")

table3=table.group("Estimated HIV Prevalence% - (Ages 15-49)",min)
table4=table.group("Estimated HIV Prevalence% - (Ages 15-49)",max)
table3

y=y.fillna(0)
full_table=ds.Table.from_df(y)
full_table

grouped_by_countries=full_table.group("continent",sum)

x=grouped_by_countries.to_df()
temp1=x.transpose()
new_header = temp1.iloc[0] #grab the first row for the header
temp1 = temp1[1:] #take the data less the header row
temp1.columns = new_header #set the header row as the df header
temp2=temp1.drop('Estimated HIV Prevalence% - (Ages 15-49) sum')
temp2['Africa']=temp2['Africa']/count[0]
temp2['Asia']=temp2['Asia']/count[1]
temp2['Australia']=temp2['Australia']/count[2]
temp2['Europe']=temp2['Europe']/count[3]
temp2['North America']=temp2['North America']/count[4]
temp2['South America']=temp2['South America']/count[5]
temp2['not found']=temp2['not found']/count[6]
temp2=temp2.drop('number of countries')
temp2.plot.line()
temp2

temp2['Africa'].plot.line()
plt.figure()
temp2['Asia'].plot.line()
plt.figure()
temp2['Australia'].plot.line()
plt.figure()
temp2['Europe'].plot.line()
plt.figure()
temp2['North America'].plot.line()
plt.figure()
temp2['South America'].plot.line()
plt.figure()
temp2['not found'].plot.line()

africa_average=y[y.continent=='Africa'].mean(axis=0,skipna=0)
africa=y[y.continent=='Africa']
africa['x']="1.647636"
africa['y']="4.28"
asia_average=y[y.continent=='Asia'].mean(axis=0,skipna=0)
asia=y[y.continent=='Asia']
asia['x']="0.072"
asia['y']="0.136"
europe_average=y[y.continent=='Europe'].mean(axis=0,skipna=0)
europe=y[y.continent=='Europe']
europe['x']="0.07208"
europe['y']="0.2079"
Australia=y[y.continent=='Australia']
Australia_average=y[y.continent=='Australia'].mean(axis=0,skipna=0)
Australia['x']="0.0145"
Australia['y']="0.0481"
North_America=y[y.continent=='North America']
North_America_average=y[y.continent=='North America'].mean(axis=0,skipna=0)
North_America['x']="0.2852"
North_America['y']="0.418"
South_America=y[y.continent=='South America']
South_America_average=y[y.continent=='South America'].mean(axis=0,skipna=0)
South_America['x']="0.3746"
South_America['y']="0.492"
Not_found=y[y.continent=='not found']
Not_found_average=y[y.continent=='not found'].mean(axis=0,skipna=0)
Not_found['x']="0.0502"
Not_found['y']="0.0714"

plt.scatter(africa['x'],africa['1990'])
plt.scatter(asia['x'],asia['1990'])
plt.scatter(North_America['x'],North_America['1990'])
plt.scatter(Australia['x'],Australia['1990'])
plt.scatter(South_America['x'],South_America['1990'])
plt.scatter(europe['x'],europe['1990'])
plt.scatter(Not_found['x'],Not_found['1990'])

plt.scatter(africa['y'],africa['2010'])
plt.scatter(asia['y'],asia['2010'])
plt.scatter(North_America['y'],North_America['2010'])
plt.scatter(Australia['y'],Australia['2010'])
plt.scatter(South_America['y'],South_America['2010'])
plt.scatter(europe['y'],europe['2010'])
plt.scatter(Not_found['y'],Not_found['2010'])