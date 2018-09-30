# unicode字符集
# unicode字符集使用16位或32位的16进制字面量（分别加上前缀\u和\U）
# 或者使用字符的Unicode名称（\N{name}）

a = '\u00c6'
b = '\U0001F60a'
c = '\N{cat}'
print(a, b, c)
