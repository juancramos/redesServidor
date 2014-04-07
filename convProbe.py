import sys, string, os, array

from converter import Converter

colours={"green":"\033[1;32m","greenx":"\033[1;m"}

print "This program runs with the following arguments:", sys.argv

n_args = len(sys.argv)

if n_args>2:
	print "to many args" 
	exit() 

path1 = sys.argv[1]

print colours['green'],"Nombre del archivo:\n",path1,"\n"

c = Converter()

info = c.probe(path1)

print "Video format:\n",info.format.format
print "Video duration:\n",info.format.duration
print "Video size:\n",len(info.streams)
print "Video codec:\n",info.video.codec
print "Video width:\n",info.video.video_width
print "Video height:\n",info.video.video_height
print "Video audio codec:\n",info.audio.codec
print "Video audio chennels:\n",info.audio.audio_channels,colours['greenx']

sys.exit()
