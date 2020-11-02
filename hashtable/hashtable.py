class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.load = 0
        self.min_size = capacity * 2

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

        self.key = key
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        for byte_of_data in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(byte_of_data)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        key_bytes = key.encode()
        hash = 5381
        for key_byte in key_bytes:
            hash = hash * 33 + key_byte
            hash &= 0xffffffff
        return hash

    # def djb2(self, key):
    #     """
    #     DJB2 32-bit hash function
    #     Implement this, and/or FNV-1.
    #     """
    #     key_bytes = key.encode()
    #     hash = 5381
    #     for k_byte in key_bytes:
    #         hash = hash * 33 + k_byte
    #         hash &= 0xffffffff
    #     return hash


    #         # key_bytes = key.encode()
    #         # hash = 5381
    #         # for k_byte in key_bytes:
    #         #     hash = hash * 33 + k_byte
    #         #     hash &= 0xffffffff
    #         # return hash


    #     # EXTRA HASH
    # def _hash(self,key):
    #     hash = 51020
    #     for x in key:
    #         hash = (hash * 33) + ord(x)
    #     return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
        # return self._hash(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)
        print('the key index:', key_index)
        print('the new line', value)

        # if self.storage[key_index] != None:
        #     print(f"Collision at {repr(self.storage[key_index])}" )
        self.storage[key_index] = value
        print('whole storage', self.storage)
        # self.storage[key_index] = HashTableEntry(key,value)

    # def put(self, key, value):
       
    #     key_index = self.hash_index(key)
    #     # cur_node = self.storage[key_index]


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)

        if self.storage[key_index] == None:
            print(f"did not find such a key")
        else:
            deleted_key = self.storage[key_index]
            self.storage[key_index] = None

            return deleted_key



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)
        print('GET index:', key_index)
        print('GET return', self.storage[key_index])
        return self.storage[key_index]



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


def hash_fn(str):
    print(str)
    encoded_string = str.encode()
    print(encoded_string)
    for char in str:
        print(char)

    result = 0
    for byte_char in encoded_string:
        print(byte_char)
        result += byte_char
    return result 






