
def bubble_sort(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements (n-1 times)
    for i in range(n - 1):
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Pythonic tuple unpacking for swapping
    return arr

# Example Usage:
data = [5, 1, 4, 2, 8]
print(f"Original list: {data}")
sorted_data = bubble_sort(data)
print(f"Sorted list: {sorted_data}")
