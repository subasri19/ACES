def search(x,key) :
    for i in range(len(x)) :
        if(x[i] == key) :
            return i
    return 1 
     
#print('Enter the number of elements in the list : ')
num = int(input())

l = []

#print('Enter elements in the list :')
for i in range(num) :
    a = int(input())
    l.append(a)
    i+=1

#print('Enter the element to be searched : ')
key = int(input())

v = search(l,key)

if(v!=1) :
    print('\nThe element to be searched ',key,' is found in position ',v+1)
else :
    print('\nOops! Sorry, the element you looked for is not found in the list :(',key)
    
    
#print('\nPress any key to exit\n')
    
