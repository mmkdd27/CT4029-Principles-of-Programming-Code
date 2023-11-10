import numpy as np
matrix = [
    [1, 2, 3],
    [4, 8, 5],
    [9, 5, 4]
]

Arr = np.array(matrix)
print(Arr)

new_shape = (1, -1)
Arr_reshaped = Arr.reshape(new_shape)

print(Arr_reshaped)
