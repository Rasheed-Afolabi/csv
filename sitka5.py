import csv
from datetime import datetime
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(15, 10))


files = ['sitka_weather_2018_simple.csv', 'death_valley_2018_simple.csv']
subplot_positions = [1, 2]

for file_idx, filename in enumerate(files):
    infile = open(filename, 'r')
    csv_file = csv.reader(infile)
    
    header_row = next(csv_file)
    print(f"\n{filename} Header:")
    print(header_row)
    
    for index, col_header in enumerate(header_row):
        print(index, col_header)
        if col_header == 'TMAX':
            tmax_index = index
        elif col_header == 'TMIN':
            tmin_index = index
        elif col_header == 'DATE':
            date_index = index
        elif col_header == 'NAME':
            name_index = index
    

    csv_file_temp = csv.reader(open(filename, 'r'))
    next(csv_file_temp)
    station_name = next(csv_file_temp)[name_index]
    
    highs = []
    lows = []
    dates = []
    
    for row in csv_file:
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
            some_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {row}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(some_date)
    
    infile.close()
    
    print(f"First 5 values: {highs[:5]}")
    print(f"First 5 dates: {dates[:5]}")
    
    # Create subplot
    plt.subplot(2, 1, subplot_positions[file_idx])
    plt.plot(dates, highs, c='red', alpha=0.8)
    plt.plot(dates, lows, c='blue', alpha=0.8)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title(station_name, fontsize=16)
    plt.ylabel('Temperature (°F)', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)

# Format and show
fig.autofmt_xdate()
plt.suptitle('Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US', fontsize=18, y=0.98)
plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()