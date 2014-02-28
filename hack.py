#!/bin/python

import os
import time
import sys
import subprocess
from random import randint

path = os.path.dirname(os.path.realpath(__file__))
w_ids = list() 

def get_window_id():
	p = subprocess.Popen(["xdotool", "getactivewindow"])
	out,err = p.communicate()
	if out:
		return int(out)
	return 0

def open_window(x, y, f):
	os.system("gnome-terminal -x %s/scroll.py %s"%(path,f))
	wid = get_window_id()
	w_ids.append(wid)
	os.system("xdotool getactivewindow windowmove --sync %i %i"%(x,y))

def get_file_list():
	global path
	if len(sys.argv) == 1:
		dir = path
	else:
		dir = sys.argv[1]
	files = os.listdir(dir)
	for i,item in enumerate(files):
		files[i] = dir + item
	return files

for f in get_file_list():
	open_window(randint(0, 1280), randint(0,800), f)
