### Why
kubernetes can run thousands of find/du/ip processes on kubernetes cluster
these processes are visible in atop, but cmdline is not available


### Usage

findexit.py -- display cmdline of all finished processes
findit.py   -- display cmdline by regexp

procfs polled with 100ms interval


### Notes
#### Pure bash alternative
in some cases the following will be enough

```bash
sudo tail  /proc/*/cmdline | tr '\0' ' ' | grep -C 5 -F 'ip '
```

