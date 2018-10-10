# 正则表达式

def test_1():
    '''
    1、通配符
        .据点与任何非换行符匹配
    2、对特殊字符转义
        对诸如\,.,?等符号都需要在其前面加反斜杠进行转义，
        如要匹配python.org需要使用规则python\\.org
    3、字符集
        要匹配指定范围的单个字符可用字符集，
        如[pj]ython匹配python和jython
        [a-zA-Z0-9]与大小写字母数字匹配
        在字符集中还可以使用^排除指定字符，如[^abc]匹配任意非a,b和c的字符
    4、二选一和子模式
        在需要进行二选一时，可以使用管道字符|
        如python|perl匹配python或perl
        可将部分值放在圆括号里构成子模式，如p(ython|erl)匹配python或perl

    5、可选模式和重复模式
        ?问号表示单个字符或子模式最多可重复1次
        *星号表示单个字符或子模式可重复任意次
        +加号表示单个字符或子模式最少重复1次
        {m,n}表示单个字符或子模式重复m-n次
    6、字符串的开头和结尾
        ^表示以其之后的单个字符或子模式开头将会被匹配,如^python 匹配以p开头的字符串
        $号表示以其之前的单个字符或子模式结尾，\.pdf$匹配以.pdf结尾的字符串

    Python中提供了re模块用于正则表达式
    '''
    import re
    # compile(pattern) 将正则表达式字符串转化为模式对象，以提高匹配效率
    pattern = re.compile('.ython')
    # match方法在字符串开头匹配模式
    print(pattern.match('aython'))
    # 可以不转化，直接传入正则字符串
    print(re.match('.ython', 'aython'))
    # search方法在字符串中搜索，如果找到返回等价于True的MatchObject
    string = 'you can use IronPython do something'
    reg = '[CPJ(Iron)]'
    if re.search(reg, string):
        print("'{}'".format(string), ' has ', reg, ' matching string')
    # split以指定为正则切割字符串，返回子字符串列表
    print([e for e in re.split('[, ]', 'alpha, beta  ,,,,,gama   delta') if e])
    # 切割模式中包含圆括号,下式将以oo为切割位置，并且在切割得到的子串列表中间插入o
    print(re.split('o(o)', 'foobaroobar'))  # ['f', 'o', 'bar', 'o', 'bar']
    # 另外可以指定最后的可选参数，最大切割次数

    # findall返回一个列表，其中所有子串都以给定模式匹配
    # 下式查找字符串包含的所有单词
    text = '"Hm... Err -- are you sure?"he said ,sounding insecure'
    print(re.findall('[a-zA-Z]+', text))
    # 下式查找所有的标点符号
    print(re.findall(r'[.?\-",]+', text))

    # sub替换匹配到的子字符串
    print(re.sub('{name}', 'perry', 'Dear {name}...'))

    # escape方法将字符串中所有可能被视为正则表达式的字符转义
    print(re.escape('www.baidu.com'))  # www\.baidu\.com
    print(re.escape(' But where is you?'))  # \ But\ where\ is\ you\?

    # 编组
    pat = 'There (was a (wee) (computer) who (lived in Fyfe))'
    string = 'There was a wee computer who lived in Fyfe'
    g = re.match(pat, string)
    print(g.group(0))  # There was a wee computer who lived in Fyfe
    print(g.group(1))  # was a wee computer who lived in Fyfe
    print(g.group(2))  # wee
    print(g.group(3))  # computer
    print(g.group(4))  # lived in Fyfe
    # start end 和span方法返回指定组在字符串中的开始，结束索引加1，和索引范围
    print(g.start(1))  # 6
    print(g.end(1))  # 42
    print(g.span(1))  # (6,42)

    pat = r'www\.(.+)\.com$'
    m = re.match(pat, 'www.baidu.com')
    print(m.group(0))
    print(m.group(1))

    # 替换，正则表达式中形如\\n将被替换为与模式中编组n匹配的字符串
    # 使用VERBOSE标志可以逐句解释正则表达式
    emphasis_pattern = re.compile(r'''
    \*         #匹配星号
    ([^\*]+)   #匹配多个非星号字符
    \*     #匹配星号
    ''', re.VERBOSE)
    # 上式相当于'\*([^\*]+)\*'

    print(re.sub(emphasis_pattern, r'<em>\1</em>', 'hello, *word*'))


test_1()
