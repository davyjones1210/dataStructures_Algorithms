phone_numbers = {
  'Aakash' : '9489484949',
  'Hemanth' : '9595949494',
  'Siddhant' : '9231325312'
}

#print(phone_numbers)

#print(phone_numbers['Aakash'])

# Add a new value
phone_numbers['Vishal'] = '8787878787'
# Update existing value
phone_numbers['Aakash'] = '7878787878'
# View the updated dictionary
#print(phone_numbers)

# for name in phone_numbers:
#     print('Name:', name, ', Phone Number:', phone_numbers[name])


class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass

    def find(self, key):
        """Find the value associated with a key"""
        pass

    def update(self, key, value):
        """Change the value associated with a key"""
        pass

    def list_all(self):
        """List all the keys"""
        pass

MAX_HASH_TABLE_SIZE = 4096

# List of size MAX_HASH_TABLE_SIZE with all values None
data_list = [None]*MAX_HASH_TABLE_SIZE

#print(len(data_list))
#print(data_list[99] == None)


def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number

        # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

#print(get_index(data_list, ''))
#print(ord('x'))
#print(get_index(data_list, 'Aakash'))
#print(ord('A')+ord('a')+ord('k')+ord('a')+ord('s')+ord('h'))
#print(get_index(data_list, 'Don O Leary'))

data_list2 = [None] *48
#print(get_index(data_list2, 'Aakash'))

key, value = 'Aakash', '7878787878'
idx = get_index(data_list, key)
#print(idx)

data_list[idx] = (key, value)
#print(data_list[idx])
data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '9595949494')
#print(data_list[get_index(data_list, 'Hemanth')])

idx = get_index(data_list, 'Aakash')
#print(idx)

key, value = data_list[idx]
#print(value)

pairs = [kv[0] for kv in data_list if kv is not None]
# print(pairs)

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]


basic_table = BasicHashTable(max_size=1024)
#print(len(basic_table.data_list))

# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
#print(basic_table.find('Hemanth'))
#print(basic_table.find('Aakash'))

# Update a value
basic_table.update('Aakash', '7777777777')

# Check the updated value
#print(basic_table.find('Aakash'))

# Get the list of keys
#print(basic_table.list_all())


