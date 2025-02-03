# Uncommon ZeroDivisionError Masking in Python

This repository demonstrates a subtle bug involving a `ZeroDivisionError` in Python.  The error is not immediately obvious due to conditional logic within the function.  The `bug.py` file contains the buggy code, while `bugSolution.py` provides a corrected version with improved error handling.

## Bug Description

The function `function_with_uncommon_error` attempts to handle division by zero by checking `if b == 0`. However, it fails to handle the case where `a == 0` and `b` is any non-zero number.  This leads to an incorrect result if 'b' is 0 and a is non-zero, but a `ZeroDivisionError` if 'a' is 0 and 'b' is non-zero, resulting in an unusual error scenario.

## Solution

The solution involves adding more comprehensive error handling to cover all possible cases where division by zero could occur.  The corrected code in `bugSolution.py` uses a `try-except` block to gracefully handle the `ZeroDivisionError`, providing a more robust and predictable behavior.