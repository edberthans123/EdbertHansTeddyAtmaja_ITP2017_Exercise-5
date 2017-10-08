import math
def hypotenuse(w,p):
    try:
        return math.sqrt(w**2+p**2)
    except TypeError:
        return None

print(hypotenuse(2,3))#two numbers
print(hypotenuse("2","3"))#two strings
print(hypotenuse(2,"3"))#one number and one string

