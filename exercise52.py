import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api 

# Read the data from the soft file. First 160 rows and the last row are metadata and can be ignored.
df = pd.read_csv('C:\Koulu\Statistical Data Analysis 5\GDS5037.soft', header=None, skiprows=160, delimiter="\t", dtype=str)

#set the first row as column names
df.columns = df.iloc[0]
df = df[1:]

#use the first column as index
df.set_index(df.columns[0], inplace=True)

#remove last row 
df = df[:-1]

with open ('52-probes.ids') as f:
    probe_ids = f.read().splitlines()

with open('52-control.ids') as f:
    lines = f.read().splitlines()
    subject_ids = lines[:]
    controls= lines[:]

with open('52-asthma.ids') as f:
    lines = f.read().splitlines()
    subject_ids += lines[:]
    asthmas = lines[:]

#filter the df so that all rows not in probe_ids are removed
df = df[df.index.isin(probe_ids)]

#remove all the columns that are not in subject_ids except the IDENTIFIER column
df = df[["IDENTIFIER"]+subject_ids]

#specify all the values as float except the IDENTIFIER column
df = df.astype({col: float for col in df.columns if col != "IDENTIFIER"})

# boxplot all the columns on the same plot except the IDENTIFIER column
#df.iloc[:,1:].boxplot()
#plt.show()

#create a copy of the df in df2 and remove the IDENTIFIER column. 
df2 = df.copy()
df2 = df2.drop(columns=["IDENTIFIER"])

df2_transposed = df2.T

#Create subdataframes of controls and asthmas
df2_controls = df2_transposed[df2_transposed.index.isin(controls)]
df2_asthmas = df2_transposed[df2_transposed.index.isin(asthmas)]


#Calculate the t-test for the df2_controls and df2_asthmas dataframes of each column and store the results in a list with only the corresponding column name and p-value
ttest_results = []
for col in df2_controls.columns:
    ttest_results.append([col, stats.ttest_ind(df2_controls[col], df2_asthmas[col])[1]])
  
#correct the p-values with the Benjamini-Hochberg method
corrected_pvalues = statsmodels.stats.multitest.fdrcorrection([x[1] for x in ttest_results])[1]

#create a new list with the column names and the corrected p-values
corrected_ttest_results = []
for i in range(len(corrected_pvalues)):
    corrected_ttest_results.append([ttest_results[i][0], corrected_pvalues[i]])

#print all the rows of the list that have a corrected p-value under 0.05
print("Rows with corrected p-value under 0.05:")
for row in corrected_ttest_results:
    if row[1] < 0.05:
        print(row)
print("Amount of rows with corrected p-value under 0.05:", len([x for x in corrected_ttest_results if x[1] < 0.05]))

#sort the list in ascending order based on the corrected p-values
corrected_ttest_results.sort(key=lambda x: x[1])

#print the first 10 rows of the list
print("First ten rows of the sorted lsit: ")
print(corrected_ttest_results[:10])

#plot histograms of the t-test p values and the corrected p values on their own plot with 10 bins
fig, axs = plt.subplots(2)
axs[0].hist([x[1] for x in ttest_results], bins=10)
axs[0].set_title("T-test p-values")
axs[1].hist(corrected_pvalues, bins=10)
axs[1].set_title("Corrected p-values")
plt.show()




