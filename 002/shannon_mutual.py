'''
shannon_mutual.py

Takes the average shannon mutual information over all replicates to determine if it is increasing over time.

'''

import gzip
import matplotlib.pyplot as plt

sums = [0.0]*2010

for seed in range(1, 31):
    workingFile = gzip.open('002_math_'+str(seed)+'/data/deme_rx_repl.dat', 'rb')
    for line in workingFile:
        if not line[0] == '#' and not line[0] == '\n':
            value = float(line[3])
            update = int(line[0])/100
            sums[update] += value

averages = []
for update in range(0,2011):
    averages.append(sums[update]/30.0)

fig = plt.figure()
plt.plot(averages)
plt.savefig('averages')
