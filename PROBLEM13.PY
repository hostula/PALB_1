def three_way_partition(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif a <= arr[mid] <= b:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# Example
arr = [1, 4, 3, 2, 5, 6, 7]
a = 3
b = 5

print(three_way_partition(arr, a, b))