import csv

path = ''

def new_csv(**args):
    data = [args]

    with open(path, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

def edit_csv(**args):
    rows = []
    with open(path, 'r') as file:
        data = csv.reader(file)
        for row in data:
            if row == args:
                pass # do something
            rows.append(row)

    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)
