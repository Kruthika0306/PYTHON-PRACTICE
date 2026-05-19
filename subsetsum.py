def subset_sum(arr, target, index=0, current=[]):

    # Target found
    if target == 0:
        print("✅ Subset Found:", current)
        return True

    # Out of bounds or negative target
    if index >= len(arr) or target < 0:
        return False

    # INCLUDE current element
    if subset_sum(
        arr,
        target - arr[index],
        index + 1,
        current + [arr[index]]
    ):
        return True

    # EXCLUDE current element
    if subset_sum(
        arr,
        target,
        index + 1,
        current
    ):
        return True

    return False


arr = [3, 4, 5, 2]
target = 7

subset_sum(arr, target)
