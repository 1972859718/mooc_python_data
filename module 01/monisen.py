#寻找第n个默尼森数
def prime(num):
    i = 2
    flag = 1
    while i*i < num:
        if num % i == 0:
            flag = 0
            break
        i += 1
    return flag
def monisen(no):
    p = m = 2
    count = 0
    while True:
        if count < no:
            if prime(p):
                m = 2 ** p - 1
                if prime(m):
                    count += 1
        else:
            return m
        p += 1
print(monisen(int(input())))
