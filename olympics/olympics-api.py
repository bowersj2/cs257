'''
	olympics-api.py
	Julian Bowers
	CS257 - Software Design
	10/28/2021
'''

import flask
import json
import argparse
import sys
import csv

app = flask.Flask(__name__)


#reads csv files and converts data into python dictionaries

with open('games.csv', newline='') as f:
	reader = csv.reader(f)
	games_list = list(reader)
	
with open('noc.csv', newline='') as g:
	reader2 = csv.reader(g)
	nocs_list = list(reader2)

@app.route('/games')
def games():
	#returns a list of dictionaries with all games
	return json.dumps(games_list)

@app.route('/nocs')
def nocs():
	#returns a list of dictionaries with all nocs
	return json.dumps(nocs_list)

if __name__ == '__main__':
	parser = argparse.ArgumentParser('Flask API')
	parser.add_argument('host', help='localhost')
	parser.add_argument('port', type=int, help='5000')
	arguments = parser.parse_args()
	app.run(host=arguments.host, port=arguments.port, debug=True)