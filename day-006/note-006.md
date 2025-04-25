# **DAY 006 - 20/04/2025**

**CS50P: Introduction To Programming with Python**

## LECTURE 1 - CONDITIONALS

## Table of Contents
1. [Boolean Type](#boolean-type)
2. [Pattern Matching](#pattern-matching)


### Boolean Type
`bool`
The bool type represents one of two values: True or False.
```python
is_active = True
print(bool(0))   # False
print(bool(5))   # True
```

### Pattern Matching
`match` Statement
Introduced in Python 3.10. It checks a value against different cases (similar to switch in other languages).

```python
command = "start"

match command:
    case "start":
        print("Starting the system...")
    case "stop":
        print("Stopping the system...")
    case _:
        print("Unknown command")
case _: acts as a default if no other case matches.
```