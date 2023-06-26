import StatScrape
import numpy as np
import seaborn as sns
from scipy import stats 
import matplotlib.pyplot as plt

stats_2023 = StatScrape.getPage('https://www.basketball-reference.com/leagues/NBA_2023_per_game.html')
stat = input("Please give stat you would like to see: ") 
field_goals = stats_2023[stat].tolist()

#Clean Data to get rid of errors
cleanedlist = StatScrape.cleanList(field_goals, stat)
bins = 32

#Create Histogram of sampled data
sns.histplot(data=cleanedlist,  bins=bins)
plt.show() 
s = np.random.normal(0, 1, 2000)

#Shapiro-Wilk Test For samples taken from Normal Distribution
test = stats.shapiro(s)
print(test.pvalue)

#Shapiro-Wilk Test For data
test = stats.shapiro(cleanedlist)
print(test.pvalue)

print("Goodness of Fit for Normal Sampled Data")
StatScrape.goodnessOfFit(s, bins)

print("Goodness of Fit for Basketball stat sampled data")
StatScrape.goodnessOfFit(cleanedlist, bins)