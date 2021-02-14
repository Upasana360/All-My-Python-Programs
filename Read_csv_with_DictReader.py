from csv import DictReader
with open("files.csv",'r')as f:
    csv_reader=DictReader(f)
    #iterator
    #next(csv_reader)
    for row in csv_reader:
        print(row['name'])
        print(row['phone'])
        