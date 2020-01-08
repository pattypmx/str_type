variable = "asdfghjdfg"

# rfind：查找所需字符串右侧的第一个索引---find为左侧开始查找
ret1 = variable.rfind("f")
print(ret1)

# rindex:同rfind
ret2 = variable.rindex("g")
print(ret2)

# partition：把str分割成三部分，str钱，str，str后，分割成元组tuple
ret3 = variable.partition("df")
print(ret3)

# rpartition：：右边开始分割
ret4 = variable.rpartition("df")
print(ret4)

