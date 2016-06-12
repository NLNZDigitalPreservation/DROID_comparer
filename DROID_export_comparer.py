import csv
import os

#### make sure these file names are the same as the ones on your system
baseline_csv = r"baseline.csv"
new_csv = r"cleaned_csv.csv"

########### do not edit below this line #################

baseline_as_rows = []
new_as_rows = []

if not os.path.exists(baseline_csv):
	quit("The baseline log csv file is not found - please check your filename '{}'".format(baseline_csv))
if not os.path.exists(new_csv):
	quit("Your local log csv file is not found - please check your filename '{}'".format(new_csv))

with open(baseline_csv) as data:
	baseline_as_csv = csv.reader(data)
	for row in baseline_as_csv:
		baseline_as_rows.append(row)
	with open(new_csv) as new_data:
		new_rows = csv.reader(new_data)
		for row in new_rows:
			new_as_rows.append(row)

		if len(baseline_as_rows) != len(new_as_rows):
			quit("Your csv log file '{}' does not have the same number of rows as the baseline log '{}'.".format(new_csv, baseline_csv))
		else:
			print "Your csv log file '{}' has the same number of rows as the baseline log '{}'.".format(new_csv, baseline_csv)
			print 

		for i, row in enumerate(baseline_as_rows):
			if row != new_as_rows[i]:
				print "Different row data detected in row #{}".format(i+1)
				print "Baseline: \t{}".format(row) 
				print "New: \t\t{}".format(new_as_rows[i])
				print
		print "Comparison complete. If you do not see any rows indicated as 'different' your log file is the same as the baseline. Congrats!\nIf you see rows indicated as 'different' check your DROID settings and try again\n\n" 
