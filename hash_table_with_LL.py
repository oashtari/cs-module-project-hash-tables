class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



hash_array = [None] * 8 # giving the array size of 8, all initialized to None
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

    # find start of the LL using the index
    # insert into the LL a new hash table entry
    # insert into head or tail, head is preferable
    # search LL for key's existence
    # IF the key already exists in the LL
        # replace the value
    # ELSE 
        # add new hastable entry to the head of the LL

    # NO LONGER NEED THIS
    # # check if something already exists at that index
    # if hash_table[i] != None:
    #     print(f"Collision! Overwriting {repr(hash_table[i])}")

    # store the value in the array at the hashed index
    hash_table[i] = value


def get(key):
    #hash the key and get an index
    i = hash_index(key)

    # get LL at computed index
    # search through LL for the key
        #compare keys until you find the right one

    # if it exists, return value
    # else return None

    # return the value from the array at that index
    return hash_table[i]

def delete(key):
    # hash the key and get an index
    i = hash_index(key)
    # search through LL for the matching key
    # delete that node
    # save and return value of deleted node (or None)

def resize():
    # make a new array that DOUBLEs the current size
    # go through each linked list in the array
        # go through each item and re-hash it
        # insert items into new locations

def shrinking():
    # same as resize but reduce array by half
    

# Load factor = number of items / number of total slots (indexes) (industry standard is 0.7)
# load factor is too high, RESIZE
# if load factor too small, DOWNSIZE (under 0.2)