# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:13:18 2017

@author: Shayan.Ishaq
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import datetime
import dateutil.parser as dparser


df = pd.read_csv('E:/DIH/hospitaldata.csv')
print (df)


#Q1

#df = df.rename(columns={col: col.replace('.'," ") for col in df.columns})

df = df.rename(columns={col: col.replace('.'," ") for col in df.columns})

##
df["Total Charges"]=pd.to_numeric(df["Total Charges"],errors="coerce")

df.Date=pd.to_datetime(df.Date)

print(df)

#Q2

max_date_pat=df['Date']
max_date_pat=df['Date'].map(lambda x: x.split(',')[0])
#print (max_date_pat)
max_date_pat=max_date_pat.value_counts().index.tolist()
print(max_date_pat[0])

#Q3

df.Age.replace("[^0-9]",'',regex=True,inplace=True)
df.Age.replace("",np.nan,regex=True,inplace=True)
x = np.array(df.Age).astype(float)
print("Average Age is ",str(np.nanmean(x)))
#v_age=pd.to_numeric(df['Age'],errors='coerce' )
#v_age.mean()

#Q4

v_count = df[(df.Age<= 21) & (df.Age >= 1)] 
print(len(v_count))

#Q5

v_male = df[df.Sex=='M']
v_male=v_male['Procedure'].value_counts().index.tolist()[0]
print (v_male)

v_Fmale = df[df.Sex=='F']
v_Fmale=v_Fmale['Procedure'].value_counts().index.tolist()[0]
print (v_Fmale)


#Q6


a= (df.groupby(['Consulting Doctor'])["Total Charges"].sum().idxmax())
print(a)

#Q7

a= (df.groupby(['Procedure'])["Total Charges"].sum().idxmax())
print(a)

#Q8
df.Time=pd.to_datetime(df.Time,errors = 'coerce')

print(datetime.datetime.strptime(str(df.Time.dt.hour.value_counts().idxmax()), '%H.%M').strftime("%I:%M %p"))


#Q10

print(len(df.id.value_counts()[df.id.value_counts()>1].index))


#Q11

print(df.id.value_counts()[df.id.value_counts()>1].index)

#Q12
print(list(df.groupby("id")["Specialty"].value_counts()[df.groupby("id")["Specialty"].value_counts()>1].index))

#Q13
df.Age=pd.to_numeric(df.Age,errors = 'coerce')
print(df.groupby("Sex")["Age"].median())

#Q14


numeric_columns= ['Age', 'Total Charges', 'Amount Received', 'Amount Balance', 'Amount in Hospital']

for i in numeric_columns:
    df[i] = pd.to_numeric(df[i], errors='coerce')
    
bal_amnt = df['Amount Balance']
bal_amnt.replace(to_replace=',', value='', inplace=True)
print(df['Amount Balance'].sum())


