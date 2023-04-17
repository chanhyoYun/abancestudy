import os
from multiprocessing import Process

# print('hello os')
# print('my pid is', os.getpid())


def foo():
    print('This is foo', os.getppid())

def bar():
    print('This is bar', os.getpid())

def baz():
    print('This is baz', os.getpid())
  
if __name__ == '__main__':
    child = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()

    print('parent process', os.getpid())