import csv

def save(data):
    with open('Data.csv','a') as f:
        writer=csv.writer(f)           #збереження данних в таблицю

        writer.writerow((
            data['date'],
            data['id'],
            data['url'],

        ))
    print('saved')

