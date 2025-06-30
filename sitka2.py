import csv
from datetime import datetime


infile  = open('sitka_weather_07-2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    some_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(some_date)

    
print(highs[:5])
print(dates[:5])
    
    

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c ='red')

plt.title("Daily high temperatures, July 2018", fontsize=20)
plt.xlabel('')
plt.ylabel('Temp (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

fig.autofmt_xdate()



plt.show()