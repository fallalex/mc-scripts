#!/usr/bin/python3
from mcstatus import MinecraftServer
import  psutil
 
mc = MinecraftServer('localhost',25565)

mc.ping()

def find_proc(user, name, search):
    ps = []
    for p in psutil.process_iter(["username","name","cmdline","pid"]):
        if user == p.info['username']:
            if name == p.info['name']:
                if search in p.info['cmdline']:
                    ps.append(p.info['pid'])
    if len(ps) == 0:
        return None
    elif len(ps) == 1:
        return ps[0]
    # to define custom Exception need class
    raise Exception('More than one server process found PIDs: {}'.format(str(ps)))

print(find_proc("mc", "java", "server.jar"))

"""
Can only be in these states:
  - down
    - no pid
  - up
    - mcstatus
  - starting (wait)
  - stuck/error
    - no mcstatus
    - timeout
    - expected tmux window not found
"""
