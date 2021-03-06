'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    nums = {}
    for num in arr:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1
    for num in nums:
        if nums[num] == 1:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")