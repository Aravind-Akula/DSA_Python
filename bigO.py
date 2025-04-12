# Constant Time: O(1)
# Explanation: The operation takes the same amount of time regardless of the input size.
def constant_time_example(arr):
    print(arr[0])  # Accessing the first element is O(1)

# Linear Time: O(n)
# Explanation: The operation scales linearly with the size of the input.
def linear_time_example(arr):
    for item in arr:
        print(item)  # Iterating through the array is O(n)

# Quadratic Time: O(n^2)
# Explanation: The operation scales quadratically with the size of the input.
def quadratic_time_example(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Nested loops result in O(n^2)

# Logarithmic Time: O(log n)
# Explanation: The operation reduces the problem size by half each time.
def logarithmic_time_example(n):
    while n > 1:
        print(n)
        n //= 2  # Halving the input size results in O(log n)

# Linearithmic Time: O(n log n)
# Explanation: Common in efficient sorting algorithms like merge sort.
def linearithmic_time_example(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = linearithmic_time_example(arr[:mid])
    right = linearithmic_time_example(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Exponential Time: O(2^n)
# Explanation: The operation doubles in size with each additional input.
def exponential_time_example(n):
    if n == 0:
        return 1
    return exponential_time_example(n - 1) + exponential_time_example(n - 1)  # Recursive calls result in O(2^n)

# Factorial Time: O(n!)
# Explanation: The operation grows factorially with the input size.
def factorial_time_example(n):
    if n == 0:
        return [[]]
    prev = factorial_time_example(n - 1)
    result = []
    for seq in prev:
        for i in range(len(seq) + 1):
            result.append(seq[:i] + [n] + seq[i:])
    return result

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3]
    print("O(1):")
    constant_time_example(arr)
    
    print("\nO(n):")
    linear_time_example(arr)
    
    print("\nO(n^2):")
    quadratic_time_example(arr)
    
    print("\nO(log n):")
    logarithmic_time_example(8)
    
    print("\nO(n log n):")
    print(linearithmic_time_example(arr))
    
    print("\nO(2^n):")
    print(exponential_time_example(3))
    
    print("\nO(n!):")
    print(factorial_time_example(3))
    
    

