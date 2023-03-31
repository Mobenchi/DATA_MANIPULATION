import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr

#Reading the data

file_path = "D:/DEV/DATA/covid_worldwide.csv"
data = pd.read_csv(file_path)

#Percentege of missing val per col

missing_val_per = data.isna().sum().sort_values(ascending=False) / len(data)
missing_val_per[missing_val_per!=0].plot(kind="barh")

#Dropping colomn that i don't need for analyses
 
data = data.drop(columns=['Active Cases'])
data = data.dropna(how='any',axis=0)

#Getting all the values of one column

all_Countrys = data["Country"].to_numpy()

#Check if morocco is among country column

check1 = 'Morocco' in data['Country'].unique()

#Remove commas from the 'Total Cases' column

data['Total Cases'] = data['Total Cases'].str.replace(',', '')
data['Total Recovered'] = data['Total Recovered'].str.replace(',', '')
data['Population'] = data['Population'].str.replace(',', '')
data['Total Test'] = data['Total Test'].str.replace(',', '')
data['Total Deaths'] = data['Total Deaths'].str.replace(',', '')

# Create a list of tuples containing the city name and the recovery ratio for each row

reco_ratios = []

#Convert the values to numeric data type

data['Total Cases'] = pd.to_numeric(data['Total Cases'])
data['Total Recovered'] = pd.to_numeric(data['Total Recovered'])
data['Population'] = pd.to_numeric(data['Population'])
data['Total Test'] = pd.to_numeric(data['Total Test'])
data['Total Deaths'] = pd.to_numeric(data['Total Deaths'])

#ratio of recovery
# Loop through each row in the DataFrame and calculate the recovery ratio for that row

for index, row in data.iterrows():
    Country = row['Country']
    value1 = row['Total Cases']
    value2 = row['Total Recovered']
    if value1 == 0:
        reco_ratio = 0
    else:
        reco_ratio = value2 / value1
    reco_ratios.append((Country, reco_ratio)) #all the ratio values that we collected are stored, each one with her index 

#Ploting and Sorting the result for better analysing
        
reco_ratios.sort(key=lambda x: x[1], reverse=True)
countries = [x[0] for x in reco_ratios]
ratios = [x[1] for x in reco_ratios]
ratios = pd.to_numeric(ratios)
plt.figure(figsize=(14, 6))
plt.bar(countries, ratios)
plt.xticks(rotation=90, fontsize=10) 
plt.yticks(fontsize=10) 
plt.xlabel('City', fontsize=12) 
plt.ylabel('Recovery Ratio', fontsize=12) 
plt.title('Recovery Ratio by City', fontsize=14) 

#Interpreting Pearson’s correlation coefficient for all columns in data

plt.figure(figsize=(14,8))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='Blues')