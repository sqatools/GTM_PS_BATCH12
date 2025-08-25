# *          *
#  *       *
#    *   *
#      *
#
for i in range (1,14):
    for j in range (1,11):
         if i == 1:
             if j in[1,9]:
                 print('*',end='')
             else:
                 print('', end=' ')
         elif i == 2:
             if j in[2,7]:
                print('*', end=' ')
             else:
              print('', end=' ')
         elif i == 3:
              if j in [3, 6]:
                  print('*', end=' ')
              else:
                  print('', end=' ')
         elif i == 4:
             if j in [4, 5]:
                 print('*', end=' ')
             else:
                 print('', end=' ')
         elif i == 5:
             if j in [5]:
                 print('*', end=' ')
             else:
                 print('', end=' ')


    print()