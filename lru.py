class LRUCache:
    def __init__(self, size):
        self.totalSize = size
        self.cache = []
        print(self.cache)

    def put(self, key, value):
        #  check for duplicate key
        for i in self.cache:
            if i[0] == key:
                # index contain the index of the list element that is to be deleted
                index = self.cache.index(i)
                del self.cache[index]
                self.cache.append([key, value])
                #print(self.cache)
                # print(len(self.cache))
                return 0

        # append when length is smaller that the size
        if len(self.cache) < self.totalSize:
            self.cache.append([key, value])
            #print(self.cache)
            # print(len(self.cache))
            return 1
        else:
            # pop 1st element and append the given in the last
            del self.cache[0]
            self.cache.append([key, value])
            #print(self.cache)
            # print(len(self.cache))
            return 1

    def get(self, key):
        status = False
        for i in self.cache:
            if i[0] == key:
                temp = [i[0], i[1]]
                # index contain the index of the list element that is to be deleted
                index = self.cache.index(i)
                del self.cache[index]
                self.cache.append(temp)
                #print(self.cache)
                # print(len(self.cache))
                status = True
                return temp[1]
        if status == False:
            return -1


a = LRUCache(2)
a.put(1,1)
a.put(2,2)
print(f"get 1 ka result: {a.get(1)}")
a.put(3,3)
print(f"get 2 ka result: {a.get(2)}")
a.put(4,4)
print(f"get 1 ka result: {a.get(1)}")
print(f"get 3 ka result: {a.get(3)}")
print(f"get 4 ka result: {a.get(4)}")




# Create an LRU cache with a size of 50
lru_cache = LRUCache(50)

# Fill the cache with keys 0-49
miss=0
count=0
for i in range(50):
    count+=1
    miss+=lru_cache.put(i,i)
    

# Retrieve the odd-numbered key values
for i in range(1, 100, 2):
    count+=1
    value = lru_cache.get(i)
    if value!=-1:
        print(f"Key: {i}, Value: {value}")
    else:
        miss+=1

# Fill the cache with prime number keys 0-100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for prime in primes:
    count+=1
    miss+=lru_cache.put(prime, prime)

# Total miss rate
miss_rate = (miss / count)*100
print(f"Final Miss Rate: {miss_rate}0 %")
