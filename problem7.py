def find_min_max(arr):
    minimum = min(arr)
    maximum = max(arr)
    return [minimum, maximum]

arr = [1, 4, 3, 5, 8, 6]

# Function call
result = find_min_max(arr)

print(result)