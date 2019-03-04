#! /usr/bin/env python

'''
    Receive list of Biggest Loser participants along with their start and finish weights.
    Sort list based on % weight lost and display results.
'''

import sys
import commands
from pprint import pprint
import re
from datetime import datetime

print '\n\nPlease enter list of Biggest Loser participants.  Enter "xxx" for name if finished.'
people = ()

num_people = 0
while True:
    name = raw_input("Participant name: ").strip()
    if name == 'xxx':
        break
    start_weight = int(raw_input("Starting weight: ").strip())
    end_weight = int(raw_input("Ending weight: ").strip())
    num_people += 1
    people += ([name, start_weight, end_weight],)

print(people)
shit


status, rtp_emps = commands.getstatusoutput(command)
emp_list = rtp_emps.splitlines()
total_number_of_employees = len(emp_list)

print 'Building dictionary from list...'

emp_dict = {}
for entry in emp_list:
    # Use regexp to extract userid and employee id from each entry in the list:
    mo = re.search(r'(\w+)\s+\w*\s+(\d+)', entry)
    if mo is not None:
        userid = mo.group(1)
        employee_num = int(mo.group(2))
        emp_dict[employee_num] = userid
    else:
        print 'Trouble parsing this entry: %s' % entry

print 'There are %s total employees in RTP that show up in directory.' % total_number_of_employees
print 'Sorting...'
sorted_keys = sorted(emp_dict)

print 'Scanning...'
rank = 1
found = False
print 'Rank  Email      Employee ID#'
for key in sorted_keys:
    print '%4d  %-10s  %5s' % (rank, emp_dict[key], key)
    if emp_dict[key] == employee:
        print '\nEmployee with userid %s has badge id# %s which is ranked #%s in RTP.' % (emp_dict[key], key, rank)
        found = True
        break
    rank += 1

if not found:
    print 'I did not find employee with userid %s.' % employee

elapsed_time = datetime.now() - start_time
print 'Elapsed runtime: ', elapsed_time, '\n\n'




