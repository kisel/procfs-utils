#!/usr/bin/env python3
import os
import re
import time

isnum=re.compile("^\d+$")
# TODO: edit regexp or add argparse
#re_proc=re.compile("<du>.*|^ip.*")
re_proc = re.compie(".*\\bip\\b.*")

def go():
   pids = [p for p in os.listdir("/proc") if isnum.match(p)]
   matching = 0
   for pid in pids:
       try:
           f = open(f"/proc/{pid}/cmdline", "rb")
           cmdline = f.read().replace(b'\0', b' ').decode()
           if re_proc.match(cmdline):
               matching += 1
               print(f"{pid} -- {cmdline}")
       except:
           # ignore file not found and permission errors
           pass
   print(f"Matching processes found: {matching}")

def main():
    while True:
        go()
        time.sleep(0.1)

main()

