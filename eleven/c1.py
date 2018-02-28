# 实现方法一非闭包函数实现

# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

# 全局变量
origin = 0


def go(step):
    # 当内部作用域想修改外部作用域的变量时，用global
    global origin
    new_pos = step + origin  # new_pos局部作用域
    origin = new_pos
    return new_pos
print(go(3))
print(go(4))
print(go(5))


# 方法二，闭包函数实现 pons为环境变量
def factory(pons):
    def go(step):
        # 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
        nonlocal pons
        new_pons = pons + step
        pons = new_pons
        return new_pons
    return go

f = factory(origin)
print(f(3))
print(f(5))