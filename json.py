
'''
us= {}

us['emon'] = {
    'name':'Minhaz Uddin Emon',
    'address': '294/5 jigatola Dhaka',
    'phone': 168888888
}
us['keya'] = {
    'name':'Maria Sultana Keya',
    'address': 'Mondol para Durgapur Ashulia Dhaka',
    'phone': 194545454
}
import json
result = json.us
with open("C://Users//EMON//PycharmProjects//pybegin//us.txt","w") as dekho:
    dekho.write(result)

'''
import json

# initialising dictionary
test1 = {"testname": "akshat",
         "test2name": "manjeet",
         "test3name": "nikhil"}

# print original dictionary
print(type(test1))
print("initial dictionary = ", test1)

# convert dictionary into string
# using json.dumps()
result = json.test1

# printing result as string
print("\n", type(result))
print("final string = ", result)