import numpy as np

def flip_zeros(arr, num):
    val_to_flip = 0 if num >= 0 else 1
    num = abs(num)

    indices = np.argwhere(arr == val_to_flip)
    selected_indices = indices[np.random.choice(len(indices), size=num, replace=False)]
    
    # Flip the selected indices to one
    for i, j in selected_indices:
        arr[i][j] = (val_to_flip + 1) % 2
    

if __name__ == "__main__":
    # Create a 2D numpy array of shape (4, 4) with all values as zero
    arr = np.zeros((4, 4), dtype=int)
    
    # Flip 4 zero values to one
    for i in range(5):
        flip_zeros(arr, 2)
        print(arr)





