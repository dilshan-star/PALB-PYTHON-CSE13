# Function to find the largest element
def find_largest(arr):
    largest = arr[0]       
    
    for num in arr:         
        if num > largest:   
            largest = num   
            
    return largest

arr = [1, 8, 7, 56, 90]

# Function call
result = find_largest(arr)

print(result)
