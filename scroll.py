#!/bin/python

import time
import sys

f = sys.argv[1]

time.sleep(0.1)
with open(f) as fp:
	for line in fp:
		print line[:-1]
		time.sleep(0.01)
