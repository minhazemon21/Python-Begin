

f = open("C:\\Users\\EMON\\PycharmProjects\\pybegin\\new.txt","r")
'''
f.write("\nI miss u tuki")
f.close()
'''


#print(f.read())
f_out = open("C:\\Users\\EMON\\PycharmProjects\\pybegin\\new1.txt","w")
for line in f:
    tokens = line.split(' ')
    f_out.write("WordCounter: "+str(len(tokens))+line)
    print(len(tokens))
f.close()
f_out.close()
