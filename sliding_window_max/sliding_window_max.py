'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    if nums == []:
        return []
    x, y = [], []
    for i in range(0, k):
        while y != [] and nums[i] > nums[y[-1]]:
            y.pop()
        y.append(i)
    for i in range(k, len(nums)):
        x.append(nums[y[0]])
        while y != [] and nums[i] > nums[y[-1]]:
            y.pop()
        y.append(i)
        while y != [] and y[0] <= i-k:
            y.pop(0)
    x.append(nums[y[0]])
    return x


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
