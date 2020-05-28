rows = int(input('input number of rows:'))

for i in range(rows):
    for j in range(2 * rows - 1):
        if rows - i <= j and j <= rows + i:
            print('*', end='')
        else:
            print(' ', end='')
        print()


