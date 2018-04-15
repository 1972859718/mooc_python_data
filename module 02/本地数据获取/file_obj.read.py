with open('firstpro.txt') as f:
    p1 = f.read(5)  #读五个字节，返回一个字符串
    p2 = f.read()   #读文件知道文件结尾，返回一个字符串
print(p1, p2)
