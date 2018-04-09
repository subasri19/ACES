def sort(x) :
    for i in range(0,num) :
        for j in range(0,num-i-1) :
            if x[j]>x[j+1] :
                swap(x[j],x[j+1])

def swap(a,b) :
    t = a
    a = b
    b = t
    
x = []

#print('Enter the number of elements in the list : ')
num = int(input())
#print("Enter the sequence")
for i in range(num) :
    s = int(input())
    x.insert(i,s)

sort(x)
           
print("\nSorted sequence\n")
print(x)
input('Press any key to exit')

    
    
               

