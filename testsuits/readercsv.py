# coding=utf-8

# import csv as CSV
# with open('D:\portal3.csv','rb') as csvfile:
#     # reader = CSV.reader(csvfile)
#     # for row in reader:
#     #     print row
#     reader = CSV.DictReader(csvfile)
#     rows = [row for row in reader]
#     print rows
# csvfile.close()


import csv
for d in csv.DictReader(open('D:\portal01.csv','rb')):
    print d