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
        return not_solutions


#Nand - if both inputs are 1 the output is 0, else the output is 1

def ourNand(nandinput1, nandinput2):

    nand_solution = []
    sol = ''
    for i in range(0, len(nandinput1)):
        if nandinput1[i] == '1' and nandinput2[i] == '1':
            sol += '0'
        else:
            sol += '1'
    nand_solution.append(sol)
    return nand_solution


#And

def ourAnd(andinput1, andinput2):

    and_solution = []
    sol = ''
    for i in range(0, len(andinput1)):
        if andinput1[i] == '1' and andinput2[i] == '1':
            sol += '1'
        else:
            sol += '0'
    and_solution.append(sol)
    return and_solution

#Or Not - an OR then a NOT

def ourOrNot(ornotinput1, ornotinput2):
    ornot_solution = []
    sol = ''
    for i in range(0, len(ornotinput1)):
        if ornotinput1[i] == '1' or ornotinput2[i] == '1':
            sol += '0'
        else:
            sol += '1'
    ornot_solution.append(sol)
    return ornot_solution

#Or

def ourOr(orinput1, orinput2):

    or_solution = []
    sol = ''
    for i in range(0, len(orinput1)):
        if orinput1[i] == '1' or orinput2[i] == '1':
            sol += '1'
        else:
            sol += '0'
    or_solution.append(sol)
    return or_solution

#And Not

def ourAndNot(andnotinput1, andnotinput2):

    andnot_solution = []
    sol = ''
    for i in range(0, len(andnotinput1)):
        if andnotinput1[i] == '1' and andnotinput2[i] == '1':
            sol += '0'
        else:
            sol += '1'
    andnot_solution.append(sol)
    return andnot_solution

#Not Or - a NOT then an OR

def ourNotOr(notorinput1, notorinput2):

    notor_solution = []
    sol = ''
    for i in range(0, len(notorinput1)):
        if notorinput1[i] == '0' or notorinput2[i] == '0':
            sol += '1'
        else:
            sol += '0'
    notor_solution.append(sol)
    return notor_solution

#Exclusive Or - if the inputs don't match the output is 1

def ourXor(xorinput1, xorinput2):

    xor_solution = []
    sol = ''
    for i in range(0, len(xorinput1)):
        if xorinput1[i] == xorinput2[i]:
            sol += '0'
        else:
            sol += '1'
    xor_solution.append(sol)
    return xor_solution

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



folders = []

for folder in folders:
    for seed in range(1, 31):
        workingFile = gzip.open(folder+str(seed)+'/message_log.dat', 'rb')
        for line in workingFile:
            if not line[0] == '#' and not line[0] == '\n':
                solution = bin(int(line.split()[5]))[2:].zfill(32)
