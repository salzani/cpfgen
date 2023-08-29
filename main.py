import random

firstninedig = ''

for index in range(9):
    firstninedig += str(random.randint(0, 9))


invert = 10
result = 0

for number in firstninedig:
    result+=int(number)*invert
    invert -= 1

rest = result*10%11
if rest == 10:
    rest = 0


teendig = firstninedig + str(rest)

invertwo = 11
resultwo = 0

for numbertwo in teendig:
    resultwo += int(numbertwo)
    invertwo -= 1

finalresult = resultwo*10%11
if finalresult == 10:
    finalresult = 0

if finalresult >= 9:
    finalresult = 0
else:
    finalresult = resultwo*10%11


#REBUILDING THE CPF
cpfgen = f'{firstninedig}{rest}{finalresult}'

print(F'CPF: {cpfgen}')


#VALIDATE


CPF = cpfgen

#sorting out the first nine numbers on a variable
first =CPF[:9]

#creating a var with invert numbers and a variable(RESULT) with the value 0
invert2 = 10
result2 = 0

for number2 in first:
    result2+=int(number2)*invert2
    invert2 -= 1

ver1 = result2*10%11
if ver1 >= 10:
    ver1 = 0
else:
    ver1
    
print(f'first digit: {ver1}')

###############

#sorting out the first teen numbers on a variable
second = CPF[:10]

#creating a var with invert numbers and a variable(RESULT) with the value 0
invertwo2 = 11
resultwo2 = 0

for numbertwo2 in second:
    resultwo2 += int(numbertwo2)
    invertwo2 -= 1

ver2 = resultwo2*10%11
if ver2 >= 10:
    ver2 = 0
else: 
    ver2


print(f'second digit: {ver2}')


#REBUILDING THE CPF
cpfgen = f'{first}{ver1}{ver2}'

print(F'CPF: {cpfgen}')


#VALIDATING THE CPF
if CPF == cpfgen:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')
