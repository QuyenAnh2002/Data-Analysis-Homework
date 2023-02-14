import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/quyen/Downloads/10_OneNumSevCatSubgroupsSevObs.csv")

df.head(10)
df.describe()
total_bill = df['total_bill']
tip = df['tip']
sex = df['sex']
smoker = df['smoker']

# Calculate	total	bill,	total	tips,	statistic	value	of	them

print("total:", total_bill.sum())
print("tip:", tip.sum())


#Number	of	man/women	book	the	table?	


sex_value = sex.value_counts()
sex_value
print(sex_value['Male'] / sex_value['Female'])

#Probability	that	a	women	will	book	a	table?	

total_sex = sex_value['Male'] + sex_value['Female']

sex_value_tb = (sex_value['Female'] / total_sex) * 100
print(sex_value_tb )


#Number	of	smoker/	non-smoker	
 
smoker_value = smoker.value_counts()
smoker_value
print(smoker_value['Yes'] / smoker_value['No'])

#Probability	that	a	smoker	will	book	a	table?
total_smoker = smoker_value['Yes'] + smoker_value['No']
total_smoker

smoker_value_tb = (smoker_value['Yes'] / total_smoker) * 100
print(smoker_value_tb)


#Probability	that	a	smoker	is	a	women	will	book	a	table?

F_smoker = df[df["sex"] == 'Female'][df["smoker"] == 'Yes']
F_smoker

print((len(F_smoker)/total_sex) * 100)


#•Classify	by	time
group_by_time = df.groupby(["time"]).value_counts()
group_by_time

#Classify	by	size
group_by_size = df.groupby(["size"]).value_counts()
group_by_size













