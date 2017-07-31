from csv import writer
from datetime import datetime

time = datetime.now().strftime("%Y%m%d-%H%M%S")
filename = '/Users/ben/code/finance/fx_15_min/data/helloo' + time + '.csv'

test_dict = {'hello': 'world'}

with open(filename, 'w+') as csv_file:
    csv_writer = writer(csv_file)
    for key, value in test_dict.items():
        csv_writer.writerow([key, value])
