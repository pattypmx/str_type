variable = "asdfgh"
variable2 = "asdfghr"
variable3 = "   asdfg   "

# l just：原字符串左对齐，并使用空格填充长度width
ret1 = variable.ljust(10, "1")
print(ret1)

# r just：原字符串右对齐，并使用空格填充长度width
ret2 = variable.rjust(10, "1")
print(ret2)

# center：原字符串居中，并使用空格填充长度width
ret3 = variable.center(10, "1")
print("位数为偶数时的居中：%s" % ret3)
ret33 = variable2.center(10, "1")
print("位数为奇数时的居中：%s" % ret33)

# l strip：删除字符串左边空格（无论是空格，还是\n,\t--tab键）
ret4 = variable3.lstrip()
print("删除左侧空格：%s" % ret4)
ret44 = variable.lstrip("a")  # 删除左侧第一个字符
print("删除左侧第一个字符a：%s" % ret44)

# r strip：删除字符串右边空格
ret5 = variable3.rstrip()
print("删除右侧空格：%s" % ret5)

# strip：删除字符串两端空格
ret6 = variable3.strip()
print(ret6)
