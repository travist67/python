#! /usr/bin/env python

import sys

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

tot_apples=0
tot_oranges=0

for x in range(m):
    if apple[x]+a>=s and apple[x]+a<=t:
        tot_apples+=1
for x in range(n):
    if oranges[x]+d>=s and oranges[x]+d<=t:
        tot_oranges+=1
print(tot_apples)
print(tot_oranges)

