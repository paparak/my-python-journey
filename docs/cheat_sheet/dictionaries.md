content = """# **Python Dictionaries Cheat Sheet 🧵**

---

1. Definition
```
person = {"name": "Parisa", "age": 27, "skill": "Python"}

```
2. Accessing Values
```
print(person["name"])     # Parisa
print(person.get("age"))  # 27


```
3. Adding / Updating Items
```
person["city"] = "Tehran"   # Add new key
person["age"] = 26          # Update existing key


```
4. Removing Items
```
person.pop("age")    # Remove by key
del person["skill"]  # Delete key


```
5. Dictionary Methods
```
person.keys()     # All keys
person.values()   # All values
person.items()    # Key-value 


```
6.  Looping Through Dictionary
```
for key, value in person.items():
print(key, value)


```
7. Check If Key Exists
```
if "name" in person:
print("Key exists")

```
8.Dictionary Length
```
len(person)
```
