import pandas as pd
import numpy as np
from scipy import stats
from sklearn import datasets
import random
#--------------------------------------------------------------------- 
#  This is just a basic file to work on getting the .csv data
#  into Python, and doing some manipulations. Mostly just the
#  basic statistical data we practiced in class so far. 
#---------------------------------------------------------------------

#Allows the terminal to display up to 8 columns. Pandas automatically
#truncates the columns / rows unless a max is stated
pd.set_option('display.max_columns', 8)

#Reads the .csv file using pandas and assigns to data
data = pd.read_csv("card_transdata.csv")

### Getting the data from the csv file ###

#Distance from home
distance_from_home = data['distance_from_home'][:].tolist()
#print(distance_from_home[0:20])

#Distance from last transaction
distance_from_last_transaction = data['distance_from_last_transaction'][:].tolist()
#print(distance_from_last_transaction[0:20])

#Ratio to median purchase price
ratio_to_median_purchase = data['ratio_to_median_purchase_price'][:].tolist()
#print(ratio_to_median_purchase[0:20])

#Repeat Retailer
repeat_retailer = data['repeat_retailer'][:].tolist()
#print(repeat_retailer[0:20])

#Used a chip
chip = data['used_chip'][:].tolist()
#print(chip[0:20])

#Used a pin number
pin = data['used_pin_number'][:].tolist()
#print(pin[0:20])

#Online order
online = data['online_order'][:].tolist()
#print(online[0:20])

#Fraud
fraud = data['fraud'][:].tolist()
#print(fraud[0:20])

varArray = [distance_from_home, distance_from_last_transaction, ratio_to_median_purchase, 
            repeat_retailer, chip, pin, online, fraud]

#Size of testing dataset
testSize = 1000

#Selecting random assortment of distance from home values
random_DFH = []     #Array containing the random distance from home values
#While loop can be configured for however large the testing set will be
while len(random_DFH) < testSize:
    randomInt = random.randint(1,30000)
    randomDistance = distance_from_home[randomInt]
    if randomDistance not in random_DFH:
        random_DFH.append(randomDistance)

#Selecting random assortment of distance from last transaction values
random_DLT = []     #Array containing the random distance from last transaction values
while len(random_DLT) < testSize:
    randomInt = random.randint(1,30000)
    randomDistance = distance_from_last_transaction[randomInt]
    if randomDistance not in random_DLT:
        random_DLT.append(randomDistance)

#Checking Correlation Covariance Matrix
numpyData = data.to_numpy()
distances = np.transpose(numpyData[:testSize, [0,1]])
#print(np.corrcoef(distances))

### Calculating basic statistical values, rounded for ease of viewing ###

#Mean
mean = []
for column in varArray:
    m = round(np.mean(column), 2)
    mean.append(m)
print("Mean Values: \n", mean)

#%10 trimmed mean
trimmedMean = []
for column in varArray:
    tm = round(stats.trim_mean(column, 0.1), 2)
    trimmedMean.append(tm)
print("Trimmed Mean: \n", trimmedMean)

#Median
median = []
for column in varArray:
    med = round(np.median(column), 2)
    median.append(med)
print("Median Values: \n", median)

#Mode
mode = []
for column in varArray:
    md = stats.mode(column)
    mode.append(md)
print("Mode Values: \n", mode)

#Frequency
frequency = []
for column in varArray:
    freq = stats.itemfreq(column)
    frequency.append(freq)
#not printing frequencies because would be far too many rows
#Can switch to new function for frequencies too

#Range
range = []
for column in varArray:
    r = round(np.max(column) - np.min(column), 2)
    range.append(r)
print("Range: \n", range)

#Variance
variance = []
for column in varArray:
    v = round(np.var(column), 2)
    variance.append(v)
print("Variance: \n", variance)

#Standard Deviation
standardDeviation = []
for column in varArray:
    sd = round(np.std(column), 2)
    standardDeviation.append(sd)
print("Standard Deviations: \n", standardDeviation)

#Percentiles
percentile = []
for column in varArray:
    per = round(np.percentile(column, 50), 2)
    percentile.append(per)
print("nth Percentiles: \n", percentile)



