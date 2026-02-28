def kth_smallest(arr, k):
    k = k - 1  # convert to 0-based index

    def quickselect(left, right):
        pivot = arr[right]
        p = left

        for i in range(left, right):
            if arr[i] <= pivot:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1

        arr[p], arr[right] = arr[right], arr[p]

        if p == k:
            return arr[p]
        elif p > k:
            return quickselect(left, p - 1)
        else:
            return quickselect(p + 1, right)

    return quickselect(0, len(arr) - 1)