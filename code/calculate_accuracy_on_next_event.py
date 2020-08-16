'''
this script takes as input the output of evaluate_suffix_and_remaining_time.py
therefore, the latter needs to be executed first

Author: Niek Tax
'''

from __future__ import division
import csv
from pathlib import Path

eventlog = "helpdesk.csv"
csvfile = open(str((Path.cwd()/'code'/'output_files'/'results'/'suffix_and_remaining_time_''{}'.format(eventlog)).resolve()), 'r')
r = csv.reader(csvfile, delimiter=',', quotechar='|')
next(r, None)  # skip the headers

#Checks if the next event in a sequence is correct
vals = dict()
for row in r:
    l = list()
    print(row)
    if row[0] in vals.keys():
        l = vals.get(row[0])
    if len(row[2])==0 and len(row[3])==0:
        l.append(1)
    elif len(row[2])==0 and len(row[3])>0:
        l.append(0)
    elif len(row[2])>0 and len(row[3])==0:
        l.append(0)
    else:
        l.append(int(row[2][0]==row[3][0]))
        print(row[2][0])
        print(row[3][0])
    vals[row[0]] = l
    #print(vals)

#Averages the score of the last loop
l2 = list()
for k in vals.keys():
    print('{}: {}'.format(k, vals[k]))
    l2.extend(vals[k])
    res = sum(vals[k])/len(vals[k])
    print('{}: {}'.format(k, res))

print('total: {}'.format(sum(l2)/len(l2)))

#Lacks the remaining time evaluation
