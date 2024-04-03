import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

print("LCM CALCULATOR")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("LCM Value:", lcm_of_list(numbers))
