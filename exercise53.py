import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Koulu\\Statistical Data Analysis 5\\53-data.csv")

#calculate the mean of first 5 colums on each weekday and save it to a new dataframe
df2 = df.iloc[:, list(range(5)) + [-1]].groupby('weekday').mean()

#plot the means as a bar plot 
df2.plot.bar()
plt.show()  

df3 = df.iloc[:, list(range(5)) + [-3]].groupby('month').mean()
df3.plot.bar()
plt.show()

df4 = df.iloc[:, 0:5].corr(method='spearman')
print(df4)

#Create scatter plots for each pair of variables

for i in range(5):
    for j in range(5):
        if i != j:
            plt.scatter(df.iloc[:,i], df.iloc[:,j])
            plt.xlabel(df.columns[i])
            plt.ylabel(df.columns[j])
            plt.show()