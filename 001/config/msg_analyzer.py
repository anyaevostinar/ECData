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

#pos_solutions = ourNot(inputs)

#Nand
#anya


#And

def ourAnd(andinput1, andinput2):
    #print "\nourAnd - input 1  -  ", andinput1
    #print "ourAnd - input 2  -  ", andinput2
    and_solution = []
    sol = ''
    for i in range(0, len(andinput1)):
        if andinput1[i] == '1' and andinput2[i] == '1':
            sol += '1'
        else:
            sol += '0'
    and_solution.append(sol)
    #print "ourAnd - solution -", and_solution
#pos_solutions = ourAnd(inputs[1], inputs[2])

#Or Not - an or then a not

def ourOrNot(ornotinput1, ornotinput2):
    #print "\nourOrNot - input 1     -  ", ornotinput1
    #print "ourOrNot - input 2     -  ", ornotinput2
    ornot_solution = []
    sol = ''
    for i in range(0, len(ornotinput1)):
        if ornotinput1[i] == '1' or ornotinput2[i] == '1':
            sol += '0'
        else:
            sol += '1'
    ornot_solution.append(sol)
    #print "ourOrNot - solution    -", ornot_solution

#pos_solutions = ourOrNot(inputs[1], inputs[2])

#Or

def ourOr(orinput1, orinput2):
    #print "\nourOr - input 1     -  ", orinput1
    #print "ourOr - input 2     -  ", orinput2
    or_solution = []
    sol = ''
    for i in range(0, len(orinput1)):
        if orinput1[i] == '1' or orinput2[i] == '1':
            sol += '1'
        else:
            sol += '0'
    or_solution.append(sol)
    #print "ourOr - solution    -", or_solution
#pos_solutions = ourOr(inputs[1], inputs[2])

#And Not
#anya

#Not Or - a not then an or

def ourNotOr(notorinput1, notorinput2):
    #print "\nourNotOr - input 1     -  ", notorinput1
    #print "ourNotOr - input 2     -  ", notorinput2
    notor_solution = []
    sol = ''
    for i in range(0, len(notorinput1)):
        if notorinput1[i] == '0' or notorinput2[i] == '0':
            sol += '1'
        else:
            sol += '0'
    notor_solution.append(sol)
    #print "ourNotOr - solution    -", notor_solution

#pos_solutions = ourNotOr(inputs[1], inputs[2])

#Exclusive Or
#anya

#Equals - bitwise equal for each position, 1 if the positions match, 0 if not

def ourEquals(eqinput1, eqinput2):
    #print "\nourEquals - input 1  -  ", eqinput1
    #print "ourEquals - input 2  -  ", eqinput2
    eq_solution = []
    sol = ''
    for i in range(0,len(eqinput1)):
        if eqinput1[i] == eqinput2[i]:
            sol += '1'
        else:
            sol += '0'
    eq_solution.append(sol)
    #print "ourEquals - solution -", eq_solution
#pos_solutions = ourEquals(inputs[1], inputs[2])

folders = []

for folder in folders:
    for seed in range(1, 31):
        workingFile = gzip.open(folder+str(seed)+'/message_log.dat', 'rb')
        for line in workingFile:
            if not line[0] == '#' and not line[0] == '\n':
                solution = bin(int(line.split()[5]))[2:].zfill(32)
