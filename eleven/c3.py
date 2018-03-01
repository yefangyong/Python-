# 列表推导式
# 元组（）
# 字典 dict()
# 列表都可以被推导
a = [1,2,3,4,5,6,7]

def go(x):
    if x >3:
        return True
    else:
        return False

# 用map lambda filter实现
b = map(lambda x:x*x,filter(go,a))
print(list(b))

# 用列表推导式
c = [i**2 for i in a if i> 3]
print(c)

# 字典列表推导式
student = {
    'yfyjsz':12,
    'hjy':45
}
# 元组不可变，得到的是一个可遍历的对象，推荐使用列表
s = [key for key,value in student.items()]
print(s)