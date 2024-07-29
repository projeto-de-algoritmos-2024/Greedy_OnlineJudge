def sherlockAndMinimax(arr, p, q):
    arr.sort()
    candidates = []

    # Adding boundary points
    candidates.append(p)
    candidates.append(q)

    # Adding mid points of all consecutive elements
    for i in range(len(arr) - 1):
        mid = (arr[i] + arr[i + 1]) // 2
        if p <= mid <= q:
            candidates.append(mid)

    # Find the optimal p from candidates
    optimal_p = -1
    optimal_minimax = -1

    for candidate in candidates:
        minimax = min(abs(candidate - x) for x in arr)
        if minimax > optimal_minimax or (minimax == optimal_minimax and candidate < optimal_p):
            optimal_minimax = minimax
            optimal_p = candidate

    return optimal_p