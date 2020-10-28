hash_fn("gunner")
print(hash_fn('gunner'))



hash_array = [None] * 8 # giving the array size of 8
# lets map the result of hash_fn to an index in some array
# we can use modulo to bind the number from hash_fn to 0 -> lenght of the array

# THIS GETS THE HASH
def my_hash(s):
    #take every character in the string, and convert character to a number
    # convert each character into UTF-8
    string_utf = s.encode()

    total = 0;
    for char in string_utf:
        total += char
        total &= 0xffffffff # limit total to 32 bits
    return total

# THIS GETS THE INDEX
def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)

def put(key, val):
    #hash the key and get index
    i = hash_index(key)
    # check if something already exists at that index
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}")
    # store the value in the array at the hashed index
    hash_table[i] = value


def get(key):
    #hash the key and get an index
    i = hash_index(key)
    # return the value from the array at that index
    return hash_table[i]


# store Gunner in inside hash_array
hash_value = hash_fn("gunner") # 609
index = hash_value % len(hash_array)
print(index)
hash_array[index] = ('gunner','gunner is brownish')
print(hash_array)

# store Ory in inside hash_array
hash_value = hash_fn("gunner") # 530
index = hash_value % len(hash_array)
print(index)
hash_array[index] = ('ory', 'ory is greyish')
print(hash_array)

# Look up Gunner in hash_array
# Get index value of Gunner

hash_value = hash_fn("gunner") # 609 #O(n) but N == length of string
index = hash_value % len(hash_array) #O(1)

print(hash_array[index])

# Hash function + an array  == Hash_Table


# To insert a key and value to this hash_table
# - hash the key to convert it to a number
# - use MOD to find index within the underlying array
# - use this new index to find the value in the array

def insert_to_hash_table(key, value):
    hash_value = hash_fn(key)
    index = hash_value % len(hash_array) # convert the number into a new number between 0 - len(array)
    hash_array[index] = (key,value)

# To retrive a value given a specific key from a hash_table
# - hash the key to convert it to a number
# - use MOD to find index within the underlying array
# - use this new index to find the value in the array

def get_from_hash_table(key):
    hash_value = hash_fn(key)
    index = hash_value % len(hash_array) # convert the number into a new number between 0 - len(array)
    return hash_array[index]

