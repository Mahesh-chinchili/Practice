def is_prime(num):
   if num < 2:
       return False
   for i in range(2, int(num ** 0.5) + 1):
       if num % i == 0:
           return False
   return True


def sum_of_primes_in_range(M, N):
   prime_sum = sum(num for num in range(M, N + 1) if is_prime(num))
   return prime_sum


# Taking input from the user
M = int(input())
N = int(input())


# Calculating and printing the sum of prime numbers in the given range
result = sum_of_primes_in_range(M, N)
print(result)