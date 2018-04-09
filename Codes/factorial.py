num = int (input())
fact = 1
if num==0:
    fact = 1
else:
    for i in range (1,num+1):
        fact = fact*i
print("The factorial of the entered number ",num," is ",fact)
#print("Press any key to exit")
    
