def search_insert(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left   # insert position


# Example
arr = [1, 3, 5, 6]
target = 5
print(search_insert(arr, target))  # Output: 2

target = 2
print(search_insert(arr, target))  # Output: 1

target = 7
print(search_insert(arr, target))  # Output: 4