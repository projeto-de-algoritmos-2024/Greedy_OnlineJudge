def boardCutting(cost_y, cost_x):
    MOD = 10**9 + 7
    
    # Sort the costs in descending order
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)
    
    # Initialize segments and costs
    horizontal_segments = 1
    vertical_segments = 1
    total_cost = 0
    
    i, j = 0, 0
    while i < len(cost_y) and j < len(cost_x):
        if cost_y[i] > cost_x[j]:
            total_cost += cost_y[i] * vertical_segments
            horizontal_segments += 1
            i += 1
        else:
            total_cost += cost_x[j] * horizontal_segments
            vertical_segments += 1
            j += 1
    
    # Add the remaining costs
    while i < len(cost_y):
        total_cost += cost_y[i] * vertical_segments
        i += 1
    
    while j < len(cost_x):
        total_cost += cost_x[j] * horizontal_segments
        j += 1
    
    return total_cost % MOD
