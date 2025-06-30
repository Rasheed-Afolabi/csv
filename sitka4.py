import csv
from datetime import datetime


infile  = open('death_valley_2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
lows = []
dates = []

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        some_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {some_date}")
    else:
        highs.append(high)
        lows.append(low)
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