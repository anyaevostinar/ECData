'''
msg_analyzer.py

A script to analyze inputs and outputs of avidians sending messages, to determine if they are engaging in problem decomposition.

Anya Johnson and Jason Lefler
10/01/12
'''

import gzip

inputs = [bin(int('0f13149f',16))[2:].zfill(32), bin(int('3308e53e',16))[2:].zfill(32), bin(int('556241eb', 16))[2:].zfill(32)]
pos_solutions = []

#Not
def ourNot(notinputs):
    not_solutions = []
    for num in notinputs:
        sol = ''
        for i in num:
            if i == '0':
                sol+='1'
            else:
                sol+='0'
        not_solutions.append(sol)

pos_solutions = ourNot(inputs)
#Nand
#anya


#And
#jason

#Or Not
#anya

#Or
#jason

#And Not
#anya

#Not Or
#jason

#Exclusive Or
#anya

#Equals
#jason - bitwise equal for each position, 1 if the positions match, 0 if not

folders = []

for folder in folders:
    for seed in range(1, 31):
        workingFile = gzip.open(folder+str(seed)+'/message_log.dat', 'rb')
        for line in workingFile:
            if not line[0] == '#' and not line[0] == '\n':
                solution = bin(int(line.split()[5]))[2:].zfill(32)
