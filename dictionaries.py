
we = {
    "emon": 'Minhaz Uddin Emon',
    "keya": 'Maria Sultana Keya',
    "mintom": 'I Love U'
}


#print(we.get("emon","Name this not match in file"))
for key,value in we.items():
    print("Name:",key,"Full Name:",value)
#del we["mintom"]
print(we)
print("emon" in we)
print("emu" in we)
print(we)
if 'mintom' in we:
    del we['mintom']
print(we)
#we.clear()
we["bhjguygf"]= "jhftudtfg"
print(we)