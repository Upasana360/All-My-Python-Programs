from csv import writer
with open("files.csv",'a',newline="")as f:
    csv_writer=writer(f)
    #mtds-writerow,writerows
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['mohit','India'])
    csv_writer.writerow(['Maggie','USA'])
    csv_writer.writerows([['name','country'],['mohit','India'],['Upsana','Bhutan']])

        