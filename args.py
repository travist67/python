#! /usr/bin/env python3

# demonstrating defining a function with arbitrary # of args 

def blah(*whuteva):   # arbitrary number of args 
   for z in whuteva:
      print("arg = "+ str(z))

################################
###    Start of script       ###
################################

answer=blah('abc',1,'def',2,3,4,5,'six',7)

# convention is to use *args for non-keyword-args and **kwargs for keyword-args.  

print('\n\n\nNEW STUFF:')
def test(normalarg, *args, **kwargs):
    print('normalarg = ' + str(normalarg))
    print('*args:')
    for x in args:
        print(x)
    print('**kwargs:')
    if kwargs is not None:
        for key, value in kwargs.items():
             print("%s = %s" % (key,value))

test(1,2,3,4,5,blah=99, abc=123)
print('===============')
test(8)
print('===============')
test("abc", "def", uu=44)

