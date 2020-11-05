import csv
with open('pc_inventory.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('pc_inventory_1.csv', 'w') as new_file:
        write_csv = csv.writer(new_file, delimiter=' ', quotechar="'")

        for line in csv_reader:
            write_csv.writerow(line)
