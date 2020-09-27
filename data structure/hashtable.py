stock_prices = []
with open("strock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
print(stock_prices)
for element in stock_prices:
    if element[0] == 'March 9':
        print(element[1])

stock_prices = {}
with open("strock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print(stock_prices)
print(stock_prices['March 9'])

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100
a = ord('z')
print(a)
b= get_hash('March 6')
print(b)


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['march 6'] = 310
t["march 1"] = 420
t["dec 1"] = 321
t["jan 1"] = 323
t["feb 1"] = 100

print(t)

print(t.arr)
del t['march 6']
print(t.arr)
