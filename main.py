import sys
import csv
i = input()
k = input()
s = input()
with open("kmd.csv", "r") as file:
		reader = csv.DictReader(file)

		for line in reader:
			print(line[i], line[k], line[s])

sys.exit()