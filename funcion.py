def multi(*args):
    return ([i/2 for i in args])
  
def funcion(fn):
    def wrapper(*args):
        for i, arg in enumerate(*args):
             print "arg: %d%d" % (i, args)
        return fn(*args)
    return wrapper


