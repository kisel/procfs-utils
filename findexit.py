#!/usr/bin/env python3
import os
import re
import time

isnum=re.compile("^\d+$")
pidcache = {}

def go():
   pids = [p for p in os.listdir("/proc") if isnum.match(p)]
   for pid in pids:
       try:
           f = open(f"/proc/{pid}/cmdline", "rb")
           cmdline = f.read().replace(b'\0', b' ').decode()
           pidcache[pid] = cmdline
       except:
           # ignore file not found and permission errors
           #print(e)
           pass

   pids = list(pidcache.keys())
   for pid in pids:
       if not os.path.exists(f"/proc/{pid}/cmdline"):
           cmdline = pidcache[pid]
           del pidcache[pid]
           print(f"process exit: {pid}: {cmdline}")

def main():
    while True:
        go()
        time.sleep(0.1)

main()

