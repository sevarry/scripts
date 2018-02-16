#!/usr/bin/env python

#created by Ted Eckerman, 2018

from collections import Counter

log = 'log.txt'
fails = []

with open(log) as f:
    for line in f:
        if 'failed login' in line:
            name = line.partition(' ')[0]
            fails.append(name)

cnt = Counter(fails)
inc = [k for k, v in cnt.iteritems() if v >= 3]

print
print 'The following users have failed login 3 or more times:'
for i in inc:
    print
    print 'username: ', i
print
