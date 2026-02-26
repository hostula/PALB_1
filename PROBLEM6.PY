def max_subarray_sum(arr):
    max_sum = arr[0]          # overall maximum
    current_sum = arr[0]      # current running sum

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum subarray sum:", max_subarray_sum(arr))