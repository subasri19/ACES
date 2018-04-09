import math

#print('Enter the values of a, b and c in the quadratic equation : ')
a = int(input())
b = int(input())
c = int(input())

d = math.sqrt(b*b - 4*a*c)
if d>=0 :
    print('\nThe roots of the equation are ',(-b-d)/(2*a),' and ',(-b+d)/(2*a))
else :
    print('\nThis equation has complex roots')

#print('\nPress any key to exit')
