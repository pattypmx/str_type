a = "qwertyu"
b = "123fdgd"
c = "123455"
d = "    "

# rsplitlines:按照指定的内容分隔，返回一个包含各行作为一个元素的列表
ret1 = a.rpartition("y")
print(ret1)

# isalpha:判断str是否都是字母，如果str都是字母，则返回True，否则返回False
ret2 = a.isalpha()
print(ret2)
ret22 = b.isalpha()
print(ret22)

# isdigit:判断str是否都是数字，如果str都是数字，则返回True，否则返回False
ret3 = a.isdigit()
print(ret3)
ret33 = c.isdigit()
print(ret33)

# isalnum:判断str是否都是数字或字母，如果是则返回True，否则返回False
ret4 = b.isalnum()
print(ret4)
ret44 = d.isalnum()
print(ret44)

# isspace：判断str是否只包含空格，如果是则返回True，否则返回False
ret5 = a.isspace()
print(ret5)
ret55 = d.isspace()
print(ret55)

# join：以指定字符串作为分隔符，将所有的元素(的字符串表示)合并为一个新的字符串
my_tp = ["h", "e", "llo"]
ret6 = "".join(my_tp)
print(ret6)
ret66 = "5".join(my_tp)
print(ret66)

# 打印出dcgh
my_tp2 = "  dc  gh "
ret7 = my_tp2.replace(" ", '')
print(ret7)

ret77 = my_tp2.split()
ret777 = "".join(ret77)
print(ret777)
