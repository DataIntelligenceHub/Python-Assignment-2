# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:39:16 2017

@author: Syed.Adeel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df= pd.read_csv("E:\DIH\R Assignment\Assignment - 22-03-2017\hospitaldata.csv")
#columns name rename replacing .. to . and also . to '' 
#print(df.head())
#Q1


for i in df.columns:
    if ".." in i:
        df.rename(columns={i: i.replace('..','')}, inplace=True)

for i in df.columns:
    if "." in i:
        df.rename(columns={i: i.replace('.','')}, inplace=True)
#Q2

date=df['Date']
days=date.map(lambda x: str(x).split(',')[0])
counts=days.value_counts().index.tolist()
print(counts[0])

#Q3
df['Age']=pd.to_numeric(df['Age'],errors='coerce' )
df['Age'].mean()

#Q4
childrentot=df[df.Age<=12]
len(childrentot.index)

#Q5

Male=df[df.Sex=='M']
print(Male['Procedure'].value_counts().index.tolist()[0])
Female=df[(df.Sex=='F')| (df.Sex=='f')]
print(Female['Procedure'].value_counts().index.tolist()[0])

#Q6
df['AmountReceived']=pd.to_numeric(df['AmountReceived'],errors='coerce')
grouped_dr = df.groupby(['ConsultingDoctor'])['AmountReceived'].sum()
print(str(grouped_dr.max())+" " +str(grouped_dr.idxmax()))

#Q7
df['AmountReceived']= pd.to_numeric(df['AmountReceived'],errors ='coerce')
highest_proc = df.groupby(['Procedure'])['AmountReceived'].sum()
print(str(highest_proc.max())+" " +str(highest_proc.idxmax()))

#Q8
df.Time=pd.to_datetime(df.Time, errors='coerce')
highest_freq_time = df.Time.dt.hour.value_counts()
print(highest_freq_time.idxmax())

#Q9
def timeslot(hours):
    if  hours >= 6 and hours < 12:
        return "Morning"
    elif hours >= 12 and hours < 14:
        return "Afternoon"
    elif  hours >= 14 and hours < 19:
        return "Evening"
    elif  hours >= 19 and hours <= 23 or hours >= 0 and hours < 6 :
        return "Night"
    else:
        return np.NAN
    
df['Time_Slot']=df.Time.dt.hour.apply(timeslot)
print(df.Time_Slot)

#Q10
repeated_patient_visits=df['id'].value_counts()
print(len(repeated_patient_visits[repeated_patient_visits>1].index))

#Q11
print(repeated_patient_visits[repeated_patient_visits>1].index)

#Q12
x=df[['id','Procedure']]
repeated_patient_visits=x.groupby(['id','Procedure']).size()
print(repeated_patient_visits[repeated_patient_visits>1])

#Q13
Female.Age.median()
Male.Age.median()

#Q14
df.replace(to_replace=df['AmountBalance'].unique()[0], value=np.nan, inplace=True)
df['AmountBalance']=df['AmountBalance'].map(lambda x: str(x).replace(',',''))
df['AmountBalance'] = df['AmountBalance'].astype(float)
print(df['AmountBalance'].sum())

#Q15

Consultation=df[df.Procedure=='Consultation']
Consultation['AmountReceived'].sum()

#Q18
df[(df.Procedure== 'X Rays') | (df.Procedure == 'Scalling')]['AmountReceived'].sum()
