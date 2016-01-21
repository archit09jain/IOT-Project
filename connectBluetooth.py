# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:12:53 2016

@author: archit08jain
"""

import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))