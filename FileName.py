import glob
names=glob.glob("Codes\*.py")
file = open('file_names.txt' , 'w+')
for i in range(0 , len(names)):
    s = str(names[i]).replace("Codes\\" , "")
    file.write(s)
    file.write('\n')
