import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
# show all columns
os.chdir("D:/2023Grade1/IBI1")
os.getcwd()

os.listdir()
covid_data=pd.read_csv("full_data.csv")
print(covid_data.head(5))
# Show the first 5 rows
print(covid_data.info)
print(covid_data.describe())
# new case mean:1.117552e+04  SD:1.052843e+05
# total cases:1.000000e+00-7.610711e+08
print(covid_data.iloc[0:100:2,0:5])
# iloc[x:y:z],means show the column from every 2 rows in the first 100 rows.
print(covid_data.iloc[1:1001:100])
my_columns=[True,False,True,False,True,False]
print(covid_data.iloc[0:3,my_columns])
# If my_columns is shorter or longer, it will report Indexerror.
print(covid_data.loc[2:4,"date"])

my_rows = covid_data["location"] == "Afghanistan"
print(my_rows)
# my_rows is
# 0        True
# 1        True
# 2        True
# 3        True
# 4        True
#         ...
# 7991    False
# 7992    False
# 7993    False
# 7994    False
# 7995    False
print(covid_data.loc[my_rows, "total_cases"])

new_data=covid_data.loc[covid_data["date"]=="2020-03-31",["location","new_cases","new_deaths"]]
print(new_data.describe())
print(np.mean(new_data["new_cases"]))
print(np.mean(new_data["new_deaths"]))
# The mean of new_cases is 1142.938525, new_deaths is 83.764228. the proportion is 0.07.
plt.boxplot(x=new_data["new_deaths"])
plt.title("new deaths on 2020-03-31")
plt.show()
plt.boxplot(x=new_data["new_cases"])
plt.title("new cases on 2020-03-31")
plt.show()

world_data = covid_data.loc[covid_data["location"] == "World", "new_cases"]
world_data1 = covid_data.loc[covid_data["location"] == "World", "new_deaths"]
world_dates = covid_data.loc[covid_data["location"] == "World", "date"]

fig, ax1 = plt.subplots(figsize=(30,5))
# subplots means I can manage different map layers through "axes". figsize controls the length and width.
ax2 = ax1.twinx()
# twinx() means two y axes.
ax1.plot(world_dates, world_data, 'b--', label='new cases')
ax2.plot(world_dates, world_data1, 'r--', label='new deaths')

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles=handles1 + handles2, labels=labels1 + labels2)
# legends
plt.xticks(world_dates.iloc[0:len(world_dates):4])
# show x ticks every 4 days.
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90,fontsize=6)
# rotate the ticks
ax1.set_ylabel('Number of new cases')
ax2.set_ylabel('Number of deaths')
plt.title("worldwide COVID-19 new deaths and new cases overtime")
plt.show()

china_data=covid_data.loc[covid_data['location']=='China',['total_cases','total_deaths']]

china_rate=china_data.apply(lambda china_data:china_data['total_deaths']/china_data['total_cases'],axis=1)
# let the value of total death / total cases in each row.
print(china_rate)
fig,ax=plt.subplots()
ax.plot(world_dates,china_rate,"bo")
plt.xticks(world_dates.iloc[0:len(world_dates):4])
plt.title("China COVID-19 death rate overtime")
ax.set_xticklabels(ax.get_xticklabels(),rotation=90,fontsize=6)
plt.show()
# Opposite to my hypothesis, there is no obvious change on COVID-19 death rate in China.
