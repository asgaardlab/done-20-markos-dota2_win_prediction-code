# =========================
# Author: Markos Viggiato 
# Date: May 13, 2020
# =========================

# import necessary libraries
import requests
import json
import os
import csv
import time

# define necessary data structures and directories
list_match_id = list()
list_existing_id = list()
list_to_request_id = list()
output_directory = "matches/"

# open csv file with all matches IDs to make requests to OpenDota API
with open("match_ids.csv", encoding="utf8") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	# skip header
	next(readCSV) 
	for row in readCSV:
		list_match_id.append(row[0])

# use 'set' to get unique values from list while already converting back to list
list_match_id_unique = list(set(list_match_id)) 
print("Number of unique matches in the dataset: ", len(list_match_id_unique))
print("------------------------------------------")

# define iteration and counter variables
iteration = 0
number_requests_made = 0

# loop through the list of match IDs to obtain the match file (in json format)
for id in list_match_id_unique:
	print("Iteration...", iteration)
	iteration += 1
	
	try:
		# request data for a specific match using the opendota API
		r = requests.get("https://api.opendota.com/api/matches/" + id)
		if r.status_code != 200:
			exit(0)
		number_requests_made += 1
		
		# convert response to json and save into a file
		json_match_info = json.loads(r.text)
		with open(output_directory + "match-" + id + ".json", 'w') as f:
			json.dump(json_match_info, f)

		# sleep for 0.8 sec to make sure it is in accordance with OpenDota policies and avoid IP blocking by the OpenDota API
		time.sleep(0.8)
		
	except:
		print(r.status_code)
		exit(0)

print("Number of successfull requests: ", number_requests_made)

## Uncomment this piece of code to check the number of match files in the output directory (if necessary)
# for file in os.listdir(output_directory):
# 	file_id = (file.split('-')[1]).split('.')[0]
# 	list_existing_id.append(file_id)

# print("Number of existing matches : " + str(len(list_existing_id)))
# print("------------------------------------------")
##