def print_cm(result):
    print('\t\t     Actual')
    print('\t\t  False\t  True')
    print('Predicted  False  ',
          str(result[0][0]).rjust(4), ' ',
          str(result[0][1]).rjust(4))
    print('\t   True   ',
          str(result[1][0]).rjust(4), ' ',
          str(result[1][1]).rjust(4))