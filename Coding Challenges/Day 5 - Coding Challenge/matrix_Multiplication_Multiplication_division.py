import numpy as np

matrix1 = [
    [1, 2, 3],
    [4, 8, 5],
    [9, 5, 4]
]

matrix2 = [
    [0, 1, 8],
    [1, 7, 0],
    [3, 1, 0]
]

Arr1 = np.array(matrix1)
Arr2 = np.array(matrix2)

result_multiply = np.multiply(Arr1, Arr2)
print(result_multiply)

result_subtract = np.subtract(Arr1, Arr2)
print(result_subtract)

with np.errstate(divide='raise', invalid='raise'):
    try:
        result_divide = np.divide(Arr1, Arr2)
        print("\nDivision Result:")
        print(result_divide)
    except FloatingPointError:
        print("Division by zero.")
