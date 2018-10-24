import os
pid = os.fork()

if pid == 0:
    print('我是进程1')
else:
    print('我是进程2')
