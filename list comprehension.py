num = [1,2,3,4,4,5,6,7]
even=[]
for i in num:
    if i%2==0:
        even.append(i)
print(even)

#even=[i for i in num if i%2==0]
#print(even)
sqr = [i*i for i in num]
print(sqr)

s = set(num)
print(s)

cities = ["Dhanmondi","silicon vally","Barcelona"]
countries = ["Bangladesh","USA","Spain"]
z=zip(cities,countries)
print(z)
for keya in z:
    print(keya)
emon = {city:country for city,country in zip(cities,countries)}
print(emon)