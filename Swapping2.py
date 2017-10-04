#Swapping of two no.s(without using third variable)

a=int(input('Enter 1st no:'))
b=int(input('Enter 2nd no:'))
print('1st no:',a)
print('2nd no:',b)
a=a+b
b=a-b
a=a-b
print('After swapping')
print('1st no:',a)
print('2nd no:',b)
