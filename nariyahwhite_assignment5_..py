Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> print("=== Challenge 3: Multiplication Table ===")
... print("Multiplication Table:")
... 
... print("      ", end="")
... for i in range(1, 11):
...     print(f"{i:4}", end="")
... print()
... 
... for row in range(1, 11):
...     print(f"{row:2}")
...     print("  ", end="")
...     for i in range(1, 11):
...         product = row * i
...         print(f"{product:4}", end="")
...     print()
