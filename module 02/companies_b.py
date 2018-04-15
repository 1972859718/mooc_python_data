#companies_b.py
s = 'Tencent Technology Company Limited'
with open('companies.txt','a+') as f:
    f.writelines('\n')
    f.writelines(s)
#移动文件指针，f.seek(offtet, whence = 0),whence可选，0表示文件头部，
#1表示当前位置，2表示文件结尾,偏移offset字节
    f.seek(0)
    cNames = f.readlines()
print(cNames)
