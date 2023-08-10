

def sort(nums):
    pass


def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    #print('bubble_sort: ', nums)
    # 4. Repeat the process n-1 times
    for j in range(len(nums) - 1):
        #print("Iteration: ", j)

        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            #print("i:", i, nums[i], nums[i+1])

            # 2. Compare the number with
            if nums[i] > nums[i + 1]:
                # 3. Swap the two elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    # Return the sorted list
    return nums




# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}
# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}
# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}
# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}
# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}
# An empty list
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}
# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}
# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

nums0, output0 = test0['input']['nums'], test0['output']

# print('Input:', nums0)
# print('Expected output:', output0)
# result0 = bubble_sort(nums0)
# print('Actual output:', result0)
# print('Match:', result0 == output0)

from jovian.pythondsa import evaluate_test_cases
#results = evaluate_test_cases(bubble_sort, tests)

def insertion_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    #Iterate over the length of the array n times
    for i in range(len(nums)):
        #pop removes the ith item from the list and is saved in cur
        cur = nums.pop(i)
        #print("i = ", i, 'Cur = ', cur)
        #set value of j as i-1 so the previous value in the array is read
        j = i-1
        #While j >= 0 allows for 1st element in the array to be read, AND if it is also greater than cur
        while j >=0 and nums[j] > cur:
            #decrement the value of j further by 1 as the while iterates downward till 0 and keeps comparing with cur
            #print("j = ", j, "nums[j] = ", nums[j])
            j -= 1
        #Insert cur where nums[j] was and pushing that value ahead
        nums.insert(j+1, cur)
        #print("nums =", nums)
    return nums
nums0, output0 = test0['input']['nums'], test0['output']

# print('Input:', nums0)
# print('Expected output:', output0)
# result0 = insertion_sort(nums0)
# print('Actual output (after insertion sort):', result0)
# print('Match:', result0 == output0)

#results = evaluate_test_cases(insertion_sort, tests)