import os.path
import json
import math

import numpy as np
from matplotlib import pyplot as plt

# stap 1: open en lezen van gemeente-veiligheidsregio's
# dit bestand komt hier weg: https://github.com/minvws/nl-covid19-data-dashboard/blob/master/src/data/gemeente_veiligheidsregio.json
with open('data/gemeente_veiligheidsregio.json', 'r') as f:
    regio_data = json.load(f)

# print (type(regio_data)) # list
#print (regio_data[1])
#print (regio_data[2])


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
file_name = ''
while not os.path.isfile(file_name):
    datum = input('Geef een datum in de format van yyyy-mm-dd op:')
    file_name = 'data/{}_1/{}.json'.format(datum, regio)
print('')

# Get data from given date and region
with open(file_name, 'r') as f:
    data = json.load(f)

# De objecten van de resultaten per regio
region_results = data['results_per_region']['values']
decimalen = 2

# data length
DATA_length = len(region_results)

# Initiate data arrays
DATA_rna = 0
DATA_total_reported_increase_per_region = []
DATA_infected_total_counts_per_region = []
DATA_hospital_total_counts_per_region = []
DATA_infected_increase_per_region = []
DATA_hospital_increase_per_region = []
DATA_hospital_moving_avg_per_region = []

for d in region_results:
    DATA_total_reported_increase_per_region.append(d['total_reported_increase_per_region'])
    DATA_infected_total_counts_per_region.append(d['infected_total_counts_per_region'])
    DATA_hospital_total_counts_per_region.append(d['hospital_total_counts_per_region'])
    DATA_infected_increase_per_region.append(d['infected_increase_per_region'])
    DATA_hospital_increase_per_region.append(d['hospital_increase_per_region'])
    DATA_hospital_moving_avg_per_region.append(d['hospital_moving_avg_per_region'])

# Initiate totales
TOTAL_rna = 0
TOTAL_total_reported_increase_per_region = 0
TOTAL_infected_total_counts_per_region = 0
TOTAL_hospital_total_counts_per_region = 0
TOTAL_infected_increase_per_region = 0
TOTAL_hospital_increase_per_region = 0
TOTAL_hospital_moving_avg_per_region = 0

# Get data from given region
print('--------------------------------------------------')
print("Gemeente: " + stad + "\t" + "Datum: ", datum)
print('')

# totalen berekenen
for i in range(DATA_length):
    TOTAL_total_reported_increase_per_region += DATA_total_reported_increase_per_region[i]
    TOTAL_infected_total_counts_per_region += DATA_infected_total_counts_per_region[i]
    TOTAL_hospital_total_counts_per_region += DATA_hospital_total_counts_per_region[i]
    TOTAL_infected_increase_per_region += DATA_infected_increase_per_region[i]
    TOTAL_hospital_increase_per_region += DATA_hospital_increase_per_region[i]
    TOTAL_hospital_moving_avg_per_region += DATA_hospital_moving_avg_per_region[i]

# calculate average
AVERAGE_total_reported_increase_per_region = round(DATA_length / TOTAL_total_reported_increase_per_region, decimalen) if TOTAL_total_reported_increase_per_region > 0 else 0
AVERAGE_infected_total_counts_per_region = round(DATA_length / TOTAL_infected_total_counts_per_region, decimalen) if TOTAL_infected_total_counts_per_region > 0 else 0
AVERAGE_hospital_total_counts_per_region = round(DATA_length / TOTAL_hospital_total_counts_per_region, decimalen) if TOTAL_hospital_total_counts_per_region > 0 else 0
AVERAGE_infected_increase_per_region = round(DATA_length / TOTAL_infected_increase_per_region, decimalen) if TOTAL_infected_increase_per_region > 0 else 0
AVERAGE_hospital_increase_per_region = round(DATA_length / TOTAL_hospital_increase_per_region, decimalen) if TOTAL_hospital_increase_per_region > 0 else 0
AVERAGE_hospital_moving_avg_per_region = round(DATA_length / TOTAL_hospital_moving_avg_per_region, decimalen) if TOTAL_hospital_moving_avg_per_region > 0 else 0

# total_reported_increase_per_region
print("Total reported: ", TOTAL_total_reported_increase_per_region)
print("Average: ", AVERAGE_total_reported_increase_per_region)
print('')

# infected_total_counts_per_region
print("Total infected: ", math.floor(TOTAL_infected_total_counts_per_region))
print("Average: ", AVERAGE_infected_total_counts_per_region)
print('')

# hospital_total_counts_per_region
print("Total in hospital: ", math.floor(TOTAL_hospital_total_counts_per_region))
print("Average: ", AVERAGE_hospital_total_counts_per_region)
print('')

# infected_increase_per_region
print("Total infected increase: ", math.floor(TOTAL_infected_increase_per_region))
print("Average: ", AVERAGE_infected_increase_per_region)
print('')

# hospital_increase_per_region
print("Total hospital increase: ", math.floor(TOTAL_hospital_increase_per_region))
print("Average: ", AVERAGE_hospital_increase_per_region)
print('')

# hospital_moving_avg_per_region
print("Total hospital moving average: ", math.floor(TOTAL_hospital_moving_avg_per_region))
print("Average: ", AVERAGE_hospital_moving_avg_per_region)
print('')

# Bereken totale rna per ml van gegeven data en regio
for d in data['results_per_sewer_installation_per_region']['values'][0]['values']:
    TOTAL_rna = TOTAL_rna + d['rna_per_ml']

print("Total ribonucleïnezuur (rna) per ml", TOTAL_rna)
print('--------------------------------------------------')
print('')
print('')


# eem wat proberen

x = np.arange(0,DATA_length) 
# y = 2 * x + 5 
y = [i for i in DATA_total_reported_increase_per_region]
plt.title(datum) 
plt.xlabel("Data object #") 
plt.ylabel("DATA_total_reported_increase_per_region") 
plt.plot(x,y,"ob") 

plt.show()