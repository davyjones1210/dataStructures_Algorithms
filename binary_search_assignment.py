#Given a list of unique numbers, arranged in increasing order, rotated unknown number of times
#write a function to deter min. number of times original list was sorted
#input = 'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], output = 3


def count_rotations_binary(nums):
    count_rotations_binary.iterations_count = 0

    #print("Binary search\n")
    lo = 0
    hi = len(nums)
    #print("Hi:", hi)


    while lo <= hi and hi != 0:
        mid = (lo + hi) // 2
        #print("lo:", lo, ", hi:", hi, ", mid:", mid)
        count_rotations_binary.iterations_count += 1
        
        if len(nums) == 1:
            return 0
        else:
            mid_number = nums[mid]
        end_number = nums[hi-1]

        # Uncomment the next line for logging the values and fixing errors.

        #print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number, "First number:", nums[lo] ,"End number:",nums[hi-1])

        if mid > 0 and nums[mid] < nums[mid-1]:
            # The middle position is the answer
            return mid

        elif mid_number < end_number:
            # Answer lies in the left half
            hi = mid - 1

        else:
            # Answer lies in the right half
            lo = mid + 1


    #print("Number of iterations: ", iteration_count)
    return 0


def count_rotations_linear(nums):
    #print("Linear search\n")
    position = 0  # What is the intial value of position?

    while position < len(nums):  # When should the loop be terminated?

        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position-1]:  # How to perform the check?
            return position

        # Move to the next position
        position += 1

    return 0  # What if none of the positions passed the check


def count_rotations(nums):
    pass


test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}



#print(result0, result0 == output0)
from jovian.pythondsa import evaluate_test_case


test0 = test
# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
}
# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1,2,3,4]
    },
    'output': 0
}

# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [7,3,5]
    },
    'output': 1
}
# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [2,3,4,5,6,7,8,1]
    },
    'output': 7
}
# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [3,5,7,8,9,10]
    },
    'output': 0
}

# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}
# A list containing just one element.
test7 = {
    'input': {
        'nums': [8]
    },
    'output': 0
}

test8 = {
    'input': {
        'nums': [7, 8, 1, 3, 4, 5, 6]
    },
    'output': 2
}

test9 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, -1, 0]
    },
    'output': 5
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9]
#print("Test cases: ", tests)

nums0 = test1['input']['nums']
output0 = test1['input']['nums']
result0 = count_rotations_binary(nums0)
#print("Result of binary search: ", result0)

nums1 = test1['input']['nums']
output1 = test1['input']['nums']
result1 = count_rotations_linear(nums1)
#print("Result of linear search: ", result1)

from jovian.pythondsa import evaluate_test_cases
#evaluate_test_cases(count_rotations_linear, tests)


#[5,6,7,1,3]

#Linear search algorithm
#1. read first element of the list, position 0
#2. check to see if it is less than the number on the right as the original is in ascending order
#3. if the number on the right is less than that of the element being read, that is the position zero of the original list
#4. return the position of the smallest element of the list as k = number of times rotation happened
#5. check the returned value with expected output

#evaluate_test_case(count_rotations_linear, test1)


#Counting algorithm's complexity is counting number of iterations - number of executions of while loop

#Binary search algorithm
#1. Read middle element of the list
#2. Check to see if middle element is smaller than last element of the range
#3. if the middle element is smaller than the last element, the answer lies to the left
#4. If not, the answer is to the right
#5. If the answer is to the left, update list to read only block to the left and retry step 1

#evaluate_test_case(count_rotations_binary, test7)
evaluate_test_cases(count_rotations_binary, tests)


