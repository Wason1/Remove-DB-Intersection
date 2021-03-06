# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
import numpy as np
import os
import re
import glob
import csv
import shutil
#endregion

# INPUT VARIABLES----------------------------------------------------------------------------------------
#region
# Directory folder of the csv files you want to process
Input_path_A = 'D:/TEST/dataA.csv'
# Can change to xlsx if needed, other changes will be nessesary to code

# Directory folder of the csv files you want to process
Input_path_B = 'D:/TEST/dataB.csv'
# Can change to xlsx if needed, other changes will be nessesary to code

Extension = 'csv'
# Csv files seperator for input and output files..generally (,) or (|)
Delimiter = ','

# Output file path of data with intersection Removed
Output_path = 'D:/TEST/data_Output.csv'

# Output file path of data Removed
Output_path_Removed = 'D:/TEST/data_Output_Removed_Data.csv'

# The names of the columns that you want to compare, if they are duplicates they will be removed
Lst_Columns = ['YEAR','MONTH', 'DAY', 'TEST-KEY-CODE', 'SAMPLEPOINT']

print('Directories loaded...')
#endregion

df_A = pd.read_csv(Input_path_A, sep=Delimiter, dtype=object)
print('Created Dataframe A...')
df_B = pd.read_csv(Input_path_B, sep=Delimiter, dtype=object)
print('Created Dataframe B...')


# Create Lists to Check for duplicates
Lst_Row_Key_A = []

for index, row in df_A.iterrows():
    Str_Row = str('')
    for item in Lst_Columns:
        Str_Row = Str_Row + row[item]
    Lst_Row_Key_A.append(Str_Row)
print('Example Row Key from A:', Lst_Row_Key_A[0])

# Create Lists to Check for duplicates
Lst_Row_Key_B = []

for index, row in df_B.iterrows():
    Str_Row = str('')
    for item in Lst_Columns:
        Str_Row = Str_Row + row[item]
    Lst_Row_Key_B.append(Str_Row)
print('Example Row Key from B:', Lst_Row_Key_B[0])

Lst_Bools = []
for item in Lst_Row_Key_A:
    if item in Lst_Row_Key_B:
        Lst_Bools.append(False)
    else:
        Lst_Bools.append(True)
Int_Duplicates = Lst_Bools.count(False)
print('Duplicate Rows:', Int_Duplicates)

# Create Array of Bools
Array_Bools = np.array(Lst_Bools)

# Remove Intersection
df_Out = df_A[Array_Bools]

# Save Intersection as another datafile
Array_Bools_filter_Intersection = np.invert(Array_Bools)
df_Intersection = df_A[Array_Bools_filter_Intersection]

# Create Output file for data with only intersection
df_Intersection.to_csv(path_or_buf=Output_path_Removed, sep=Delimiter, index=False)

# Create Output File for data with intersection removed
df_Out.to_csv(path_or_buf=Output_path, sep=Delimiter, index=False)
