import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
os.chdir("D:/2023Grade1/IBI1")
os.getcwd()

os.listdir()
covid_data=pd.read_csv("full_data.csv")
print(covid_data.head(5))
print(covid_data.info)
print(covid_data.describe())
# new case mean:1.117552e+04  SD:1.052843e+05
# total cases:1.000000e+00-7.610711e+08
print(covid_data.iloc[0:100:2,0:5])
# iloc[x:y:z],means show the column from every 2 rows in the first 100 rows.
print(covid_data.iloc[1:1001:100])
my_columns=[True,False,True,False,True,False,True,False,True,False]
print(covid_data.iloc[0:3,my_columns])
# If my_columns is shorter or longer, it will report Indexerror.
print(covid_data.loc[2:4,"date"])

print(covid_data.loc[covid_data["location"]=="Afghanistan",'total_cases'])

new_data=covid_data.loc[covid_data["date"]=="2020-03-31",["location","new_cases","new_deaths"]]
print(new_data.describe())
print(np.mean(new_data["new_cases"]))
# The mean of new_cases is 1142.938525, new_deaths is 83.764228. the proportion is 0.07.
plt.boxplot(x=new_data["new_deaths"])
plt.show()
plt.boxplot(x=new_data["new_cases"])
plt.show()
# New_cases has no plot!
world_data=covid_data.loc[covid_data["location"]=="World","new_cases"]
world_data1=covid_data.loc[covid_data["location"]=="World","new_deaths"]
world_dates=covid_data.loc[covid_data["location"]=="World","date"]
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(world_dates,world_data,'r--',label="new cases")
ax2.plot(world_dates,world_data,'b--',label="new deaths")
# r/b means color,+/o means the shape
plt.show()
