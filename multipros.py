

import time
import multiprocessing
cube_result=[]
def cal_cube(num):
    global cube_result
    for new in num:
        print('Cube' + str(new*new*new))
        cube_result.append(new*new*new)
    print("result" +str(cube_result))
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    pro2 = multiprocessing.Process(target=cal_cube, args=(array,))



    pro2.start()


    pro2.join()

    print('RESULT' + str(cube_result))
    print("done")


