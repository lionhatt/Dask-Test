import csv
import random
from time import time
from faker import Faker

RECORD_COUNT = 400000000
fake = Faker()



def create_csv_file():
    with open('./files/test.csv', 'w', newline='') as csvfile:
        fieldnames = ['user_id', 'isAuthenticated', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'user_id': fake.random_int(min=1, max=100000),
                    'isAuthenticated': fake.boolean(chance_of_getting_true=50),
                    'time': fake.date_time_this_decade(),
                }
            )

if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))





