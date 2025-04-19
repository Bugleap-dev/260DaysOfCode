# **DAY 004 - 18/04/2025**

**CS50P: Introduction To Programming with Python**

## **LECTURE 1 -CONDITIONALS **



# Python Conditionals and Related Concepts

## Table of Contents
1. [Comparison Operators](#comparison-operators)
2. [Conditional Statements](#conditional-statements)
   - [if Statement](#if-statement)
   - [elif (Else If)](#elif-else-if)
   - [else](#else)
3. [Logical Operators](#logical-operators)
   - [or](#or)
   - [and](#and)
4. [Boolean Type](#boolean-type)
5. [Pattern Matching](#pattern-matching)

---

## Comparison Operators

| Operator | Meaning                          | Example          |
|:---------|:----------------------------------|:-----------------|
| `>`       | Greater than                     | `5 > 3` → `True`  |
| `<`       | Less than                        | `2 < 7` → `True`  |
| `>=`      | Greater than or equal to          | `5 >= 5` → `True` |
| `<=`      | Less than or equal to             | `4 <= 6` → `True` |
| `!=`      | Not equal to                     | `5 != 3` → `True` |
| `==`      | Equal to                         | `5 == 5` → `True` |
| `%`       | Modulus (remainder after division) | `7 % 3` → `1`     |

---

## Conditional Statements

### `if` Statement
Executes a block of code if a specified condition is `True`.

```python
x = 10
if x > 5:
    print("x is greater than 5")
