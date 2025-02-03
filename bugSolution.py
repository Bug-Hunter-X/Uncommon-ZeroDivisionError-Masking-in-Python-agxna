def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

result = function_with_uncommon_error(10, 0)  # This now handles the ZeroDivisionError
print(result)

result = function_with_uncommon_error(0, 10) #This also works as intended
print(result) 