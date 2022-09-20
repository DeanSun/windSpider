import csv

with open(file=r'F:\workspace-python\windSpider\test.csv', mode='r', encoding='UTF-8') as csvFile:
    csv_reader = csv.reader(csvFile)
    for row in csv_reader:
        print(row)
        print(row[0])
