#Given a list of unique numbers, arranged in increasing order, rotated unknown number of times
#write a function to deter min. number of times original list was sorted
#input = 'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], output = 3

def count_rotations(nums):
    pass

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

nums0 = test['input']['nums']
output0 = test['input']['nums']
result0 = count_rotations(nums0)

result0, result0 == output0
from jovian.pythondsa import evaluate_test_case
evaluate_test_case(count_rotations, test)
