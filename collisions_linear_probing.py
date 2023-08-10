from hash_tables import *


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)


    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv == None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE

# New key 'listen' should return expected index
print(get_valid_index(data_list2, 'listen'))

# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)

# Colliding key 'silent' should return next index
print(get_valid_index(data_list2, 'silent'))