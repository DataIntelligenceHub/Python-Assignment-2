# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:39:16 2017

@author: Syed.Adeel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df= pd.read_csv("E://DIH//Assignment2//hospitaldata.csv")

#print(df.head())
#Q1
for i in df.columns:
    if ".." in i:
        df.rename(columns={i: i.replace('..','.')}, inplace=True)
        
print(df.head())

#Q2
date=df['Date']
days=date.map(lambda x: str(x).split(',')[0])
counts=days.value_counts()
print(counts)

#Q3
df['Age']=pd.to_numeric(df['Age'],errors='coerce' )
df['Age'].mean()

#Q4
children=df[df.Age<=12]
len(children.index)

#Q5
Male=df[df.Sex=='M']
print(Male['Procedure'].value_counts().index.tolist()[0])

Female=df[(df.Sex=='F')| (df.Sex=='f')]
print(Female['Procedure'].value_counts().index.tolist()[0])

#Q6
df['Total.Charges']=pd.to_numeric(df['Total.Charges'],errors='coerce')
grouped_dr = df[['Consulting.Doctor', 'Total.Charges']].groupby(['Consulting.Doctor']).sum()

#Q7
grouped_proced=df[['Procedure', 'Total.Charges']].groupby(['Procedure']).sum()

#Q8
Time=pd.to_datetime(df.Time, errors='coerce')
Time.dt.hour.value_counts()

#Q9
def time_bracket(hour):
    if  hour>= 6.0 and hour<12.0:
        return "Morning"
    elif hour>= 12 and hour<14:
        return "Afternoon"
    elif  hour>=14 and hour<19 :
        return "Evening"
    elif  hour>=19 and hour<=23 or hour >= 0 and hour < 6 :
        return "Night"
    else:
        return np.NAN
    
df['Time_brackets']=Time.dt.hour.apply(time_bracket)

#Q10
patient_visits=df['id'].value_counts()
print(len(patient_visits[patient_visits>1].index))

#Q11
print(patient_visits)

#Q12
x=df[['id','Procedure']]
patient_visits=x.groupby(['id','Procedure']).size()
print(patient_visits[patient_visits>1])
#Q13
Female.Age.median()
Male.Age.median()

#Q14
df.replace(to_replace=df['Amount.Balance'].unique()[0], value=np.nan, inplace=True)
df['Amount.Balance']=df['Amount.Balance'].map(lambda x: str(x).replace(',',''))
df['Amount.Balance'] = df['Amount.Balance'].astype(float)
print(df['Amount.Balance'].sum())

#Q15

Consultation=df[df.Procedure=='Consultation']
Consultation['Total.Charges'].sum()

#Q16
Corr=df.corr()
Corr.loc[['Age'],['Total.Charges']]

#Q17
#df['Age'].value_counts().plot(kind='bar')
df['Age'].plot.hist()
plt.show()

#Q18
df[(df.Procedure== 'X Rays') | (df.Procedure == 'Scalling')]['Total.Charges'].sum()

df.to_csv(path_or_buf="E://DIH//Assignment2//clean_hospital_data_python.csv")
