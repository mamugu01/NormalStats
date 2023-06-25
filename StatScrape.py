import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats 

#Function takes in a URL and returns a Pandas table of the list of stats for the 2023 season
def getPage(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id="per_game_stats")
    stats_2023 = pd.read_html(str(table))[0]
    return stats_2023
    
        
 
   
#Function takes in a list of data datascraped from the stats website, and the name of the stat you want to scrape(
# according to the table on Basketball Reference) and returns a list of a sample taken for each player
def cleanList(list, stat):
    list_fixed = []
    for x in list:
        if x != stat and x != ' nan ':
            list_fixed.append(x)


    list_fixed = [x for x in list_fixed if str(x) != 'nan']
    cleanedlist = []
    for x in list_fixed:
        cleanedlist.append(float(x))

    return cleanedlist
   
#Function takes in a set of cleaned data and the number of bins requested and performs a goodness of fit test
# to see if the data is normally distributed result is printed out.
def goodnessOfFit(data, bins):
    data.sort()
    mean = np.mean(data)
    std = np.std(data)
    interval = []
    for i in range(1,bins + 1):
        val = stats.norm.ppf(i/bins, mean, std)
        interval.append(val)
    interval.insert(0, -np.inf)
    
    
    df = pd.DataFrame({'lower_limit':interval[:-1], 'upper_limit':interval[1:]})
    expected_freqs= calculate_expected(data, interval, mean, std, bins)
    
    df['obs_freq'] = df.apply(lambda x:sum([i>x['lower_limit'] and i<=x['upper_limit'] for i in data]), axis=1)
    df['exp_freq'] = expected_freqs
    
    stats.chisquare(df['obs_freq'], df['exp_freq'])
     # number of parameters
    p = 2   
    DOF = len(df['obs_freq']) - p -1
    cal_value = stats.chisquare(df['obs_freq'], df['exp_freq'])
    chi_value = stats.chi2.ppf(0.95, DOF)
    print('calculated value =' + str(cal_value))
    print('critical value = '+ str(chi_value))

    if cal_value.statistic < chi_value:
        print("Null hypothesis cannot be rejected and the given data is normally distributed")
    else:
        print("Null hypothesis must be rejected and the data is not normally distributed")


#Function takes cleaned data, the intervals for the distribution, the mean and standard deviation of the 
# sampled data, and the number of bins and returns the number of expected samples per bucket
def calculate_expected(data, intervals, mean, std, bins):
    expected_freq = []
    for i in range(0,bins):
        expected_freq.append((stats.norm(mean, std).cdf(intervals[i + 1]) - stats.norm(mean, std).cdf(intervals[i])) * len(data)) 
    return expected_freq




