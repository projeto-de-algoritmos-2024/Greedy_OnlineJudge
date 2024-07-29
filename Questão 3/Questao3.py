def pylons(k, arr):
    n = len(arr)
    i = 0
    plants = 0

    while i < n:
        furthest = min(i + k - 1, n - 1)
        while furthest >= max(0, i - k + 1) and arr[furthest] != 1:
            furthest -= 1
        if furthest < max(0, i - k + 1):
            return -1
        plants += 1
        i = furthest + k
    return plants
