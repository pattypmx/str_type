
# 切片语法：[起始：结束：步长]
mm = "abcdef"
# 读取abc
ret1 = mm[:3]  # 从头部开始，0可以省略[:结束]==mm[0:3]
print(ret1)
# 读取ace
ret2 = mm[:5:2]  # 步长：默认步长为1，，2个步长即为2
print(ret2)
# 读取bd
ret3 = mm[1:4:2]
print(ret3)
# 读取fdb
ret4 = mm[::-2]  # 方向取值，步长默认-1
print(ret4)
# 读取fd
ret5 = mm[-1:-4:-2]
print(ret5)




