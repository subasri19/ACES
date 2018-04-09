def read(r,c,a) :
    for i in range(0,r) :
        a.append([])
        for j in range(0,c) :
            s = int(input())
            a[i].insert(j,s)
            j+=1
        i+=1

def add(a,b) :
    Sum = []
    for i in range(len(a)) :
        row = []
        for j in range (len(a[0])) :
            row.append(a[i][j]+b[i][j])
        Sum.append(row)
    return Sum
      
x = []
y = []
res = []

#print('Enter the number of rows and column in the matrix 1 : ')
r1 = int(input())
c1 = int(input())
#print('Enter the elements in the matrix 1 ')
read(r1,c1,x)

#print('Enter the number of rows and column in the matrix 2 : ')
r2 = int(input())
c2 = int(input())
#print('Enter the elements in matrix 2 ')
read(r2,c2,y)

#print('\nThe matrix 1 is : ')
print(x)

#print('\nThe matrix 2 is : ')
print(y)

if(r1 == r2 and  c1 == r2) :
    res = add(x,y)
    print('\nThe sum of the two matrices are :')
    print(res)

else :
    print('\nAddition of these matrices are not possible as their orders are different')

#print('Press any key to exit')
    
