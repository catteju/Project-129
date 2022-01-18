import csv

data = []

with open("Final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
name = data[1]
mass_radius_data = data[1:]

for data_point in mass_radius_data:
    data_point[2,3] = data_point[2,3].convert(float)

with open("dwarf.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(name)
    csvwriter.writerows(mass_radius_data)