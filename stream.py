import os, sys
from os.path import basename

path1 = sys.argv[1]
times = int(sys.argv[2])
base = basename(path1)

for i in range(times):
	os.system("ffmpeg2theora -v 10 -a 6 -x 512 -y 238 "+path1+" -o -| oggfwd localhost 8000 emilio /"+base)
	i=i+1

exit(0)
