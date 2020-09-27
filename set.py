emon = {"minhaz","maria", "maria", "uddin","sultana","emon","keya","keya"}
print(emon)

limon = [1,1,1,2,1,2,3,4,5,6,7,8,9]

uniq = set(limon)
print(uniq)

'''fz = frozenset(limon)
print(fz)
fz.add(120)#itcan not add value to list
print(fz)'''
keya = {"Emu","Tuki","Emon","emon"}
z = emon | keya
print("Union",z)
x = emon & keya
print("intersection",x)
c = emon - keya
print(c)
v = emon < keya
print("subset",v)