import csv


table =[
    ['Tag Name','Address','Data Type','Respect Data Type','Client Access','Scan Rate'],
    ['Tag1','RANDOM','LONG',1,'RO',100],
    ['Tag2', 'RANDOM', 'LONG', 1, 'RO', 500],
    ['Tag3', 'RANDOM', 'LONG', 1, 'RO', 100],
    ['Tag4', 'RANDOM', 'LONG', 1, 'RO', 500],
    ['Tag5', 'RANDOM', 'LONG', 1, 'RO', 100],
    ['Tag6', 'RANDOM', 'LONG', 1, 'RO', 500]
]

def readCSV(csv_name):
    with open(csv_name+'.csv', newline='',encoding='utf-8') as csvfile:
        csv_row = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csv_row:
            print(', '.join(row))

def writeCSV(csv_name):
    with open('device1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(table)

#writeCSV('device1')
readCSV('demo_0906')
