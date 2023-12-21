import turtle as t  # 引入turtle模块，并将其重命名为t
from turtle import *  # 从turtle模块中导入所有函数，可以直接使用turtle的函式，不需要加前缀
import random as r  # 引入random模块，并将其重命名为r


def set_initial_state(tree_height):
    """设置初始状态"""
    speed(0)  # 设置画笔的速度为0，最快，也可以设定为 fastest
    screensize(bg='black')  # 设置屏幕的大小，背景为黑色
    left(90)  # 画笔向左旋转90度
    forward(3 * tree_height)  # 按照单位长度n的3倍长度向前移动
    color("orange", "yellow")  # 设置画笔的颜色，画线（轮廓）的颜色为橙色，填充的颜色为黄色


def draw_star(tree_height):
    """画一个五角星"""
    begin_fill()  # 开始填充颜色
    left(126)  # 画笔向左旋转126度
    for i in range(5):  # 循环5次，画五角星的五个边
        forward(tree_height / 5)  # 向前移动长度为n的五分之一
        right(144)  # 右转144度，画五角星的内角
        forward(tree_height / 5)  # 向前移动长度为n的五分之一
        left(72)  # 画笔向左旋转72度，画五角星的外角
    end_fill()  # 填充颜色完毕
    right(126)  # 画笔向右旋转126度


def drawlight():
    """在树干上随机画灯"""
    # 30个点内有一个是彩灯，如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
    # 改变颜色，画一个彩点
    if r.randint(0, 30) == 0:
        color('tomato')  # 定义第一种颜色
        circle(6)  # 定义彩灯大小
    elif r.randint(0, 30) == 1:
        color('orange')  # 定义第二种颜色
        circle(3)  # 定义彩灯大小
    else:
        color('dark green')  # 其余的颜色为深绿色，代表树枝


def draw_tree(tree_height):
    """画树的主体部分"""
    color("dark green")  # 设置画笔颜色为深绿色
    backward(tree_height * 4.8)  # 向后移动单位长度n的4.8倍，为了画树干


def tree(d, s):
    """以递归的方式画树的枝干"""
    if d <= 0:
        return
    forward(s)  # 向前移动
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    # 同时调用小彩灯的方法，也就是画完一个树枝后画一个小彩灯
    drawlight()
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


def draw_decorations():
    """画树下的装饰品"""
    for i in range(200):
        a = 200 - 400 * r.random()
        b = 10 - 20 * r.random()
        up()  # 提笔
        forward(b)
        left(90)
        forward(a)
        down()  # 落笔
        if r.randint(0, 1) == 0:
            color('tomato')
        else:
            color('wheat')
        circle(2)
        up()
        backward(a)
        right(90)
        backward(b)


def write_text(greeting):
    """
    在画布中央书写圣诞祝福
    参数: greeting -- 用户输入的圣诞祝福字符串
    """
    # 根据用户的输入长度决定使用的字体大小。用户输入的字符越多，字体越小
    font_size = 40 - len(greeting)
    # 如果用户没有输入祝福，则会显示默认祝福语
    if not greeting:
        greeting = "Merry Christmas!"
    t.color("dark red", "red")  # 定义字体颜色
    # 定义文字、位置、字体、大小
    t.write(greeting, align="center", font=("Comic Sans MS", font_size, "bold"))


def draw_snow():
    """画雪花"""
    t.ht()  # 隐藏画笔的turtle形状
    t.pensize(2)  # 设置画笔的宽度
    for i in range(200):  # 随机画200个雪花
        t.pencolor("white")  # 设置画笔为白色
        t.pu()  # 提笔
        t.setx(r.randint(-350, 350))  # 随机设置X坐标
        t.sety(r.randint(-100, 350))  # 随机设置Y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔
        dens = 6  # 定义雪花的瓣数
        snow_size = r.randint(1, 10)  # 定义雪花的大小
        for j in range(dens):  # 画每一瓣雪花
            t.fd(int(snow_size))
            t.backward(int(snow_size))
            t.right(int(360 / dens))  # 转动一定的角度


def run():
    """
    执行整个绘图程序
    """
    # 获取用户输入
    greeting = input("请输入圣诞祝福（最多只能输入10个字符）: ")
    # 如果用户输入的字符超过10个，提示用户重新输入
    while len(greeting) > 10:
        greeting = input("祝福语的字符数超过了10个。请重新输入：")

    tree_height = 100.0  # 树的高度，作为绘画的基本单位
    set_initial_state(tree_height)
    draw_star(tree_height)
    draw_tree(tree_height)
    tree(15, tree_height)  # 具体调用tree函数，画出一棵树
    backward(tree_height / 2)
    draw_decorations()
    # 将用户输入的祝福语传递给write_text函数
    write_text(greeting)
    draw_snow()
    # 结束，等待用户操作，否则窗口会直接关闭
    t.done()


if __name__ == "__main__":
    run()  # 当脚本运行时，调用运行画图的函数
