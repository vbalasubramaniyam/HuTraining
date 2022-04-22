class Pattern3():
    n = 5
    for rows in range(n):
        for columns in range(n):
            if rows == 0 or columns == (n - 1) or rows == columns:
                print('*', end='')
            else:
                print(end=' ')
        print()

