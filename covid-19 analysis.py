import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')
#loading corna csv file dataset and displaying top5 rows
c=pd.read_csv("Datasets\covid19_Confirmed_dataset.csv")
print(c.head())
print(c.shape)  #shape of the dataframe
#deleting usless columns
c.drop(["Lat","Long"],axis=1,inplace=True)  #drop col lat and long
print(c.head(10))
print(c.shape)
df=c.groupby("Country/Region").sum()
print(df.head(10))
print(df.shape)
#visualizing data related to a country ex: China,India,Italy
df.loc["China"].plot()  #plot the graph for the country
df.loc["India"].plot()
df.loc["Italy"].plot()
plt.legend()        #to diff. b/w curves
#calculating a Good measure
df.loc["China"].plot()
df.loc["China"][:3].plot()  #plotting for first 3 days data
plt.legend()
#calculating the first derivative of the curve
df.loc["China"].diff().plot()   #diff() is used to find 1st derivative
print(df.loc["China"].diff().max()) #prints max value of infection
print(df.loc["India"].diff().max())    #caculates max single day rise for India
print(df.loc["Spain"].diff().max())
# find max infection rate for all countries
countries=list(df.index)
max_infection_rate=[]
for i in countries:
    max_infection_rate.append(df.loc[i].diff().max())
print(max_infection_rate)
# or appending the max_infection_rate to our df
df["max_infection_rate"]=max_infection_rate
print(df.head(10))
#create a new data frame with only needed columns
newdf=pd.DataFrame(df["max_infection_rate"])
print(newdf.head())


#part2 Importing the happiness report csv data
report=pd.read_csv("Datasets/worldwide_happiness_report.csv")
print(report.head())
#drop useless columns
useless_cols=["Overall rank","Generosity","Perceptions of corruption"]
report.drop(useless_cols,axis=1,inplace=True)
print(report.head())
#changing the indices of the dataframe
report.set_index("Country or region",inplace=True)
print(report.head())
#combing corona data and happiness data
data=newdf.join(report,how="inner")
print(data.head())
#Correrlation Matrix
print(data.corr())
#Visualization of the results
print(data.head())
x=data["GDP per capita"]    #Conclusion people living in more developed countries are more prone to covid-19
y=data["max_infection_rate"]
sns.scatterplot(x, np.log(y))    #seaborn scatterplot b/w x and log(y) to bring down y value
sns.regplot(x, np.log(y))   #fit a curve in above plot
#plot b/w social support and max_infection rate
x=data["Social support"]
sns.scatterplot(x, np.log(y))
sns.regplot(x, np.log(y))
#plot b/w Healthy life expectancy and max_infection_rate
x=data["Healthy life expectancy"]
sns.scatterplot(x, np.log(y))
sns.regplot(x, np.log(y))
#plot b/v Freedom to make life choices and max_infection_rates
x=data["Freedom to make life choices"]
sns.scatterplot(x, np.log(y))
sns.regplot(x, np.log(y))
