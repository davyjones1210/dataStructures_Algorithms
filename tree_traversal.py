from binary_search_tree import parse_tuple

from binary_search_tree import display_keys


def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
display_keys(tree, '  ')

print(traverse_in_order(tree))

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

#print(tree_height(tree))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

#print(tree_size(tree))