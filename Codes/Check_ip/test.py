import subprocess
myinput = open('fact_ip.txt')
myoutput = open('fact_op.txt', 'w')
my = open('rev_ip.txt')
myo = open('rev_op.txt','w')
p = subprocess.Popen('factorial.py', stdin=myinput, stdout=myoutput, shell = True)
q = subprocess.Popen('reverse.py', stdin=my, stdout=myo, shell = True)
p.wait()
q.wait()
myoutput.flush()
myo.flush()
