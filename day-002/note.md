# **DAY 002 - 06/04/2025**

**CS50P: Introduction To Programming with Python**
    
CONTINUATION OF **LECURE 0: Function_Variable**

## **STRING**
* String is a sequence of characters, enclosed in single (''), double ("") and triple ('""')quotes.

-  * **STRING FUNCTION**: is any function that works with strings -either built in functions like len(),or methods like uppper().
   - * len(): returns the length of a sting.
   - * str(): converts other data types into string.
   - * type(): tells you the data type.

- * **STRING METHODS**:is a built-in function in python that you can use with strings to perform specific tasks like changing text, finding things or formatting. **Method** is a function that is associated with an object. **Functions** are independent and can work on different types of data, while methods are attached to objects and work only on that specific type.

   - * .strip(): is used to remove leading and trailing whitespaces from a string. 
      - * .lstrip(): removes left space only.
      - * .rstrip(): removes right space only.
   - * capitalize(): convert the first character of a string and the rest to lowercases.
   - * .title(): capitalizes the first letter of each word in a string while converting the rest to lowercase. 
   - * .split(): is used to split a string into a list based in a separator(like a space or comma)

## - **INTEGER AND FLOAT**
- Integers are whole numbers without a decimal point, e.g, 1, -5, 100, 0, etc.
- Float are numbers with a decimal point or in exponential form, properly called a floating point value, e.g, 3.14, -0.5, 2.0, 1e3,3e5,etc.

- * Arithmetic operatoes:
   - * **Addition (+)**: adds two values.
   - * **Sutraction(-)**:subtracts the right operand from the left.
   - * **Multiplication(*)**: multiplies teo values.
   - * **Division(/)**: divides and return a float.
   - * **Floor(//)**: divides and retuen the integer part (floor) of the result.
   - * **Modulus(%)**: returns the remainder of the division.

```md
>>> 1+2
3
>>> 5-1
4
>>> 5*2
10
>>> 1+2
3
>>> 5-1
4
>>> 5*2
10
>>> 7/2
3.5
>>> 9//5
1
>>> 7%5
2
```
- **PYTHON INTERACTIVE MODE**
- Python interactive mode is a way to run Python commands one at a time and get immediate feedback. It's super useful for testing small pieces of code, exploring libraries, or doing quick calculations.
- * How to Access Interactive Mode:
   - * From the Terminal/Command Line,
   - Just type *python* or *python3* (depending on your system).
- * To Exit Interactive mode:
   - * Press ***Ctrl + Z***

###- **ROUND() FUNCTION**:
- - Round() Function in python is used to round a number to the nearest integer or to a specified number if decimal places.
- - Syntax:
   ```bash
      round(number[,ndigits])
   ```
   - * number: The number you want to round.
   - * ndigits: number of decimal places to round to.
      - - if omitted, it rounds to the nearest **whole number**.
      - - if given, it rounds to that many decimal places.
- **NOTE:** Python uses a rule called ***ROUND HALF TO EVEN***, ALSO KNOWN AS ***BANKER'S ROUNDING*** If a number is exactly halfway between two integers (like -2.5 is between -2 and -3 ), ***python will round to the nearest even number.***

### - * **DEF FUNCTION:**
   - * def is used to define a function.

- * **RETURN statement:**
   - * return statement is used in a function to send a value back to the caller. It ends the function and returns the apecified value.
   - * reurn statement syntax:
   ```bash
         def function():
             return value
   ```

- ***Return VS Print***
   - * ***return*** sends data to caller, while ***print*** just shows data to the screen.
   - * ***return*** is used in calculation and logic, whereas ***print*** is used for debugging and displaying,
   - * ***return*** function output is usable, while ***print*** output is not usable in code.
