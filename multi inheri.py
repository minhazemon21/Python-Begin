

class Father():
    def gardening(self):
        print("I enjoy gardening")
class Mother():
    def cooking(self):
        print("I love cooking")
class Child(Father,Mother):
    def sports(self):
        #Father.skills(self)
        print("I enjoy Sports")

c = Child()
c.gardening()
c.cooking()
c.sports()