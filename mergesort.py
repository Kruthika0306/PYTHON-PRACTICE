def merge_sort(arr):
    """
    Sorts a list of elements using the merge sort algorithm.
    """
    if len(arr) > 1:
        # Finding the midpoint of the array
        mid = len(arr) // 2

        # Dividing the array elements into two halves
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        # Sorting the first half recursively
        merge_sort(L)

        # Sorting the second half recursively
        merge_sort(R)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temporary lists L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any elements were left in L (if the end of R was reached first)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Check if any elements were left in R (if the end of L was reached first)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Driver code to test the implementation
if __name__ == '__main__':
    my_list = [12, 11, 13, 5, 6, 7]
    print(f"Given array is: {my_list}")

    merge_sort(my_list)

    print(f"Sorted array is: {my_list}")
