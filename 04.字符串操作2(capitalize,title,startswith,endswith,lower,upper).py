variable = "abfssssff"
variable2 = "a b f g h "
variable3 = "afdfBFBdfgd"

# capitalize:把字符串的第一个字符变为大写
ret1 = variable.capitalize()
print(ret1)

# title：把字符串的每个单词变成大写（一个字符串用空格隔开，即每个都变大写，不然只变第一个）
ret2 = variable.title()
print(ret2)
ret22 = variable2.title()
print(ret22)

# startswith:检查是否以xxx开头，是返回True，否则返回False
ret3 = variable.startswith("abf")
print(ret3)
ret33 = variable.startswith("bbb")
print(ret33)

# endswith:检查是否以xxx结尾，是返回True，否则返回False
ret4 = variable.endswith("sff")
print(ret4)
ret44 = variable.endswith("ggg")
print(ret44)

# lower：大写--->小写，转换字符串中的所有大写字符为小写
ret5 = variable3.lower()
print(ret5)

# upper：小写--->大写，转换字符串中的所有小写字符为大写
ret6 = variable3.upper()
print(ret6)