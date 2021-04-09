for n in range(10, 25):
    a = n % 2
    b = n % 3
    if a == 0:
        print(n, 'bukan prima')
    elif b == 0:
        print(n, 'bukan prima')
    else:
        print(n, 'adalah bilangan prima')