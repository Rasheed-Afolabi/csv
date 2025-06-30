# 1) Changing the file to include all the data for the year of 2018
# 2) Change the title to - Daily and low high temperatures - 2018
# 3) Extract low temps from the file and add to chart
# 4) Shade in the area between high and low

import csv
from datetime import datetime


infile  = open('sitka_weather_2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
lows = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    some_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(some_date)

    
print(highs[:5])
print(lows[:5])
print(dates[:5])
    
    

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c ='red')
plt.plot(dates, lows, c ='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily and low high temperatures - 2018", fontsize=20)
plt.xlabel('')
plt.ylabel('Temp (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

fig.autofmt_xdate()



plt.show()