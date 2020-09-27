import time
import threading

def cal_square(num):
    print("Sqare number calculate")
    for new in num:
        time.sleep(1)
        print('square: ', new * new)


def cal_cube(num):
    print("Cube number calculate")
    for new in num:
        time.sleep(1)
        print('cube: ', new * new * new)


array = [1, 2, 3, 4, 5, 6]
tm = time.time()
'''
cal_square(array)
cal_cube(array)
'''
td1 = threading.Thread(target=cal_square,args=(array,))
td2 = threading.Thread(target=cal_cube,args=(array,))

td1.start()
td2.start()

td1.join()
td2.join()

print("Done my job: ", time.time()-tm)
print("Hmm.. I am done with all my work now")