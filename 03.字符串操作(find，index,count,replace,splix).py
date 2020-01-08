string = "abhadfdnjs"
# find :获取对应字符串的下标索引
ret1 = string.find("a")
print(ret1)
ret11 = string.find("ad")
print(ret11)
ret111 = string.find("as")
print("ret111的值：%d" % ret111)

# index
ret2 = string.index("a")
print(ret2)
ret22 = string.index("ad")
print(ret22)
# ret222 = string.index("as")
# print(ret222)
count = string.count("as")
if count > 0:
    index = string.index("as")
    print(index)
else:
    print("没有索引")


# count:计算某个字符串出现的次数
ret3 = string.count("a")
print("a的count数=%d" % ret3)

# replace:字符串替换，如果指定count，则替换不超过count次数--从第一个开始数，到底几个（"被替换的值"， å"替换值"， 次数）
ret4 = string.replace("a", "m")
ret44 = string.replace("d", "k", 1)
print(ret4)
print(ret44)

# split:分割，以str为分割符切片，如果maxsplit有指定值，则仅分割maxsplit个字符串
ret5 = string.split("ab")
print(ret5)
ret55 = string.split("ad")
print(ret55)
