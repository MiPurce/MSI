import csv
from datetime import datetime
CSV_COMPLETE_PATH = '/Users/purcell/Code/LauraResearch/messed_up_dates_data_sample.csv'

csv_data = []

with open(CSV_COMPLETE_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        new_row = []
        for value in row:
            try:
                new_row.append(datetime.strptime(value, "%d-%m-%y").strftime("%Y-%m-%d"))
            except ValueError:
                new_row.append(value)
        csv_data.append(new_row)


with open(CSV_COMPLETE_PATH, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for x in csv_data:
        spamwriter.writerow(x)
