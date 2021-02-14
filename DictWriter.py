from csv import DictWriter
with open("files.csv",'a',newline="")as f:
    csv_writer=DictWriter(f,fieldnames=['name','country'])
    csv_writer.writeheader()
    #mtds-writerow,writerows
    csv_writer.writerow({'name':'mohit','country':'India'})
    csv_writer.writerow({'name':'Maggie','country':'USA'})
    #csv_writer.writerows([['name','country'],['mohit','India'],['Upsana','Bhutan']])