from tree_traversal import *
from binary_search_tree import *


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key

tree1 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
#print(is_bst(tree1))

tree2 = parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
# print(is_bst(tree2))
# display_keys(tree2, '  ')


class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Level 0
#print(jadhesh.username)


tree = BSTNode(jadhesh.username, jadhesh)
# View Level 0
#print(tree.key, tree.value)

# Level 1
tree.left = BSTNode(biraj.username, biraj)
tree.left.parent = tree
tree.right = BSTNode(sonaksh.username, sonaksh)
tree.right.parent = tree
# View Level 1
#print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)

#display_keys(tree, '  ')

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, jadhesh.username, jadhesh)
print(tree.key, tree.value)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

display_keys(tree)

tree2 = insert(None, aakash.username, aakash)
insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)

#display_keys(tree2)

#print(tree_height(tree2))

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

node = find(tree, 'hemanth')
print(node.key, node.value)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
node = find(tree, 'hemanth')
#print(node.value)

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

#print(list_all(tree))

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

print(is_balanced(tree2))


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root

data = [(user.username, user) for user in users]
print(data)

tree = make_balanced_bst(data)
display_keys(tree)

tree3 = None
for username, user in data:
    tree3 = insert(tree3, username, user)

display_keys(tree3)

def balance_bst(node):
    return make_balanced_bst(list_all(node))
tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)
display_keys(tree1)

tree2 = balance_bst(tree1)
display_keys(tree2)


class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)

print(users)

treemap = TreeMap()
print(treemap.root)
treemap.display()

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

print(treemap.root)
treemap.display()

print(treemap['jadhesh'])

print(len(treemap))

treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal
treemap.display()