def fractional_knapsack(weights, values, W):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0

    for w, v in items:
        if W >= w:
            W -= w
            total_value += v
        else:
            total_value += v * (W / w)
            break

    return total_value

print(fractional_knapsack([10,20,30], [60,100,120], 50))
