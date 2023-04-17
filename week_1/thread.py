import threading
import os

def foo():
    print('This is foo', threading.get_native_id())
 
def bar():
    print('This is bar', threading.get_native_id())
 
def baz():
    print('This is baz', threading.get_native_id())


if __name__ == '__main__':
    thread = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()