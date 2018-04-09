import glob
names=glob.glob("Codes\Check_ip\*.txt")
file = open('ip_names.txt' , 'w+')
for i in range(0 , len(names)):
    s = str(names[i]).replace("Codes\Check_ip\\" , "")
    file.write(s)
    file.write('\n')
