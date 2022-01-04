### Why
Kubernetes can run thousands of find/du/ip short-live processes(mostly exec.command liveness probes) on kubernetes node.  
These processes are visible in atop, but cmdline is not available as procfs records are gone soon.

### Usage

- findexit.py -- display cmdline of all finished processes
- findit.py   -- display cmdline by regexp

procfs polled with 100ms interval


### Notes
#### Pure bash alternative
in some cases the following will be enough

```bash
sudo tail  /proc/*/cmdline | tr '\0' ' ' | grep -C 5 -F 'ip '
```

