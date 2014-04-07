import sys, subprocess, os

print "The stream will run in background with the next argument:\n"

times = len(sys.argv)

for i in range(times):
	print sys.argv[i], "\n"

j=1
while j<times:
	path1 = sys.argv[j]	
	p=subprocess.Popen([sys.executable,'stream.py', path1,"10"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	j = j+1

exit(0)
