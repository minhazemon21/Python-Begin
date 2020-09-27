


emon = input("Enter Number 1: ")

keya = input("Enter Number 2: ")
try:
    tuki = int(emon) / int(keya)
except ZeroDivisionError as emu:
    print('Division by zero exception')
    tuki = None
except TypeError as emu:
    print('Type Error Exception')
    tuki = None
print("Division Is: ",tuki)