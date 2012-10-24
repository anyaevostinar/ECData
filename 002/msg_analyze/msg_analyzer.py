'''
msg_analyzer.py

A script to analyze inputs and outputs of avidians sending messages, to determine if they are engaging in problem decomposition.

Anya Johnson and Jason Lefler
10/01/12
'''

import gzip
import sys

inputs = [int('0f13149f',16), int('3308e53e',16), int('556241eb',16)]
pos_solutions = []

# A + B
def arith1(input1, input2):
    solutions= [bin(input1+input2)[2:].zfill(32)]
    return solutions

# A - B
def arith2(input1, input2):
    solutions= [bin(input1-input2)[2:].zfill(32)]
    return solutions

# A + A
def arith3(input1, input2):
    solutions= [bin(input1+input1)[2:].zfill(32)]
    return solutions

# 3A - B
def arith4(input1, input2):
    solutions= [bin(3*input1-input2)[2:].zfill(32)]
    return solutions

# 4A
def arith5(input1, input2):
    solutions= [bin(4*input1)[2:].zfill(32)]
    return solutions

# 2A + 3B
def arith6(input1, input2):
    solutions= [bin(2*input1+3*input2)[2:].zfill(32)]
    return solutions

# - A - B - C

def arith7(input1, input2, input3)
    solutions= [bin(-input1-input2-input3)[2:].zfill(32)]
    return solutions

# A + B + C

def arith8(input1, input2, input3)
    solutions= [bin(input1+input2+input3)[2:].zfill(32)]
    return solutions

# 5A - 2B + C

def arith9(input1, input2, input3)
    solutions= [bin(5*input1-2*input2+input3)[2:].zfill(32)]
    return solutions


#Equals - bitwise equal for each position, 1 if the positions match, 0 if not

def ourEquals(eqinput1, eqinput2):

    eq_solution = []
    sol = ''
    for i in range(0,len(eqinput1)):
        if eqinput1[i] == eqinput2[i]:
            sol += '1'
        else:
            sol += '0'
    eq_solution.append(sol)
    return eq_solution

functions = [ourNand, ourAnd, ourOrNot, ourNotOr, ourXor, ourOr, ourEquals, ourAndNot]

#Make solution list from inputs                                                                                                   
for value in inputs:
    pos_solutions.append(ourNot(value))

#Input 1 and 2                                                                                                                    
for function in functions:
    pos_solutions+=function(inputs[0], inputs[1])

#Input 1 and 3                                                                                                                    
for function in functions:
    pos_solutions+=function(inputs[0], inputs[2])

#Input 2 and 3                                                                                                                    
for function in functions:
    pos_solutions+=function(inputs[1], inputs[2])


'''
seed = int(sys.argv[1])
folder = sys.argv[2]

workingFile = gzip.open('/mnt/home/anyaejo/EC/ECData/001/'+folder+str(seed)+'/data/message_log.dat.gz', 'rb')
num_messages = 0
num_correct = 0
for line in workingFile:
    if not line[0] == '#' and not line[0] == '\n':
        solution = bin(int(line.split()[5]))[2:].zfill(32)
        num_messages+=1
        for sol in pos_solutions:
            if solution == sol:
                num_correct+=1
                break
workingFile.close()
if num_messages != 0:
    percent_correct = float(num_correct)/float(num_messages)
else:
    percent_correct = 0.0
outputFile = open(folder+str(seed)+'_analyzed.dat','w')
outputFile.write('num_correct, num_messages, percent_correct \n' + str(num_correct) + ' ' + str(num_messages) + ' ' + str(percent_correct))
outputFile.close()

'''
