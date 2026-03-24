import numpy as np

# Python list — slow
data = [1, 2, 3, 4, 5]
result = []
for x in data:
    result.append(x * 2)

print("Python list result:")
print(result)

# NumPy — fast, clean, industry standard
data = np.array([1, 2, 3, 4, 5])
result = data * 2   # operates on entire array at once
print("\nNumPy result:")
print(result)
# This is called vectorization. It is how ML works at scale

# ---------------------


# From list
a = np.array([10, 20, 30, 40, 50])
print("\nArray from list:")
print(a, "\n")

# Zeros and ones
zeros = np.zeros(5)        # [0. 0. 0. 0. 0.]
ones  = np.ones(5)         # [1. 1. 1. 1. 1.]
print("Zeros:", zeros)
print("Ones:", ones, "\n")

# Range
r = np.arange(0, 10, 2)   # [0 2 4 6 8]
print("Range:", r)
print()
# Evenly spaced
ls = np.linspace(0, 1, 5) # [0. 0.25 0.5 0.75 1.]
print("Linspace:", ls)

print("\nArray properties:")
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)
print("Shape:", a.shape)    # (2, 3) → 2 rows, 3 columns
print("Dimensions:", a.ndim)     # 2 → 2-dimensional
print("Data type:", a.dtype)    # int64
print("Size:", a.size)     # 6 → total elements

print("\n\nArray Indexing and Slicing:")

a = np.array([10, 20, 30, 40, 50])
print("Array:", a)        # [10 20 30 40 50]
print("Element at index 0:", a[0])      # 10
print("Last element:", a[-1])     # 50
print("Slice [1:4]:", a[1:4])    # [20 30 40]
print("Every 2nd element [::2]:", a[::2])    # [10 30 50] — every 2nd element

# 2D array
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print("\n2D Array:\n", b)
print("Element at row 0, column 1:", b[0, 1])    # 2 — row 0, col 1
print("All rows, column 1:", b[:, 1])    # [2 5] — all rows, col 1
print("Row 1, all columns:", b[1, :])    # [4 5 6] — row 1, all cols

# Vectorized operations — no loops:
print("\n\nVectorized operations — no loops:")
a = np.array([1, 2, 3, 4, 5])

print("Array a:", a)
print("a + 10:", a + 10)      # [11 12 13 14 15]
print("a * 2:", a * 2)       # [ 2  4  6  8 10]
print("a ** 2:", a ** 2)      # [ 1  4  9 16 25]
print("a > 3:", a > 3)       # [False False False  True  True]

# Two arrays
b = np.array([10, 20, 30, 40, 50])
print("Array a:", a)
print("Array b:", b)
print("a + b:", a + b)       # [11 22 33 44 55]

print("\n\nStatistical operations — what you will use in ML every day:")
a = np.array([4, 7, 2, 9, 1, 5])

print("Array a:", a)
print("Sum:", np.sum(a))     # 28
print("Mean:", np.mean(a))    # 4.666...
print("Median:", np.median(a))  # 4.5
print("Standard Deviation:", np.std(a))     # 2.624...
print("Minimum:", np.min(a))     # 1
print("Maximum:", np.max(a))     # 9
print("Index of Maximum:", np.argmax(a))  # 3 → index of max value
print("Index of Minimum:", np.argmin(a))  # 4 → index of min value


print("\n\nBoolean filtering — core ML operation:")

a = np.array([10, -5, 30, -2, 50, 0])

print("Array a:", a)
# Get all positive values
positive = a[a > 0]
print("Positive values:", positive)   # [10 30 50]

# Replace negatives with 0
a[a < 0] = 0
print("Array after replacing negatives with 0:", a)   # [10  0 30  0 50  0]

# Reshape — critical for ML:
print("\n\nReshape — critical for ML:")
a = np.arange(12)          # [ 0  1  2 ... 11]
b = a.reshape(3, 4)        # 3 rows, 4 cols
c = a.reshape(2, 2, 3)     # 3D array
print("Original array a:", a)
print("Reshaped to 3x4:\n", b)
print("Reshaped to 2x2x3:\n", c)
# Flatten back to 1D
d = b.flatten()
print("Flattened array:", d)
print("\n\n")
# ===================

def demonstrate_arrays():
    print("=== Array Creation ===")
    a = np.array([5, 10, 15, 20, 25])
    print(f"Array     : {a}")
    print(f"Shape     : {a.shape}")
    print(f"Dtype     : {a.dtype}")
    print(f"Size      : {a.size}")

def demonstrate_operations():
    print("\n=== Vectorized Operations ===")
    a = np.array([1, 2, 3, 4, 5])
    print(f"Original  : {a}")
    print(f"x2        : {a * 2}")
    print(f"Squared   : {a ** 2}")
    print(f"+ 100     : {a + 100}")
    print(f"> 3 mask  : {a > 3}")
    print(f"Filtered  : {a[a > 3]}")

def demonstrate_stats():
    print("\n=== Statistics ===")
    data = np.array([23, 45, 12, 67, 34, 89, 56, 11, 78, 90])
    print(f"Data      : {data}")
    print(f"Mean      : {np.mean(data):.2f}")
    print(f"Median    : {np.median(data):.2f}")
    print(f"Std Dev   : {np.std(data):.2f}")
    print(f"Min       : {np.min(data)}")
    print(f"Max       : {np.max(data)}")
    print(f"Argmax    : index {np.argmax(data)} → value {data[np.argmax(data)]}")
    print(f"Argmin    : index {np.argmin(data)} → value {data[np.argmin(data)]}")
    print(f"25th Percentile : {np.percentile(data, 25):.2f}")
    print(f"75th Percentile : {np.percentile(data, 75):.2f}")


def demonstrate_2d():
    print("\n=== 2D Arrays (Matrix) ===")
    matrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    print(f"Matrix:\n{matrix}")
    print(f"Shape     : {matrix.shape}")
    print(f"Row 0     : {matrix[0, :]}")
    print(f"Col 1     : {matrix[:, 1]}")
    print(f"Element   : {matrix[1, 2]}")
    print(f"Col means : {np.mean(matrix, axis=0)}")
    print(f"Row means : {np.mean(matrix, axis=1)}")

def demonstrate_reshape():
    print("\n=== Reshape ===")
    a = np.arange(12)
    print(f"Original  : {a}")
    print(f"Reshaped  :\n{a.reshape(3, 4)}")
    print(f"Flattened : {a.reshape(3, 4).flatten()}")


if __name__ == "__main__":
    demonstrate_arrays()
    print("\n\n")
    demonstrate_operations()
    print("\n\n")
    demonstrate_stats()
    print("\n\n")
    demonstrate_stats()
    print("\n\n")
    demonstrate_2d()
    print("\n\n")
    demonstrate_reshape()