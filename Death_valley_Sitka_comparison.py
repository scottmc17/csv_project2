import csv
from datetime import datetime 


open_death = open("death_valley_2018_simple.csv", "r")

open_sitka = open("sitka_weather_2018_simple.csv", "r")


csv_death = csv.reader(open_death, delimiter=",")

csv_sitka = csv.reader(open_sitka, delimiter=",")

header_death = next(csv_death)

header_sitka = next(csv_sitka)




for index, column_header in enumerate(header_death):
    if column_header == "TMIN":
        l = index
    elif column_header == "TMAX":
        h = index
    elif column_header == "DATE":
        d = index


highs_death = []
dates_death = []
lows_death = []


highs_sitka = []
dates_sitka = []
lows_sitka = []

#x = datetime.strptime('2018-07-01', '%Y-%m-%d')  #example
#print(x)

#death valley
for row in csv_death:
    try:
        high_death = int(row[h])
        low_death = int(row[l])
        current_date_death = datetime.strptime(row[d],'%Y-%m-%d' )
    except ValueError:
        print(f"Missing data for {current_date_death}")
    else:
        highs_death.append(high_death)
        lows_death.append(low_death)
        dates_death.append(current_date_death)     #append date to list
#sitka
for index, column_header in enumerate(header_sitka):
    if column_header == "TMIN":
        l = index
    elif column_header == "TMAX":
        h = index
    elif column_header == "DATE":
        d = index

for row in csv_sitka:
    try:
        high_sitka = int(row[h])
        low_sitka = int(row[l])
        current_date_sitka = datetime.strptime(row[d],'%Y-%m-%d' )
    except ValueError:
        print(f"Missing data for {current_date_sitka}")
    else:
        highs_sitka.append(high_sitka)
        lows_sitka.append(low_sitka)
        dates_sitka.append(current_date_sitka)     #append date to list



# CHARTS
import matplotlib.pyplot as plt 

# make subplots
fig, ax = plt.subplots(2,1) #runs when its (1,2)

ax[0].plot(dates_sitka, highs_sitka, c="red", alpha=0.5)    #add dates list to plot
ax[0].plot(dates_sitka, lows_sitka, c="blue", alpha=0.5)
ax[1].plot(dates_death, highs_death, c="red", alpha=0.5)    #add dates list to plot
ax[1].plot(dates_death, lows_death, c="blue", alpha=0.5)


#chart title #use ax

ax[0].set_title("Temperature comparison between SITKA AIRPORT, AK US  and DEATH VALLEY, CA US \n \n  SITKA AIRPORT")


plt.title("SITKA AIRPORT, AK US " , fontsize=16) 
plt.ylabel("", fontsize=12)

plt.title("DEATH VALLEY, CA US" , fontsize=16) 
plt.xlabel("", fontsize=12)


ax[1].fill_between(dates_death, highs_death, lows_death, facecolor= 'blue', alpha=0.1)
#plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

ax[0].fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor= 'blue', alpha=0.1)
#plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()

