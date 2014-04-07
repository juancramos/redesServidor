import sys, subprocess, os

print "this action will run in background with the next argument:\n"

times = len(sys.argv)

for i in range(times):
	print sys.argv[i], "\n"

j=1
while j<times:
	path1 = sys.argv[j]
	path2 = sys.argv[j+1]
	p=subprocess.Popen([sys.executable,'conv.py', path1, path2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print "file saved at:", path2 
	j = j+2

sys.exit()
