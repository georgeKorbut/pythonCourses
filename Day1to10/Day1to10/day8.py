#day 8 of 100 days of python

#prime number check
import math


def check_if_prime(n):
    is_prime = True
    n_sqrt = math.ceil(math.sqrt(n))
    first_divisor = 0
    for num in range(2, n_sqrt+1):
        if n % num == 0:
            is_prime = False
            first_divisor = num    
            break
    if is_prime:
        print(f"{n} is prime!")
    else:
        print(f"{n} is not prime. It is divisible by {first_divisor}.")          


n = int(input("Check if this number is prime:"))
check_if_prime(n)
