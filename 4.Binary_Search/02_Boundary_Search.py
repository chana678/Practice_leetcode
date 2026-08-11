'''
Boundary Search using Bianry Search

'''

def first_occurrence(nums, target):
    '''
    Returns the index of the first occurrence for the target variable in the list.
    '''
    left = 0
    right = len(nums) - 1
    start_index = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            start_index = mid
            right = mid - 1

        elif nums[mid] > target:
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

    return start_index

def last_occurrence(nums, target):
    '''
    Returns the index of the last occurrence of the target variable in the list
    '''
    left = 0
    right = len(nums) - 1
    end_index = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            end_index = mid
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

    return end_index

def search_range(nums, target):
    start_index = first_occurrence(nums,target)
    end_index = last_occurrence(nums, target)

    return f"[{start_index},{end_index}]"


nums = [1,2,2,2,2,3,4]
target = 2

print(search_range(nums,target))

'''
Time complexity : O(log n) + O(log n), because we are defining two seperate binary search, 
final time complexity O(log n)

Space Complexity : O(1) , Only for variable declaration
'''
