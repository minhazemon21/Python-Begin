
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("user defined exception: ",self.msg)


try:
    raise Accident('crash between two cars')
except Accident as e:
    e.print_exception()