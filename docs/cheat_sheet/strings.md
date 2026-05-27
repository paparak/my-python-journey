content = """# **Python Strings Cheat Sheet 🧵**

---

1. Basic Operations
```
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # "Hello World"
print(s1 * 3)         # "HelloHelloHello"
print(len(s1))        # 5
```
2. Indexing 
```
s = "Python"
print(s[0])   # 'P'
print(s[-1])  # 'n'
```
3. Slicing
```
s = "Python"
print(s[0:3])   # 'Pyt'
print(s[:3])    # 'Pyt'
print(s[3:])    # 'hon'
print(s[::-1])  # 'nohtyP'
```
4. Searching
```
s = "Hello World"
print(s.find("World"))  # 6
print(s.index("World")) # 6
```
5. Counting
```
s = "banana"
print(s.count("a"))  # 3
```
6. Membership
```
s = "Hello World"
print("World" in s)      # True
print("Python" not in s) # True
```
7. Case Conversion
```
s = "pyThOn"
print(s.lower())       # "python"
print(s.upper())       # "PYTHON"
print(s.title())       # "Python"
print(s.capitalize())  # "Python"
print(s.swapcase())    # "PYtHon"
```
8. Stripping
```
s = "  hello  "
print(s.strip())   # "hello"
print(s.lstrip())  # "hello  "
print(s.rstrip())  # "  hello"
```
9. Replacing
```
s = "I love Java"
print(s.replace("Java", "Python")) # "I love Python"
```
10. Splitting and Joining
```
s = "apple,banana,cherry"
fruits = s.split(",")  # ['apple', 'banana', 'cherry']
print("-".join(fruits))  # "apple-banana-cherry"
```
11. Start and End Check
```
s = "report.pdf"
print(s.startswith("rep")) # True
print(s.endswith(".pdf"))   # True
```
12. Content/Type Check
```
print("12345".isdigit())    # True
print("Hello".isalpha())    # True
print("Hello12".isalnum())  # True
print("   ".isspace())      # True
```
13. Padding and Alignment
```
s = "hi"
print(s.center(10, "-"))  # "----hi----"
print(s.ljust(10, "-"))   # "hi--------"
print(s.rjust(10, "-"))   # "--------hi"
```
14. Zero Padding (Zfill)
```
num = "42"
print(num.zfill(5))  # "00042"
```
15. Formatting
```
name = "Parisa"
age = 25
print(f"My name is {name} and I am {age}.")
print("My name is {}.".format(name))
```
16. Conversion
```
print(list("Py"))  # ['P', 'y']
print(int("10") + 5)   # 15
print(float("3.14"))   # 3.14
```
17. Sorting
```
s = "cba"
print("".join(sorted(s))) # "abc"
```




















