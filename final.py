import csv

dataset_1 = []
dataset_2 = []

with open("dwarf.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("Final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
sun_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
dwarf_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
final_data = []
for index, data_row in enumerate(sun_data_1):
    final_data.append(sun_data_1[1,2,3,4] + dwarf_data_2[1,2,3,4,5,6])

with open("final_data", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_data)

    