import csv

def get_login_data(file_path):

    rows = []

    with open(file_path, newline='') as file:

        data = csv.reader(file)

        next(data)

        for row in data:
            rows.append(row)

    return rows