#!/usr/bin/python3
from mcstatus import MinecraftServer
import  psutil
from time import time
import libtmux

class mcStatus:
    def __init__(self):
        self.mc = MinecraftServer('localhost',25565)
        self.username = "mc"
        self.process_name = "java"
        self.cmd_query = "server.jar"
        self.stime = None

    def ping(self):
        try:
            self.mc.ping()
            return True
        except:
            return False

    def find_proc(self):
        ps = []
        for p in psutil.process_iter(["username","name","cmdline","pid","create_time"]):
            if self.username == p.info['username']:
                if self.process_name == p.info['name']:
                    if self.cmd_query in p.info['cmdline']:
                        ps.append((p.info['pid'], p.info['create_time']))
        if len(ps) == 0: return None
        elif len(ps) == 1:
            self.stime = int(time() - ps[0][1])
            return ps[0][0]
        # to define custom Exception need class
        raise Exception('More than one server process found PIDs: {}'.format(str(ps)))

    def tmux(self):


    
def main():
    mc = mcStatus()
    pid = mc.find_proc()
    mc.tmux()
    if pid == None:
        return 1
    if mc.ping():
        print(mc.stime)
        return 0
    return 2

if __name__ == "__main__":
    main()

"""
Can only be in these states:
  - down
    - no pid
  - up
    - mcstatus
  - starting (wait)
    - pid but mcstatus does not return
  - stuck/error
    - no mcstatus
    - timeout
    - expected tmux window not found
"""
  
"""
status
0 up 
1 down

2 starting

check for pid
if not pid:
    return 1
try mcstatus
    return 0
except
    return 2
"""
