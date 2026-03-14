def min_chocolate_diff(arr, m):
    n = len(arr)

    # If students are more than packets
    if m > n:
        return -1

    # Sort the array
    arr.sort()

    min_diff = float('inf')

    # Find the minimum difference
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


# Example
arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print("Minimum difference:", min_chocolate_diff(arr, m))