'''
Binary Search Implementation

'''

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

    return -1

nums = [1,3,5,7,9,11,13,15]
target = 9

print(binarySearch(nums, target))