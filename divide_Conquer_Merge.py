from sorting_algos import *

#1. If the list is empty or contains just one element, it is already sorted. Return it
#2. If the list contains 2 or more elements, run same function recursively to split the list into 2 smaller lists
#3. Merge the items in ascending order to reform the list of original size this time sorted
#3.1 Check if list1[0] is less than list2[0], if so, check if list1[1] is less than list2[0] and so on till this condition is not true
#3.2 Add list2[0] at the location where it is less than list1's element
#3.3 Check if list1[0] is less than list2[1], if so, check if list1[1] is less than list2[1] and so on till this condition is not true
#3.4 Adding list2[1] at the location where it is less than list1's element
#3.5 Return merged, sorted list

def merge(nums1, nums2):
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


# test0 = {
#     'input': {
#         'nums': [4, 2, 6, 3, 4, 6, 2, 1]
# 4, 2, 6, 3,
#     },
#[1, 2], [2, 3], [ 4, 4], [6, 6]
#[1, 2, 2, 3], [ 4, 4, 6, 6]

#     'output': [1, 2, 2, 3, 4, 4, 6, 6]



nums0, output0 = test0['input']['nums'], test0['output']

# print('Input:', nums0)
# print('Expected output:', output0)
# result0 = merge_sort(nums0)
# print('Actual output:', result0)
# print('Match:', result0 == output0)


print('Input:', nums0)
print('Expected output (merge_sort - divide and conquer):', output0)
result_sorted_list = merge_sort(nums0)
print('Actual output:', result_sorted_list)
print('Match:', result_sorted_list == output0)

# print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12]))
results = evaluate_test_cases(merge_sort, tests)



