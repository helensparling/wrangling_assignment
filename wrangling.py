#!/usr/bin/env python3

import numpy as np # Import the numpy package into your workspace
import matplotlib.pyplot as plt # Import matplotlib into your workspace
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# Question 1.1:
df = pd.read_csv("data/airbnb_hw.csv") 
df["Price"] = df["Price"].str.replace(",","")
#print(df['Price'])
# I removed the commas in the numerical values that were over 999 (for example, 1,000 needed to be cleaned to be 1000)

# Question 1.2: 
df2 = pd.read_csv("data/mn_police_use_of_force.csv")
df2['subject_injury']=df2['subject_injury'].replace('',np.nan)
#print(df2['subject_injury'])
# replaced missing values with np.nan instead of blanks
missing_values = (df2['subject_injury'].isna().sum())
total_values = len(df2)
proportion = missing_values/total_values
#print(proportion)
# https://stackoverflow.com/questions/26266362/how-do-i-count-the-nan-values-in-a-column-in-pandas-dataframe
#print(pd.crosstab( df2["subject_injury"], df2["force_type"]))

# The proportion of missing values to total values is ~0.76 which is concerning because about 3/4 of the data is missing. The use of baton, firearm, and less lethal projectile seem to be the most associated with missing data. 


# Question 1.3: Dummy variable
url = 'http://www.vcsc.virginia.gov/pretrialdataproject/October%202017%20Cohort_Virginia%20Pretrial%20Data%20Project_Deidentified%20FINAL%20Update_10272021.csv'
df3 = pd.read_csv(url,low_memory=False)
#print(df3["WhetherDefendantWasReleasedPretrial"].unique())
df3['WhetherDefendantWasReleasedPretrial']=df3['WhetherDefendantWasReleasedPretrial'].replace('9',np.nan)
#print(df3['WhetherDefendantWasReleasedPretrial'])
# I first looked at what unique values were in the WhetherDefendantWasReleasedPretrial column. They were all either 0, 1, or 9. I replaced the 9 with np.nan as it is not a 0 or 1 value for the dummy variables. 

# Question 1.4: missing values 
df3['ImposedSentenceAllChargeInContactEvent']=df3['ImposedSentenceAllChargeInContactEvent'].replace("",np.nan)
df3['ImposedSentenceAllChargeInContactEvent']=pd.to_numeric(df3['ImposedSentenceAllChargeInContactEvent'],errors='coerce') 
#print(df3['ImposedSentenceAllChargeInContactEvent'].head(20))

# Question 2.1
df4 = pd.read_excel("GSAF5.xls")
# https://stackoverflow.com/questions/3239207/how-can-i-open-an-excel-file-in-python

# Question 2.2
#https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe
df4=df4.drop(columns=["pdf","href formula","href", "Case Number", "Case Number.1", "original order", "Unnamed: 21", "Unnamed: 22"])

# Question 2.3
# https://saturncloud.io/blog/python-pandas-how-to-remove-nan-and-inf-values/
df4 = df4.dropna()
df4["Year"]=df4["Year"].astype(int)
#print(df4["Year"].unique())
#print(df4.dtypes)
# The values for the "Year" variable range from 0-2025. 
recent_attacks = df4[df4["Year"]>1939]
#print(recent_attacks["Year"].value_counts())
# Response: the values for the "Year" variable range from 0-2025. After filtering rows to focus on attacks since 1940, attacks appear to be increasing over time, though this could be due to data availability rather than a true increase. 

# Question 2.4
#print(df4["Age"].unique())
df4["Age"] = df4["Age"].astype(str)
df4["Age"]=df4["Age"].str.strip()
df4["Age"]=df4["Age"].str.replace("s","",regex=False)
df4["Age"]=df4["Age"].str.replace("'","",regex=False)
df4["Age"]=df4["Age"].str.replace("'s","",regex=False)
df4["Age"]=df4["Age"].str.replace("+","",regex=False)
df4["Age"]=df4["Age"].str.replace("6½","6.5",regex=False)
df4["Age"]=df4["Age"].str.replace("?","",regex=False)
df4["Age"]=df4["Age"].replace(["\xa0", "?","Teen"," ","Middle age",""],np.nan)
df4["Age"]=df4["Age"].str.replace(">","",regex=False)
df4["Age"]=df4["Age"].str.replace("45 and 15","45",regex=False)
df4["Age"]=df4["Age"].str.replace("28 & 22","28",regex=False)
df4["Age"]=df4["Age"].str.replace("9 & 60","9",regex=False)
df4["Age"]=df4["Age"].str.replace("30 or 36","30",regex=False)
df4["Age"]=df4["Age"].str.replace("18 or 20","18",regex=False)
df4["Age"]=df4["Age"].str.replace("30 & 32","30",regex=False)
df4["Age"]=df4["Age"].str.replace("13 or 18","13",regex=False)
df4["Age"]=df4["Age"].str.replace("7 or 8","7",regex=False)
df4["Age"]=df4["Age"].str.replace("9 or 10","9",regex=False)
df4["Age"]=df4["Age"].str.replace("13 or 14","13",regex=False)
#https://www.geeksforgeeks.org/python/python-string-strip/
#https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html
df4["Age"]=df4["Age"].astype(float)
#print(df4["Age"].unique())
df4["Age"].hist()

# Question 5:_
#print(df4["Sex"].value_counts())
#print(1439/(226+1439))
# There are far more male victims than female victims, with the proportion of male victims = 0.86

# Question 6:
#print(df4["Type"].unique())
df4["Type"]=df4["Type"].str.replace("un","Un",regex=False)
df4["Type"]=df4["Type"].replace(["Questionable","Watercraft","Invalid","Sea Disaster"],"Unknown")
#print(df4["Type"].unique())
#print(df4["Type"].value_counts())
#print(1528/(125+44+1528))
#https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html?utm_source=chatgpt.com
#The proportion of attacks that are unprovoked is 0.9

# Question 7:
#print(df4["Fatal Y/N"].unique())
df4["Fatal Y/N"]=df4["Fatal Y/N"].astype(str)
df4["Fatal Y/N"]=df4["Fatal Y/N"].replace(["F","M","2017"],"Unknown")
df4["Fatal Y/N"]=df4["Fatal Y/N"].str.replace(" N","N",regex=False)
#print(df4["Fatal Y/N"].unique())

# Question 8:
#print(pd.crosstab(df4["Sex"],df4["Type"]))
#print(pd.crosstab(df4["Type"],df4["Fatal Y/N"]))
#print(pd.crosstab(df4["Fatal Y/N"],df4["Sex"]))
# Sharks are more likely to launch unprovoked attacks on men.
# When the attack is provoked, it is more likely to to not be fatal than fatal. When the attack is unprovoked, the attack is also more likely to not be fatal. 
# For females, the proportion of fatal attacks is 0.16, while for men it is slightly higher at 0.17.
# I am not particularly worried about sharks, attacks appear to be more common in men, and deeper analysis into location of attack would be requried for me to be more concerned.

# Question 9:
df4["Species "]=df4["Species "].astype(str)
df4["Species "]=df4["Species "].str.replace("Great White","GWS")
df4["Species "]=df4["Species "].str.replace("great white","GWS")

shark_list = (df4["Species "].str.split( ))
print(shark_list.head(10))
x = "White"
count = sum([x in sub_shark_list for sub_shark_list in shark_list])
proportion = count/len(shark_list)
#print(proportion)
#https://www.geeksforgeeks.org/python/python-count-the-sublists-containing-given-element-in-a-list/
# https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
# The proportion of attacks that appear to be qhite sharks is 0.17.
