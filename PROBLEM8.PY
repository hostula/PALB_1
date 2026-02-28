def min_jumps(arr):
    n = len(arr)

    # Edge cases
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    farthest = 0
    end = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])

        # When we reach the end of current jump range
        if i == end:
            jumps += 1
            end = farthest

            # If we can't move further
            if end <= i:
                return -1

        # If we can already reach the last index
        if end >= n - 1:
            return jumps

    return -1