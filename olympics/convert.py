"__author__ = JULIAN BOWERS"
import csv

with open('athlete_events.csv', newline='') as f:
	reader = csv.reader(f)
	athlete_events_list = list(reader)
	#your_list contains a list of all rows in athlete_events.csv

column_list = ['id.csv', 'name.csv', 'sex.csv', 'age.csv', 'height.csv', 'weight.csv', 'team.csv', 'noc.csv', 'games.csv', 'year.csv', 'season.csv', 'city.csv', 'sport.csv', 'event.csv', 'medal.csv']
n = 0
for i in column_list:
	temp_list = []
	for j in athlete_events_list:
		temp_list.append(j[n])
		#temp_list contains a list of all j row in athlete_events.csv
	n = n + 1
	
	temp_list_sep = []
	for k in temp_list:
		list_temp_list = [k]
		temp_list_sep.append(list_temp_list)
		#temp_list_sep contains a list of all k row as single element lists for csv row conversion 
	
	#creates a new csv file for each name in column_list.
	with open(i, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for row in temp_list_sep:
			writer.writerow(row)