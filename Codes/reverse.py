rev = 0
#print('Enter the number for which the reverse has to be found : ')
num = int(input())
temp1 = num

while num>0 :
    temp = num % 10
    rev = rev*10 + temp
    num //= 10

print('\nThe reverse of the number ',temp1,' is ',rev)
#print('\nPress any key to exit\n')
