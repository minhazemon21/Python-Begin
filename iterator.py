
class RemoteControl():
    def __init__(self):
        self.story = ["hey","tuki","i","miss","u"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.story):
            raise StopIteration
        return self.story[self.index]
ogo = RemoteControl()
itr = iter(ogo)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

'''
a = ["hey","tuki","i","miss","u"]
for i in a:
    print(i)
print(dir(a))
itr=iter(a)
print(itr)
b=next(itr)
print(b)
b=next(itr)
print(b)
'''