#!/usr/bin/env python
# memusage
# BitBar plugin
#
# by Gautam krishna R
#
# Shows the current system memmory usage
# Use memusage.py python script to fetch data
import subprocess
import re

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
vm = subprocess.Popen(['memory_pressure'], stdout=subprocess.PIPE).communicate()[0]

# Iterate processes
processLines = ps.split('\n')
sep = re.compile('[\s]+')
rssTotal = 0 # kB
for row in range(1,len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0 # ignore...
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
sep = re.compile(':[\s]+')
vmStats = {}
for row in range(1,len(vmLines)-1):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    if not (len(rowElements) < 2):
        if rowElements[0] == "System-wide memory free percentage":
            vmStats[(rowElements[0])] = int(rowElements[1].strip('\.%'))
        else:
            vmStats[(rowElements[0])] = int(rowElements[1].strip('\.%')) * 4096

print "Memory: %d%%" % ( 100 - vmStats["System-wide memory free percentage"])
print '---'
print 'Wired Memory: %d MB' % ( vmStats["Pages wired down"]/1024/1024 )
print 'Active Memory: %d MB' % ( vmStats["Pages active"]/1024/1024 )
print 'Inactive Memory: %d MB' % ( vmStats["Pages inactive"]/1024/1024 )
print 'Free Memory: %d MB' % ( vmStats["Pages free"]/1024/1024 )
print 'Real Mem Total (ps): %.3f MB' % ( rssTotal/1024/1024 )
