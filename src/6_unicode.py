# 1、Python使用unicode编码来表示文本
# unicode字符集使用16位或32位的16进制字面量（分别加上前缀\u和\U）
# 或者使用字符的Unicode名称（\N{name}）
a = '\u00c6'
b = '\U0001F60a\u00c6'
c = '\N{cat}'
print(a, b, c)

# 2、创建不可变的bytes对象，表示字符串的编码值,
# 字面量表示法仅支持ASCII编码的字符，意味着中文必须使用编码值
d = b'Hello world! \xe5\x87\x9b '
print(d.decode())  # Hello world! 凛

# 3、 encode和decode可指定字符集对字符串进行编码,默认的编码和解码字符是utf-8，
# 因为utf-8兼容ASCII编码，所以对ASCII编码进行解码可不指定
# 使用ASCII编码字符串，仅支持128个ASCII字符，中文会报错，
# 可指定编码规则，默认是script,还有ignore，replace(使用？代替)，backslashreplace(使用\\),xmlcharrefreplace（使用&#）
e = "hello".encode("ASCII")
h = 'hello 黄益凛'.encode("ASCII", 'replace')
f = 'hello 凛'.encode('utf-8')
g = 'hello 凛'.encode('utf-32')
print(e, ':', e.decode())  # b'hello' : hello
print(h, ':', h.decode())  # b'hello' : hello
print(f, ":", f.decode())  # b'hello \xe5\x87\x9b' : hello 凛
print(f, ':', g.decode('utf-32'))  # b'hello \xe5\x87\x9b' : hello 凛

# 相比encode和decode，bytes和str也能实现该编码译码功能，并且更常用,
# bytes和str需要指定编码
a1 = bytes('黄益凛', 'utf-8')
b1 = bytes('黄益凛', 'utf-32')
c1 = bytes('hello', 'ASCII')
print('*********************')
print(a1, ':', str(a1, 'utf-8'))  # b'\xe9\xbb\x84\xe7\x9b\x8a\xe5\x87\x9b' : 黄益凛
print(b1, ':', str(b1, 'utf-32'))  # b'\xff\xfe\x00\x00\xc4\x9e\x00\x00\xcav\x00\x00\xdbQ\x00\x00' : 黄益凛
print(c1, ':', str(c1, 'ascii'))  # b'hello' : hello
