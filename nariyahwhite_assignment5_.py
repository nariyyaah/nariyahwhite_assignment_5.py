Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> print("=== Challenge 2: Prime Number Checker ===")
... num = int(input("Enter a number: ")) #prompting user to enter a number
... print(f"Testing divisors from 2 to {num - 1}...")
... 
... prime_art = True
... for i in range(2, num): #check number from 2 up to num
...     if num % i == 0: #if num divides evenly from i its not prime
...         prime_art = False
...         divisors = i
...         break #stops checking
... if prime_art:
...     print(f"{num} is prime!")
... else:
...     print(f"{num} is not prime (divisible by {divisors})")
... 
