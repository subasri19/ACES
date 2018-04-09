import glob
names=glob.glob("Codes\Verify\*.txt")
file = open('op_check.txt' , 'w+')
for i in range(0 , len(names)):
    s = str(names[i]).replace("Codes\Verify\\" , "")
    file.write(s)
    file.write('\n')
