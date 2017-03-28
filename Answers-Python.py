# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import datetime as dt
import dateutil.parser as dparser
from datetime import datetime
df=pd.read_csv("C:/Users/m.salahuddin/Desktop/R Assignments/Assignment2/Python/hospitaldata.csv")



df=df.rename(columns={'Consulting..Doctor': 'ConsultingDoctor', 'Total..Charges': 'TotalCharges',
                                          'Amount..Received.':'AmountReceived', 'Amount..Balance':'AmountBalance',
                                          'Amount.Received.By':'AmountReceivedBy','Amount.in.Hospital':'AmountInHospital',
                                          'Receptionist..Name':'ReceptionistName','Next.Apt':'NextApt'})


def replace_M(x):
    if 'M' in str(x):
        x=x.replace('M','')
        return float(x)/12
    else:
        return float(x)
def conv24_to12(x):
        x=dparser.parse(x)
        return str(x.strftime('%H:%M'))
    
def time_segment(p_hour):
    if p_hour >= 6 and p_hour <12:
        return 'Morning'
    elif p_hour >=12 and p_hour < 16:
        return 'Afternoon'
    elif p_hour >= 16 and p_hour < 19:
        return 'Evening'
    elif (p_hour >=19 and p_hour < 24) or (p_hour >= 0 and p_hour < 6):
        return 'Night'
    else:
        return np.nan

def age_group(p_age):
    if p_age>0 and p_age <=12:
        return 'Children'
    elif p_age>12:
        return 'Elders'
    else:
        return np.nan
#Separate Date column from Day of Week. Prepare new column WeekDay and move Day value in it.
df['Date'] = pd.to_datetime(df['Date'])
df['WeekDay'] = df['Date'].dt.weekday_name
weekday_count_list = df.groupby('WeekDay')['id'].agg(['count'])
#weekday_count_list.columns=['WeekDay_Count']
#weekday_count_list['Week_Day'] =weekday_count_list.index
print('Answer 2 ',weekday_count_list['count'].idxmax())

df.Age[df.Age=='-'] = np.nan
     
      
df.Age=df.Age.map(replace_M)
print('Answer 3 Mean Age = ',df.Age.mean())
#def replace_M(x):
#    if 'M' in x:
#        x.replace('M','')
#        return float(x)/12
      
df.Sex=df.Sex.replace(to_replace='f', value='F')
#df.Sex[df.Sex=='f'] = 'F'
df.Sex[df.Sex=='-'] = np.nan

df[df.Time=='-']=np.nan
  
df.replace(to_replace=df['AmountBalance'].unique()[0], value=np.nan, inplace=True)
df['AmountBalance']=df['AmountBalance'].map(lambda x: str(x).replace(',',''))

print('Answer 4 Age Bracket [1-12]', len(df.Age[df.Age<=12]))
Male_df = df[df.Sex=='M']
Female_df = df[df.Sex=='F']
print('Answer 5, Male Count', Male_df.Procedure.value_counts().idxmax(), Male_df.Procedure.value_counts().max())
print('Answer 5, Female Count', Female_df.Procedure.value_counts().idxmax(), Female_df.Procedure.value_counts().max())

df.TotalCharges = pd.to_numeric(df.TotalCharges, errors='coerce')
print('Answer 6', df.groupby('ConsultingDoctor')['TotalCharges'].sum().idxmax())

print('Answer 7', df.groupby('Procedure')['AmountReceived'].sum().idxmax())


print('Answer 8 Hour:', pd.to_datetime(df.Time).dt.hour.value_counts().idxmax(), 'Max Value:', pd.to_datetime(df.Time).dt.hour.value_counts().max())

df['TimeSlot'] = pd.to_datetime(df.Time).dt.hour.map(time_segment)
print('Answer 9: ', df['TimeSlot'])

patient_wise_count = df['id'].value_counts()
print('Answer 10: ',len(patient_wise_count[patient_wise_count>1]))

print('Answer 11: ',patient_wise_count[patient_wise_count>1])

print('Answer 12: ',df.groupby(['id', 'Procedure']).size()[df.groupby(['id', 'Procedure']).size()>1])

print('Answer 13: Male median age=', Male_df.Age.median(), ', Female median age= ', Female_df.Age.median())

print('Answer 14: ', pd.to_numeric(df.AmountBalance, errors='coerce').sum())

print('Answer 15: ', df.TotalCharges[df.Procedure=='Consultation'].sum())

print('Answer 16: ', df.corr().loc[['Age'], ['TotalCharges']])

df['AgeGroup'] = df.Age.map(age_group)

print('Answer 17: Group: ',df.groupby('AgeGroup').size().idxmax(), 'Group Count: ', df.groupby('AgeGroup').size().max())

print('Answer 18: ', df.TotalCharges[(df.Procedure=='X Ray') | (df.Procedure=='Scaling')].sum())

df.to_csv('C:/Users/m.salahuddin/Desktop/R Assignments/Assignment2/Python/CleanedHospitalData.csv', sep=',')

#Time2=dparser.parse(df['Time'])
#df['TFH_Time']=df.Time.map(conv24_to12)

#print(conv24_to12(df.Time[5]))
#print(df.Time.map(conv24_to12))

#Time2=dparser.parse(TimeValue)


#Time2=dparser.parse(Time_Str)

#print(hospitaldata['TotalCharges'].unique())
#if hospitaldata['Age'].str.contains("M"):





#print(hospitaldata['Age'].mean())

#print(weekday_count_list)
#print(weekday_count_list)


for row in df.itertuples(index=True, name='Pandas'):
    #print (getattr(row, "Date"), getattr(row, "id"))
    Day_Date = getattr(row, "Date")
    #print(Day_Date)
    #first_comma_pos = Day_Date.index(',')
    #first_comma_pos_space = Day_Date.index(', ')
    #CalDate = Day_Date[2+first_comma_pos_space:]
    #WeekDay = Day_Date[:first_comma_pos]
    #np.where(np.logical_and(np.greater_equal(dists,r),np.greater_equal(dists,r + dr))
    
    
    
    
    #hospitaldata[row, 'WeekDay'] =WeekDay
    
    #hospitaldata[row, 'CalDate']=CalDate
    
##print(hospitaldata)
#print(hospitaldata)    
