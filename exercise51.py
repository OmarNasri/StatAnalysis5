import pandas as pd


# Read the data from the soft file. First 160 rows and the last row are metadata and can be ignored.
df = pd.read_csv('C:\Koulu\Statistical Data Analysis 5\GDS5037.soft', header=None, skiprows=160, delimiter="\t", dtype=str)

#set the first row as column names
df.columns = df.iloc[0]
df = df[1:]

#use the first column as index
df.set_index(df.columns[0], inplace=True)

#remove last row 
df = df[:-1]

probe_ids = ["A_23_P100011", "A_23_P102083", "A_23_P104323", "A_23_P106562", "A_23_P108673", "A_23_P110686", "A_23_P112646", "A_23_P115223", "A_23_P117582", "A_23_P119617", "A_23_P121716", "A_23_P124084", "A_23_P126613", "A_23_P12884", "A_23_P130948", "A_23_P133146", "A_23_P135079", "A_23_P137634", "A_23_P139704", "A_23_P14184"]
subject_ids = ['GSM1068478', 'GSM1068486', 'GSM1068492', 'GSM1068498', 'GSM1068505', 'GSM1068512', 'GSM1068520', 'GSM1068480', 'GSM1068501', 'GSM1068516', 'GSM1068458', 'GSM1068468', 'GSM1068477', 'GSM1068467', 'GSM1068528', 'GSM1068537', 'GSM1068543', 'GSM1068548', 'GSM1068555', 'GSM1068562']


#filter the df so that all rows not in probe_ids are removed
df = df[df.index.isin(probe_ids)]

#remove all the columns that are not in subject_ids except the IDENTIFIER column
df = df[["IDENTIFIER"]+subject_ids]

print(df)

print("Mean expression level of each probe:")
amount = 0
for i in range(len(df)):
    row = df.iloc[i]
    mean = row[1:].astype(float).mean()
    print(row[0],mean)
    if mean > 10:
        amount += 1

print("Amount of probes with mean expression level over 10:", amount)
        
print("Mean expression level of each subject:")
#calculate the mean for every column
for i in df:
    if i != "IDENTIFIER":
        print(i, df[i].astype(float).mean())
