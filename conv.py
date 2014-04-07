import sys, string, os, array, time, subprocess

from converter import Converter
from time import sleep

print "This program runs with the following arguments:", sys.argv

colours={"green":"\033[1;32m","greenx":"\033[1;m"}
n_args = len(sys.argv)

if n_args>3:
	print "to many args" 
	exit(0) 

for i in range(n_args):
	print i
	print "Input file: ",sys.argv[i]

path1 = sys.argv[1]
path2 = sys.argv[2]

c = Converter()

conv = c.convert(path1,path2,{'format':'mp4','audio':{'codec':'copy'},'video':{'codec':'divx','bitrate':5000}})#,'width':1024,'height':576}})

#os.system("ffmpeg -i "+path1+" -r 25 "+path2)

i = 0
for timecode in conv:
	i=i+1
	sys.stdout.write("\r%d%% Working" %timecode) 
	sys.stdout.write("\t Mechine time: " + str(i))
	sys.stdout.flush()
	pass

i = 0
print colours['green'],"\n Your file is ready! AND SAVED AT:",path2,colours['greenx']

exit(0)
