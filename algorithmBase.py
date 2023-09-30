import numpy as np

def generate_random_array(rows, cols):
    # Generate a random 2D array with values 0 and 1
    return np.random.randint(2, size=(rows, cols))

def modify_array_to_k_ones(arr, k):
    # Flatten the 2D array to a 1D array
    num_rows, num_columns = arr.shape
    size_r = num_rows *num_columns
    flat_arr = arr.flatten()


    # Count the current number of 1's in the flattened array
    current_ones = np.sum(flat_arr == 1)


    if current_ones == k:
        # If we already have k 1's, return the original array
        return arr
    else:

        while(current_ones!=k):
            x = np.random.randint(0, size_r)
            if flat_arr[x] != 1:
                flat_arr[x] = 1
                current_ones+=1

    # Reshape the modified 1D array back to the original shape
    modified_array = flat_arr.reshape(arr.shape)

    return modified_array

original_array = np.array([[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]])



print("Original Array:")
print(original_array)

for i in range(9):
    original_array = modify_array_to_k_ones(original_array, i)

    print("Original Array:")
    print(original_array)
    print(f"Desired Number of 1s (k): {i}")
    print()




