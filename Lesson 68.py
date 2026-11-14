#A Python program that finds the index where the sum of all values on the left equals the sum of all values on the right by calculating both sides for each position.
def find_equilibrium_index(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            return i         
    return -1
numbers = [-7, 1, 5, 2, -4, 3, 0]
index = find_equilibrium_index(numbers)
print(f"Equilibrium Index: {index}")
#A Python program that finds the value located at an equilibrium point where the sum of the elements on the left matches the sum of the elements on the right.
def find_equilibrium_value(arr):
    total_sum = sum(arr)
    left_sum = 0
    for num in arr:
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return num
        left_sum += num
    return None
numbers = [-7, 1, 5, 2, -4, 3, 0]
value = find_equilibrium_value(numbers)
print(f"Equilibrium Value: {value}")
#A Python program that checks each fixed-size subarray, calculates its sum, and returns the starting index of the first window whose total matches the target value.
def find_subarray_with_sum(arr, k, target):
    if k > len(arr) or k <= 0:
        return -1
    for i in range(len(arr) - k + 1):
        window = arr[i : i + k]
        if sum(window) == target:
            return i
    return -1
numbers = [2, 1, 5, 1, 3, 2]
window_size = 3
target_sum = 9
start_index = find_subarray_with_sum(numbers, window_size, target_sum)
print(f"Starting Index: {start_index}")