def factorial(p):
    try:
        if p == 1:
            return 1
        elif p == 0:
            return 1
        else:
            return p*factorial(p-1)
    except(RecursionError,TypeError):
        return None

w = float(input('Input number here: '))
if w > 1:
    print(int(factorial(w)))
elif 0 <= w <= 1:
    print(1)

