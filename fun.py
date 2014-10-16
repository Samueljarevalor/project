rgs):
  2     return ([i/2 for i in args])
  3  
  4 def decorador(fn):
  5     def nuevo(*args):
  6         for i, arg in enumee(*args):
  7             print "arg: %d%d" % (i, args)
  8         return fn(*args)
  9     return nuevo

