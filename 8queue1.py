import numpy as np


count = 0
def eightQueen(plate, total_num):
    if plate is None:
        return
    if total_num <= 0:
        print("total num < 0")
        return None
    index_edge = plate.shape[0]
    col_edge = plate.shape[1]
    if index_edge <= 0 or col_edge <= 0:
        print("edge error")
        return None

    num = 0

    for index in list(range(0, index_edge - total_num + 1)):
        for col in list(range(col_edge)):
            flag = is_ok(plate, index, col)
            if flag == 1 :
                plate[index][col] = 1

                put_queen(plate, num + 1, index_edge, col_edge)
                #print(plate)
                clear(plate, index, col)
    global count
    print(count)



def put_queen(plate, num, index_edge, col_edge):
    if plate is None:
        return
    if num >= 8:
        print("num > 8")
        print(plate)
        global count
        count += 1


        with open("log.txt", 'a') as f:
            f.write(str(plate))
            f.write('\n')
        return None

    for index in list(range(num, index_edge)):
        for col in list(range(col_edge)):
            flag = is_ok(plate, index, col)
            if flag == 1:
                plate[index][col] = 1

                #print(plate)
                put_queen(plate,num + 1, index_edge, col_edge)
                #print("put queue")
                #print(plate)
                #print("clear begin")
                clear(plate,index,col)

    pass

def is_ok(plate, index, col):
    index_edge = plate.shape[0]
    col_edge = plate.shape[1]
    if index_edge <= 0 or col_edge <= 0:
        print("edge error")
        return None
    flag = 1
    for i in list(range(index_edge)):
        if plate[i][col] == 1:
            flag = 0
            return flag

    for j in list(range(col_edge)):
        if plate[index][j] == 1:
            flag = 0
            return flag

    i = index - 1
    j = col - 1
    while (i >= 0 and j >= 0):
        if plate[i][j] == 1:
            flag = 0
            return flag
        i -= 1
        j -= 1

    i = index + 1
    j = col + 1
    while i < index_edge and j < col_edge:
        if plate[i][j] == 1:
            flag = 0
            return flag
        i += 1
        j += 1
    i = index - 1
    j = col + 1
    while (i >= 0 and j < col_edge):
        if plate[i][j] == 1:
            flag = 0
            return flag
        i -= 1
        j += 1

    i = index + 1
    j = col - 1
    while i < index_edge and j >= 0:
        if plate[i][j] == 1:
            flag = 0
            return flag
        i += 1
        j -= 1

    return flag

def clear(plate, index, col):
    index_edge = plate.shape[0]
    col_edge = plate.shape[1]
    if index_edge <= 0 or col_edge <= 0:
        print("edge error")
        return None
    plate[index][col] = 0
    #print(plate)

plate = np.zeros((8,8))
#print("clear")
#print(plate)

eightQueen(plate, 8)