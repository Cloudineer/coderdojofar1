#!/usr/bin/env python3

import sys
from mpmath import mp

if len(sys.argv)>1:
    dp = int(sys.argv[1])
else:
    dp = 500

mp.dps = dp
print ("PI = {}".format(mp.quad(lambda x: mp.sqrt(1-(x**2)),[0,1]) *4))
