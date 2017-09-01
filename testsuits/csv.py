# coding=utf-8

import csv
with open('D:\portal.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

