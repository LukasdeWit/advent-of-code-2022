
def one():
    data = open("day 6 data.txt").readline()
    for i in range(len(data)):
        lst = []
        for k in range(4):
            if not data[i + k] in lst:
                lst.append(data[i + k])
                if len(lst) == 4:
                    return i + 4
    return -1



def two():
    data = open("day 6 data.txt").readline()
    for i in range(len(data)):
        lst = []
        for k in range(14):
            if not data[i + k] in lst:
                lst.append(data[i + k])
                if len(lst) == 14:
                    return i + 14
    return -1

    
print(one())
print(two())
