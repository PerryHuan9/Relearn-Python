# 集合set的概念
def test_set():
    '''
    set集合，不能保存相同的元素，无序，可利用set类传入可迭代对象
    集合中只能包含不可变（可散列）的值，因此不能包含集合，
    但可包含frozenset，它表示不可变的集合
    :return:
    '''
    s = set([12, 34, 54, 34, 434, 23, 1, 2, 34, 4])
    print(s)
    s1 = {1, 1, 2, 3, 4, 3, 4, 7, 5, 3, 2, 2, 3}
    print(s1)  # {1,2,3,4,5,7} 去重
    # union方法或按位或|求并集
    print(s.union(s1))
    print(s | s1)
    # 按位与求交集,或intersection方法
    c = s & s1
    print(c)  # {1,2,4}
    print(s.intersection(s1))
    # issubset方法判断是否为子集或父集
    print(c.issubset(s))  # True
    print(s.issuperset(c))  # True
    print(c <= s1)  # True
    print(c >= s)  # False
    # difference或‘-’号去掉本集合中的另一个集合的元素
    print(s.difference(s1))
    print(s1 - s)
    # symmetric_deifference和^求差集
    print(s.symmetric_difference(s1))
    print(s1 ^ s)
    # copy方法进行复制
    print(s.copy())
    print(s.copy() is s)
    # add和remove方法
    s.add(888)
    print(s)
    s.remove(888)
    print(s)
    # frozenset不可变的集合
    a = set()
    b = frozenset()
    a.add(b)
    print(a)


# test_set()

def test_heap():
    '''
    堆是一种优先队列，优先队列能够让你以任意的顺序添加对象，
    并随时找出并删除最小的元素，相比列表的min方法，其效率高得多,
    堆中的数据顺序必须保证：位置i处的元素总是大于位置i//2处的元素
    （反过来就是小于位置2*i和2*i+1处的特征），这是堆算法的基础，成为堆特征

    '''
    import heapq
    from random import shuffle

    data = list(range(10))
    shuffle(data)
    print(data)
    heap = []
    for n in data:
        heapq.heappush(heap, n)
    print(heap)
    heapq.heappush(heap, 0.5)
    print(heap)
    # 弹出最小的数
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heap)
    # heapify将列表转化为堆
    h = [12, 34, 45, 67, 7, 89, 34]
    heapq.heapify(h)
    print(h)
    # heapreplace将最小的数弹出来，并压入一个新的数
    heapq.heapreplace(h, 12)
    print(h)
    # nlargest(n,iter)和nsmallest(n,iter)分别用于从可迭代对象中找出最大和最小的n个元素
    lst = [12, 23, 343, 34, 445, 12, 1, 23, 54, 5, 5, 6, 56423, 4232]
    print(heapq.nlargest(4, lst))
    print(heapq.nsmallest(5, lst))


# test_heap()

def test_deque():
    '''
    双端队列，在需要按添加顺序来删除元素时非常有用，其为于collection集合，
    可以通过序列进行创建

    '''
    from collections import deque
    q = deque(range(7))
    q.append(23)
    q.append(2)
    print(q)
    q.appendleft(888)
    print(q)
    print(q.pop())
    print(q.popleft())
    print(q)
    # 旋转队列，将后面n个元素移至最前
    q.rotate(3)
    print(q)
    q.rotate(4)
    print(q)
    # 还有extend和extendleft(按相反顺序出现在队列中)方法
    q.extend(range(66, 70))
    print(q)
    q.extendleft(range(66, 70))
    print(q)


# test_deque()
