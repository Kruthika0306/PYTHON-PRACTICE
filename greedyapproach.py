def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Create list of tuples (value, weight, ratio)
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((values[i], weights[i], ratio))
    
    # Sort items based on ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    
    for value, weight, ratio in items:
        if capacity >= weight:
            # Take full item
            total_value += value
            capacity -= weight
        else:
            # Take fractional part
            total_value += value * (capacity / weight)
            break
    
    return total_value


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value:", max_value)