#===================================== First Task - Dot Product======================================#
# Function to calculate the dot product of two vectors v1 and v2
def dot_product(v1, v2):
    if len(v1) != len(v2):
        return None  # Vectors must be of the same length
    ps = 0
    for i in range(len(v1)):
        ps += v1[i] * v2[i]
    return ps

# Algorithm to check if two vectors are orthogonal
def are_orthogonal(v1, v2):
    dot_result = dot_product(v1, v2)
    if dot_result is None:
        return False  # Vectors must be of the same length
    return dot_result == 0

# Example usage
v1 = [1, 2, 3]
v2 = [4, -2, 1]
v3 = [0, 0, 1]

result1 = are_orthogonal(v1, v2)  # False
result2 = are_orthogonal(v1, v3)  # True
print(result1, result2)
#===================================== Second Task - Insertion Sort======================================#
# Function to perform insertion sort on an array
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
