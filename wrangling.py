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

# Question 4: missing values (get rid of blanks, for all to numeric
df3['ImposedSentenceAllChargeInContactEvent']=df3['ImposedSentenceAllChargeInContactEvent'].replace("",np.nan)
df3['ImposedSentenceAllChargeInContactEvent']=pd.to_numeric(df3['ImposedSentenceAllChargeInContactEvent'],errors='coerce') 
print(df3['ImposedSentenceAllChargeInContactEvent'].head(20))

