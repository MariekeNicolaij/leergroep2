import os.path
import json
import math

# gemeente_veiligheidsregio.json komt hier weg: https://github.com/minvws/nl-covid19-data-dashboard/blob/master/src/data/gemeente_veiligheidsregio.json
# overige data komt hier weg: https://github.com/boisei0/corona-dashboard-data/tree/master/data/2020-10-07_1

from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

# stap 1: open en lezen van gemeente-veiligheidsregio's
with open('data/gemeente_veiligheidsregio.json', 'r') as f:
    regio_data = json.load(f)

# stap 2: zoek de VR (veiligheidsregio) van 'input'' op
regios = ''
while not regios: # Nu kun je niet een niet bestaande stad invullen
    gemeente = input("Geef uw gemeente op: ")
    gemeente = gemeente.capitalize()  # Eerste letter = caps
    print('')  # Beetje whitespace tussen de teksten door
    regios = [x for x in regio_data if x['name'] == gemeente]
regio = regios[0]['safetyRegion']
print("De veiligheidsregio nummer van " + gemeente + " is: " + regio)
print('')  # Beetje whitespace tussen de teksten door
# VR van Groningen = VR01

# stap 3: welke steden zitten er allemaal in dezelfde VR?
gemeentes = [x for x in regio_data if x['safetyRegion'] == regio]
print("Gemeentes in deze regio: ")
for number, ss in enumerate(gemeentes):
    print(number+1, '\t' + ss['name'])  # Wil niet dat lijst bij '0' beginnen vandaar +1
print('')  # Beetje whitespace tussen de teksten door

# Data ophalen en storen in arrays
file_name = 'data/{}.json'.format(regio)
with open(file_name, 'r') as f:
    data = json.load(f)

region_results = data['results_per_region']['values']

data_array = {
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
            data_array[key].append(x[key])

            unixDate = datetime.utcfromtimestamp(x[key]).strftime('%Y-%m-%d')
            dates.append(unixDate)
        else:
            data_array[key].append(x[key])

data_array_length = len(data_array['date_of_report_unix']) # is toch allemaal hetzelfde

# stap 4: vul een datum in
datum = ''
while datum not in dates: # Je kunt alleen een bestaande datum vinden
    datum = input('Geef een geldige datum in het yyyy-mm-dd format op:') # we gebruiken deze format omdat dit ook zo in de data wordt gebruikt
    # waarom print hij al het volgende wanneer je niet een goede datum in vult? en toch blijft ie zeuren om een goede datum

# ---------- Grafieken ----------

# we willen data laten van + 3 dagen en - 3 dagen laten zien
# plus wat checks zodat er altijd 7 dagen worden weergeven
dagen_offset_index = 3
datum_middle_index = dates.index(datum)
# als de middelste index lager is dan de offset dan wordt het de offset
# Dus als de gebruiker dag dag 2 of dag 3 van de hele data reeks somehow invuld dan willen we dat het opzchuift zodat we nog mooi 7 dagen kunnen zien
datum_middle_index = dagen_offset_index if datum_middle_index < dagen_offset_index else datum_middle_index

# hier er dus verder vor zorgen dat de 7 dagen goed geshowed worden
datum_max_index = (datum_middle_index + dagen_offset_index) if (datum_middle_index + dagen_offset_index) < data_array_length else (data_array_length - 1) # index
datum_min_index = (datum_max_index - 6) if (datum_max_index - 6) > 0 else 0 # 7 days in a week en 1 index ding


x = dates[datum_min_index:datum_max_index + 1] # wil niet dat ie de laatste exclude
y = data_array['total_reported_increase_per_region'][datum_min_index:datum_max_index + 1] # wil niet dat ie de laatste exclude
plt.title(regio + ": total_reported_increase_per_region")  # dus niet de gemeente! dat is niet logisch
plt.xlabel("Datum") 
plt.ylabel("Waarde") 
plt.plot(x,y,"ob") 
plt.show()

x = dates[datum_min_index:datum_max_index + 1] # wil niet dat ie de laatste exclude
y = data_array['hospital_total_counts_per_region'][datum_min_index:datum_max_index + 1] # wil niet dat ie de laatste exclude
plt.title(regio + ": hospital_total_counts_per_region") # dus niet de gemeente! dat is niet logisch
plt.xlabel("Datum") 
plt.ylabel("Waarde") 
plt.plot(x,y,"ob") 
plt.show()

# Tim kan jij er voor zorgen: 
# * dat er lijntjes tussen de punten komen of bars
# * dat de gekozen 'datum' een kleurtje krijgt (is niet heel belangrijk)
# * dat het grafiek venster iets groter is zodat die datums niet zo over elkaar heen lopen 
# * zou heel vet zijn als je voor elkaar weet te krijgen hoe we alle grafieken in 1 scherm 
# kunnen houden ipv dat het steeds een nieuw scherm opent als je op kruisje klikt. Dit is mij
# ook niet gelukt hoor. Iets met 'plt.subplot'