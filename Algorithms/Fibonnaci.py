def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)


def fastFibonnaci(n):
    if n == 1 or n == 2:
        return 1

    f1 = 1
    f2 = 1

    for i in range(3, n + 1):
        f = f1 + f2
        f2 = f1
        f1 = f
    return f1


print("Fastly Calculation of Fibonnaci (For Method)")
print(fastFibonnaci(10))
print('Slowly Calculation of Fibonnaci (Recursion)')
print(fibonnaci(10))
