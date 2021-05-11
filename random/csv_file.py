import csv

with open('data.csv', 'a') as file:
    field_name = ['name', 'age']
    data = {
        'name': 'Shefalika Pathak',
        'age': '44'
    }
    writer = csv.DictWriter(file, fieldnames=field_name)
    # writer.writeheader()
    writer.writerow(data)

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['age'])