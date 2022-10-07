from . import _version

name = 'utils-lib'

__VERSION__ = _version.get_version()

data = 'def'

if data == 'abc':
    while True:
        print ('Infinite loop')

def area(r):
    #if DEBUG:
    #   print("Computing area of %r" % r)
    return r.length * r.width
