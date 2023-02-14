import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/quyen/Downloads/10_OneNumSevCatSubgroupsSevObs.csv")

df.head(10)

total_bill = df['total_bill']
tip = df['tip']
sex = df['sex']

print(total_bill.sum())
print(tip.sum())

df.describe()

sex_value = sex.value_counts()
print(sex_value['Male'] / sex_value['Female'])

total_sex = sex_value['Male'] + sex_value['Female']

sex_value_tb = (sex_value['Female'] / total_sex) * 100
print(sex_value_tb )

