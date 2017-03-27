# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 10:48:54 2017

@author: Ali.Ejaz
"""

import pandas as pd
import numpy as np


raw_data=pd.read_csv("D://diHub//Assessment2_RandPython_Marked//aliejaz1749_khi_r_assignment2//hospitaldata.csv")



# Qus1. Please remove the dots in the names, so it may become easier for you to work through it.
raw_data = raw_data.rename(columns={col: col.replace('.',"") for col in raw_data.columns})
raw_data = raw_data.rename(columns={col: col.replace("..","") for col in raw_data.columns})
raw_data = raw_data.rename(columns={col: col.strip() for col in raw_data.columns})
#print(raw_data)

# Qus2. Which day of the week is expected to have most visits?
#max_date_pat=raw_data['Date'].map(lambda x: x.split(',')[0])
#max_date_pat=max_date_pat.value_counts().index.tolist()
#print(max_date_pat[0])

# Qus3. What is the average age of patients?
#p_avg_age =pd.to_numeric(raw_data['Age'],errors='coerce' )
#print(p_avg_age.mean())


# Qus4. How many children were entertained? (Make a Bracket of Age from 1-12)
#p_ent_child=raw_data[pd.to_numeric(raw_data['Age'],errors='coerce' )<=12]
#print(p_ent_child)
#print(len(p_ent_child.index))

# Qus5. Which gender type had what kind of procedure in abundance? i.e. Female visit mostly because of Gynae Problem
#Female=raw_data[(raw_data.Sex=='F')| (raw_data.Sex=='f')]
#print(Female['Procedure'].value_counts().index.tolist()[0])

# Qus6. Which Doctor is earning highest?
#raw_data['TotalCharges'] = pd.to_numeric(raw_data['TotalCharges'],errors='coerce')
#con_dr_amt = raw_data[['ConsultingDoctor', 'TotalCharges']].groupby(['ConsultingDoctor']).sum()
#print(con_dr_amt.max())

# Qus7. Which procedure type earns more money?
p_proc_typ_high = raw_data[['Procedure', 'TotalCharges']].groupby(['Procedure']).sum()
print(p_proc_typ_high.max())


# Qus8. Which time of the day has highest frequency of visits by hour?
# Qus9. Create a bracket of time by Morning, Afternoon, Evening, Night (6am – 12pm – Morning, 12 pm- 4 pm, Afternoon, 4 pm- 7pm, Evening, 7pm – 6 am, Night).
# Qus10. How many patients are repeated visitors?
# Qus11. Give us the id of repeated visitors.
# Qus12. Which patients visited again for the same problem?
# Qus13. What is the median age for Females and Males?
# Qus14. What is the total amount in balance?
# Qus15. How much money was made by Procedure Type “Consultation”?
# Qus16. Is there a relation between Age and Total Charges paid?
# Qus17. Which Age group had highest number of visits?
# Qus18. What is the total cost earned by Procedure Type X Ray and Scalling together?