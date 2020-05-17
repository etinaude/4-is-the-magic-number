import pickle
import time
first = {
    0: 4,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
}

second = {
    0: 0,
    1: None,
    2: 7,
    3: 7,
    4: 6,
    5: 6,
    6: 6,
    7: 9,
    8: 7,
    9: 7,
}

weird = {
    0: 3,
    1: 6,
    2: 6,
    3: 8,
    4: 7,
    5: 8,
    6: 7,
    7: 9,
    8: 8,
    9: 8
}

longer = {
    4: 9,       # thousand
    7: 8,       # million
    10: 8,      # billion
    13: 9,      # trillion
    16: 12,     # quadrillion
}


class O:
    def __init__(self, route, searched, big):
        self.route = route
        self.searched = searched
        self.big = big


def odd(num):
    return weird[num]


def group(num):
    working = 0
    if int(num[-2:]) > 9 and int(num[-2:]) < 20:
        num = odd(int(num[-1]))
        working = num
    else:
        working += first[int(str(num)[0])]
        if len(str(num)) > 1:
            working += second[int(str(num)[-2])]
        if len(str(num)) > 2:
            if str(num)[-3] != "0":
                working += first[int(str(num)[-3])]
                working += 8
    return working


upper = 1400000
try:
    pass
    with open('data', 'rb') as fp:
        o = pickle.load(fp)
    if upper <= o.searched:
        print("BIG", o.big[0], o.big[1], o.big[2])
    exit()
except:
    o = O({0: [1]}, 0, [0, 0, 0])

# '''
start = time.perf_counter()
for i in range(o.searched, upper):
    num = str(i)
    step = []
    count = 0
    if int(num) in o.route:
        count = len(o.route[int(num)])+count
        step.extend(o.route[int(num)])
        if count > o.big[0]:
            o.big[0] = count
            o.big[1] = i
            o.big[2] = step
        continue
    while int(num) != 4:
        if int(num) in o.route:
            count = len(o.route[int(num)])+count
            step.extend(o.route[int(num)])
            break
        working = 0
        working = group(str(num))
        if len(num) > 3:
            working += longer[4]
            num = num[:-3]
            working += group(str(num))
        if len(num) > 3:
            working += longer[7]
            num = num[:-3]
            working += group(str(num))
        if len(num) > 3:
            working += longer[10]
            num = num[:-3]
            working += group(str(num))
        if len(num) > 3:
            working += longer[13]
            num = num[:-3]
            working += group(str(num))
        if len(num) > 3:
            working += longer[16]
            num = num[:-3]
            working += group(str(num))
        num = str(working)
        step.append(working)
        count += 1
    o.route[i] = step
    if count > o.big[0]:
        o.big[0] = count
        o.big[1] = i
        o.big[2] = step
    print(i, ":", count)
    # '''
print("BIG", o.big[0], o.big[1], o.big[2])
print(time.perf_counter()-start)
p = O(o.route, upper, o.big)
with open('data', 'wb') as fp:
    pickle.dump(p, fp)
