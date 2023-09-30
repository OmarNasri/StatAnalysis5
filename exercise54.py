import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

df_image = pd.read_csv("C:\\Koulu\\Statistical Data Analysis 5\\54-image.csv")
df_video = pd.read_csv("C:\\Koulu\\Statistical Data Analysis 5\\54-video.csv")

print(df_image)
print(df_video)

#test both for normality 
print(stats.shapiro(df_image['amount_spent']))
print(stats.shapiro(df_video['amount_spent']))

#perform a mann whitney u test
print(stats.mannwhitneyu(df_image['amount_spent'], df_video['amount_spent']))

