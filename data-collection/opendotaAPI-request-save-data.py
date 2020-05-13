import requests
import json
import os
import csv
import time

list_match_id = list()
list_existing_id = list()
list_to_request_id = list()
output_directory = "matches/"

# Open csv file with all matches IDs to make requests to OpenDota API
with open("match_ids.csv", encoding="utf8") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV) # skip header
	for row in readCSV:
		list_match_id.append(row[0])

list_match_id_unique = list(set(list_match_id)) # use 'set' to get unique values from list while already converting back to list
print("Number of unique matches in the dataset: ", len(list_match_id_unique))
print("------------------------------------------")

iteration = 0
number_requests_made = 0

for file in os.listdir(output_directory):
	file_id = (file.split('-')[1]).split('.')[0]
	list_existing_id.append(file_id)

print("Number of existing matches : " + str(len(list_existing_id)))

# existing_id_file = open('list_existing_id.txt', 'r')
# for id in existing_id_file:
# 	list_existing_id.append(id)
# print("Number of existing matches : " + str(len(list_existing_id)))


# for id in list_match_id_unique:
# 	if id not in list_existing_id:
# 		list_to_request_id.append(id)

# with open('list_to_request_id.txt', 'w') as f:
#     for item in list_to_request_id:
#         f.write("%s\n" % item)

        
# with open('list_existing_id.txt', 'w') as f:
#     for item in list_existing_id:
#         f.write("%s\n" % item)


for id in list_match_id_unique:
	print(id)
	if id in list_existing_id:
		print("exist...")
		continue

	print("DO NOT exist...")
	print("Iteration...", iteration)
	iteration += 1
	try:
		# Request data for a specific match using opendota API
		r = requests.get("https://api.opendota.com/api/matches/" + id)
		number_requests_made += 1
		if r.status_code != 200:
			exit(0)

		# Convert response to json and save into a file
		json_match_info = json.loads(r.text)
		with open(output_directory + "match-" + id + ".json", 'w') as f:
			json.dump(json_match_info, f)

		# Sleep for 0.5 sec to be in accordance with OpenDota policies and avoid IP blocking by the OpenDota API
		time.sleep(0.8)
		
	except:
		print(r.status_code)
		exit(0)

print("Number of successfull requests: ", number_requests_made)