content = """# **Python List Cheat Sheet 🧵**

---

1. Access Elements
```
lst = [10, 20, 30, 40]

lst[0]    # 10
lst[2]    # 30
lst[-1]   # 40

```
2. Slicing
```
lst = [0, 1, 2, 3, 4, 5]

lst[1:4]   # [1, 2, 3]
lst[:3]    # [0, 1, 2]
lst[3:]    # [3, 4, 5]
lst[::2]   # [0, 2, 4]
lst[::-1]  # reverse copy

```
3. Change Values
```
lst = [10, 20, 30]
lst[1] = 99

lst = [1, 2, 3, 4]
lst[1:3] = [20, 30]

```
4. Add Items
```
lst = [1, 2]

lst.append(3)
lst.insert(1, 99)
lst.extend([4, 5])

```
5. Remove Items
```
lst = [10, 20, 30, 40]

lst.remove(20)
lst.pop()
lst.pop(1)
del lst[0]
lst.clear()

```
6.  Find Items
```
lst = [1, 2, 2, 3]

lst.index(2)
lst.count(2)

```
7. Sort
```
lst = [3, 1, 2]

lst.sort()
lst.sort(reverse=True)

new_lst = sorted(lst)

```
8. Reverse
```
lst = [1, 2, 3]

lst.reverse()
lst[::-1]

```
9. Length
```
lst = [10, 20, 30]

len(lst)

```
10. Check Existence
```
lst = ["python", "java"]

"python" in lst
"c++" not in lst

```
11.  Iterate Through List
```
lst = [10, 20, 30]

for item in lst:
    print(item)

for i in range(len(lst)):
    print(i, lst[i])

for i, item in enumerate(lst):
    print(i, item)

```
12. Copy
```
lst = [1, 2, 3]

a = lst.copy()
b = lst[:]
c = list(lst)

```
13.  Concatenate
```
a = [1, 2]
b = [3, 4]

c = a + b

```
14.  Multiply
```
lst = [1, 2]

lst * 3

```
15. Convert
```
list("abc")
"a,b,c".split(",")

chars = ["a", "b", "c"]
"".join(chars)

tuple([1, 2, 3])
set([1, 2, 2, 3])

```
16.  sum, min, max
```
nums = [5, 2, 9]

sum(nums)
min(nums)
max(nums)

```
