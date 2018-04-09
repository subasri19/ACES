import subprocess
import filecmp
f1 = open('ip_names.txt','r')
f2 = open('op_check.txt','r')
f3 = open('file_names.txt','r')
f4 = open('Status.txt','w')
l1 = f1.readlines()
l2 = f2.readlines()
l3 = f3.readlines()

for i in range(0,len(l3)):
    myinput = open('Codes\Check_ip\\' + str(l1[i]).rstrip('\n'),'r')
    s = 'Codes\Check_op\output' + str(i+1) + '.txt'
    myoutput = open( s ,'w')
    p = subprocess.Popen(str(l3[i]).rstrip('\n'), stdin = myinput, stdout = myoutput, shell = True)
    p.wait()
    myoutput.flush()
    t = filecmp.cmp('Codes\Verify\\' + str(l2[i]).rstrip('\n') , s)
    if t == True :
        f4.write(str(l3[i]).rstrip('\n') + ' - Successful\n')
    else :
        f4.write(str(l3[i]).rstrip('\n') + ' - Failed\n')


    
