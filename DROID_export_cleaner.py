import csv
import os


#### make sure this filename is the same as the one on your system
csv_filename = r"thread0.csv"

########### do not edit below this line #################

if not os.path.exists(csv_filename):
	quit("Can't find the log file '{}', please check your filename".format(csv_filename))

cleaned_csv_data = []

with open(csv_filename) as data:
	csv_reader = csv.reader(data)
	for row in csv_reader:
		if row[8] != "Folder":
			cleaned_csv_data.append(row[4:])

headers = cleaned_csv_data[0]
cleaned_csv_data.remove(headers)
cleaned_csv_data.sort()

with open("cleaned_csv.csv", "wb") as data:
	writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	writer.writerow(headers)
	for row in cleaned_csv_data:
		writer.writerow(row)