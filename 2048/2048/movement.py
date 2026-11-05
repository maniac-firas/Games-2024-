from functions import merge, reverse, transpose
places = dict()
error = False
ms = 4

def printrows(matr):
     global error
     if error: print("Option not correct")

     larg = matr[0][0]     
     for r in matr:
          temp = max(r)
          if temp > larg:     larg = temp
     mS = len(str(larg))

     for r in matr:
          space =  '   '*mS+'   '
          if larg in r and mS>1:               
               for c in r:
                    print(c, space, end = '')
          else:
               for c in r:
                    print(c, space, end = ' ')
          print('\n')
     
     error = False

def err():
     global error
     error = True
     return True
              
#-----------------------------------------------------------Key Functions-----------------------------------------------------------------------
"""----------------------------------------------------------------------------------------------------------------------------------------------"""
def left(matr):
     for i in range(ms):
          matr[i] = merge(matr[i])

"""----------------------------------------------------------------------------------------------------------------------------------------------"""

def right(matr):
     for i in range(ms):
          matr[i] = reverse(matr[i])
          matr[i] = merge(matr[i])
          matr[i] = reverse(matr[i])

"""----------------------------------------------------------------------------------------------------------------------------------------------"""

def up(matr):
     transpose(matr)
     for i in range(ms):
          matr[i] = merge(matr[i])
     transpose(matr)

"""----------------------------------------------------------------------------------------------------------------------------------------------"""

def down(matr):
     transpose(matr)
     for i in range(ms):
          matr[i] = reverse(matr[i])
          matr[i] = merge(matr[i])
          matr[i] = reverse(matr[i])
     transpose(matr)
          
               
          
