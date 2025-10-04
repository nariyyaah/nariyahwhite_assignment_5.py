Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> print("=== Challenge 1: Collatz Conjecture ===")
... 
... current_number = int(input("Enter starting number: "))
... step_count = 0
... 
... print("Sequence:", end= " ")
... while current_number != 1: #this keeps looping until the condition is true
...     print(current_number, end= " ")
...     step_count +=1
... 
...     if current_number % 2 == 0:
...         current_number = current_number // 2
...     else:
...         current_number = current_number * 3 + 1
... print(current_number)
