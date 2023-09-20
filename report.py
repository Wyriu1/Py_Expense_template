from PyInquirer import prompt
import csv

def get_report():
    with open('expense_report.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in spamreader:
            if len(row) < 2:
                print("report done")
                return

            share = int(row[2]) / (len(row) - 2.0)
            for i in range(3, len(row)):
                print("{} owes {} to {}".format(row[i], share, row[0]))

    print("report done")