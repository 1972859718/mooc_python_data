f = open("firstpro.txt", 'w')
f.write('hello,world!')
f.close()
#with方法，可处理异常，且会自动关闭文件
with open('secondpro.txt','w') as f:
    f.write('hello moon!')
