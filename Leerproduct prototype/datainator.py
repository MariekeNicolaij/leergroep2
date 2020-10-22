import os.path
import json
import math

from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

# stap 1: open en lezen van gemeente-veiligheidsregio's
# dit bestand komt hier weg: https://github.com/minvws/nl-covid19-data-dashboard/blob/master/src/data/gemeente_veiligheidsregio.json
with open('data/gemeente_veiligheidsregio.json', 'r') as f:
    regio_data = json.load(f)

# print (type(regio_data)) # list
#print (regio_data[1])
#print (regio_data[2])4


# Nu kun je niet een niet bestaande stad invullen
regios = ''
while not regios:
    # stap 2: zoek de VR (veiligheidsregio) van Groningen op
    # stad = "Groningen"
    stad = input("Geef uw stad op: ")
    stad = stad.capitalize()  # Eerste letter = caps
    print('')  # Beetje whitespace tussen de teksten door
    regios = [x for x in regio_data if x['name'] == stad]
regio = regios[0]['safetyRegion']
print("De veiligheidsregio nummer van " + stad + " is: " + regio)
print('')  # Beetje whitespace tussen de teksten door
# VR van Groningen = VR01

# stap 3: welke steden zitten er allemaal in dezelfde VR?
steden = [x for x in regio_data if x['safetyRegion'] == regio]
print("Gemeentes in deze regio: ")
for number, ss in enumerate(steden):
    print(number+1, '\t' + ss['name'])  # Wil niet bij '0' beginnen vandaar +1
print('')  # Beetje whitespace tussen de teksten door

# Nu kun je geen verkeerde datum invullen
file_name = 'data/{}.json'.format(regio)

# Data ophalen en storen in arrays
with open(file_name, 'r') as f:
    data = json.load(f)

region_results = data['results_per_region']['values']

dataArray = {
    'date_of_report_unix': [],
    'vrcode': [],
    'total_reported_increase_per_region': [],
    'infected_total_counts_per_region': [],
    'hospital_total_counts_per_region': [],
    'infected_increase_per_region': [],
    'hospital_increase_per_region': [],
    'infected_moving_avg_per_region': [],
    'hospital_moving_avg_per_region': [],
    'date_of_insertion_unix': []
}

# Setting dates array for date input verification
dates = []

for x in region_results:
    for key in x:
        if (key == 'date_of_report_unix'):
            dataArray[key].append(x[key])

            unixDate = datetime.utcfromtimestamp(x[key]).strftime('%Y-%m-%d')
            dates.append(unixDate)
        else:
            dataArray[key].append(x[key])

datum = ''
while datum not in dates :
    datum = input('Geef een geldige datum in het yyyy-mm-dd format op:')

# Write data to console view
print('--------------------------------------------------')
print("Gemeente: " + stad + "\t" + "Bijgewerkt: " + dates[-1])
print('')

total = 0

# total_reported_increase_per_region
for x in dataArray['total_reported_increase_per_region']:
    total = total + x
average = total / len(dataArray['total_reported_increase_per_region'])

print("Total reported: ", total)
print("Average per day: ", round(average))
print('')

# infected_total_counts_per_region
for x in dataArray['infected_total_counts_per_region']:
    total = total + x
average = total / len(dataArray['infected_total_counts_per_region'])

print("Total infected: ", math.floor(total))
print("Average per day: ", average)
print('')

# hospital_total_counts_per_region
for x in dataArray['hospital_total_counts_per_region']:
    total = total + x
average = total / len(dataArray['hospital_total_counts_per_region'])

print("Total in hospital: ", math.floor(total))
print("Average per day: ", average)
print('')

# infected_increase_per_region
for x in dataArray['infected_increase_per_region']:
    total = total + x
average = total / len(dataArray['infected_increase_per_region'])

print("Total infected increase: ", math.floor(total))
print("Average per day: ", average)
print('')

# hospital_increase_per_region
for x in dataArray['hospital_increase_per_region']:
    total = total + x
average = total / len(dataArray['hospital_increase_per_region'])

print("Total hospital increase: ", math.floor(total))
print("Average per day: ", average)
print('')

# hospital_moving_avg_per_region
for x in dataArray['hospital_moving_avg_per_region']:
    total = total + x
average = total / len(dataArray['hospital_moving_avg_per_region'])

print("Total hospital moving average: ", math.floor(total))
print("Average per day: ", average)
print('')

# Bereken totale rna per ml van gegeven data en regio
# for d in data['results_per_sewer_installation_per_region']['values'][0]['values']:
#     TOTAL_rna = TOTAL_rna + d['rna_per_ml']

# print("Total ribonucleïnezuur (rna) per ml", TOTAL_rna)
print('--------------------------------------------------')
print('')
print('')


# eem wat proberen

x = np.arange(0,DATA_length) 
# y = 2 * x + 5 
y = [i for i in DATA_total_reported_increase_per_region]
plt.title(stad + " " + datum) 
plt.xlabel("Data object #") 
plt.ylabel("DATA_total_reported_increase_per_region") 
plt.plot(x,y,"ob") 

plt.show()