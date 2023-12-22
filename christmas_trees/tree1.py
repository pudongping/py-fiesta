from turtle import *


def setup_turtle():
    """ 设置画板和初始化海龟的状态 """
    setup(600, 600, startx=None, starty=None)
    title("🎄")
    speed(0)
    pencolor("pink")
    pensize(10)
    penup()
    hideturtle()
    goto(0, 150)
    showturtle()
    pendown()
    shape(name="classic")


def guest(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        right(10)


def guet(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        left(10)


def qu(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(6)
        right(10)
    seth(-150)
    fd(20)


def hdj(x, y):
    penup()
    goto(x, y)
    seth(80)
    pendown()
    pensize(2)
    circle(5)
    seth(10)
    fd(15)
    seth(120)
    fd(20)
    seth(240)
    fd(20)
    seth(180)
    fd(20)
    seth(-60)
    fd(20)
    seth(50)
    fd(20)
    seth(-40)
    fd(30)
    seth(-130)
    fd(5)
    seth(135)
    fd(30)
    seth(-60)
    fd(30)
    seth(-150)
    fd(6)
    seth(110)
    fd(30)


def uit(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(2)
    circle(5)
    seth(-10)
    fd(15)
    seth(90)
    fd(15)
    seth(200)
    fd(15)
    seth(160)
    fd(15)
    seth(-90)
    fd(15)
    seth(10)
    fd(15)
    seth(-60)
    fd(20)
    seth(-180)
    fd(5)
    seth(110)
    fd(20)
    seth(-90)
    fd(20)
    seth(-180)
    fd(6)
    seth(70)
    fd(15)
    hideturtle()


def yut(x, y, z):
    penup()
    goto(x, y)
    pendown()
    seth(z)
    for po in range(5):
        fd(4)
        left(36)


def ytu(x, y, z):
    penup()
    goto(x, y)
    pendown()
    seth(z)
    for kk in range(5):
        fd(4)
        left(36)


def iou(x, y, z):
    penup()
    goto(x, y)
    pencolor("#f799e6")
    pendown()
    seth(z)
    for po in range(10):
        fd(4)
        left(18)


def koc(x, y, size):
    pensize(2)
    pencolor("black")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor("yellow")
    for i in range(5):
        left(72)
        fd(size)
        right(144)
        fd(size)
    end_fill()


def draw_section_one():
    seth(-120)
    for i in range(10):
        fd(12)
        right(2)
    penup()
    goto(0, 150)
    seth(-60)
    pendown()
    for i in range(10):
        fd(12)
        left(2)
    seth(-150)
    penup()
    fd(10)
    pendown()
    for i in range(5):
        fd(10)
        right(15)
    seth(-150)
    penup()
    fd(8)
    pendown()
    for i in range(5):
        fd(10)
        right(15)
    seth(-155)
    penup()
    fd(5)
    pendown()
    for i in range(5):
        fd(7)
        right(15)


def draw_section_two():
    penup()
    goto(-55, 34)
    pendown()
    seth(-120)
    for i in range(10):
        fd(8)
        right(5)

    penup()
    goto(50, 35)
    seth(-60)
    pendown()
    for i in range(10):
        fd(8)
        left(5)
    seth(-120)
    penup()
    fd(10)
    seth(-145)
    pendown()
    for i in range(5):
        fd(10)
        right(15)
    penup()
    fd(10)
    seth(-145)
    pendown()
    for i in range(5):
        fd(12)
        right(15)
    penup()
    fd(8)
    seth(-145)
    pendown()
    for i in range(5):
        fd(10)
        right(15)
    penup()
    seth(-155)
    fd(8)
    pendown()
    for i in range(5):
        fd(11)
        right(15)


def draw_section_three():
    penup()
    goto(-100, -40)
    seth(-120)
    pendown()
    for i in range(10):
        fd(6)
        right(3)
    penup()
    goto(80, -39)
    seth(-50)
    pendown()
    for i in range(10):
        fd(6)
        left(3)
    seth(-155)
    penup()
    fd(10)
    pendown()
    for i in range(5):
        fd(8)
        right(10)
    penup()
    fd(8)
    seth(-145)
    pendown()
    for i in range(7):
        fd(8)
        right(10)
    penup()
    fd(8)
    seth(-145)
    pendown()
    for i in range(7):
        fd(7)
        right(10)
    penup()
    fd(8)
    seth(-145)
    pendown()
    for i in range(7):
        fd(7)
        right(10)
    penup()
    fd(8)
    seth(-140)
    pendown()
    for i in range(7):
        fd(6)
        right(10)


def draw_section_four():
    penup()
    goto(-120, -95)
    seth(-130)
    pendown()
    for i in range(7):
        fd(10)
        right(5)
    penup()
    goto(100, -95)
    seth(-50)
    pendown()
    for i in range(7):
        fd(10)
        left(5)
    penup()
    seth(-120)
    fd(10)
    seth(-155)
    pendown()
    for i in range(6):
        fd(8)
        right(10)
    penup()
    seth(-160)
    fd(10)
    seth(-155)
    pendown()
    for i in range(6):
        fd(8)
        right(10)
    penup()
    seth(-160)
    fd(10)
    seth(-155)
    pendown()
    for i in range(6):
        fd(8)
        right(10)
    penup()
    seth(-160)
    fd(10)
    seth(-160)
    pendown()
    for i in range(6):
        fd(8)
        right(10)
    penup()
    seth(-160)
    fd(10)
    seth(-160)
    pendown()
    for i in range(6):
        fd(8)
        right(10)
    penup()
    seth(-160)
    fd(10)
    seth(-165)
    pendown()
    for i in range(5):
        fd(10)
        right(11)


def draw_section_five():
    penup()
    goto(-70, -165)
    seth(-85)
    pendown()
    for i in range(3):
        fd(5)
        left(3)
    penup()
    goto(70, -165)
    seth(-95)
    pendown()
    for i in range(3):
        fd(5)
        right(3)
    seth(-170)
    penup()
    fd(10)
    pendown()
    pendown()
    for i in range(10):
        fd(12)
        right(2)


def draw_section_six():
    penup()
    goto(70, -165)
    pendown()
    seth(-90)
    pensize(8)
    pencolor("#de8891")
    circle(-20, 90)

    penup()
    goto(30, -185)
    pendown()
    seth(-180)
    pensize(8)
    pencolor("#de8891")
    fd(40)

    penup()
    goto(-5, -170)
    pendown()
    seth(-180)
    pensize(8)
    pencolor("#de8891")
    fd(35)


def draw_tree_branches():
    """画树枝"""
    guest(-70, -150, 160)
    guest(100, -150, 160)
    guet(110, -110, 50)
    guest(160, -140, 150)
    qu(80, -120, 180)
    guest(70, -85, 165)
    guest(-40, -85, 165)
    guet(90, -50, 50)
    guest(130, -80, 150)
    pencolor("pink")
    qu(-40, -60, 180)
    pencolor('#de8891')
    qu(80, -30, 180)
    pencolor("pink")
    qu(40, 10, 180)
    pencolor("#de8891")
    guest(-60, 30, 120)
    guest(-20, -20, 150)
    guet(45, 40, 60)
    guest(-30, 40, 170)
    guest(-30, 110, 115)
    guet(40, 90, 60)
    guest(80, 50, 160)
    pencolor("#de8891")


def draw_bow_ties():
    """画蝴蝶结"""
    # 小蝴蝶结
    seth(0)
    uit(40, -160)
    hdj(-80, -120)
    yut(-67, -115, 120)
    yut(-86, -123, 150)
    hdj(40, -50)
    yut(52, -45, 130)
    yut(34, -55, 160)
    seth(0)
    uit(-20, -60)
    ytu(-4, -60, 100)
    ytu(-20, -60, 120)
    hdj(-30, 20)
    yut(-15, 25, 130)
    yut(-40, 20, 180)
    uit(30, 70)
    ytu(45, 70, 100)
    ytu(30, 70, 120)

    # 大蝴蝶结
    pencolor("#f799e6")
    pensize(5)
    penup()
    seth(0)
    goto(0, 150)
    pendown()
    circle(10)
    seth(-15)
    fd(40)
    seth(90)
    fd(40)
    seth(200)
    fd(40)
    seth(160)
    fd(40)
    seth(-90)
    fd(40)
    seth(15)
    fd(40)
    seth(-70)
    pencolor("#f799e6")
    pensize(4)
    fd(40)
    seth(-180)
    fd(10)
    seth(100)
    fd(40)
    seth(-100)
    fd(40)
    seth(-180)
    fd(10)
    seth(70)
    fd(40)
    penup()
    seth(0)
    goto(0, 130)
    pencolor("pink")
    pendown()

    seth(0)
    iou(35, 145, 100)
    iou(-7, 145, 110)
    pencolor("red")
    pensize(7)
    penup()
    goto(-35, 135)
    pendown()


def draw_xmas_hat():
    """画圣诞帽"""
    seth(-20)
    pensize(2)
    penup()
    goto(-30, -120)
    pencolor("black")
    pendown()
    fillcolor("red")
    fd(30)
    circle(4, 180)
    fd(30)
    circle(4, 180)
    penup()
    goto(-25, -115)
    seth(75)
    pendown()
    begin_fill()
    for i in range(5):
        fd(6)
        right(20)
    seth(-10)
    for i in range(5):
        fd(8)
        right(15)
    seth(145)
    for i in range(5):
        fd(5)
        left(2)
    seth(90)
    for i in range(5):
        fd(1)
        left(2)
    seth(-90)
    for i in range(4):
        fd(4)
        right(6)
    seth(161)
    fd(30)
    end_fill()
    pensize(1)
    pencolor("black")


def draw_stars():
    """画星星"""
    seth(-15)
    koc(-120, -70, 10)
    seth(10)
    koc(100, -20, 10)
    seth(-10)
    koc(10, 40, 10)
    seth(30)
    koc(-80, 60, 10)
    koc(100, -150, 10)
    koc(-140, -150, 10)
    koc(20, 120, 10)


def draw_socks():
    """画袜子"""
    seth(-20)
    pensize(2)
    penup()
    goto(-20, 80)
    pencolor("black")
    pendown()
    fillcolor("red")
    fd(25)
    circle(4, 180)
    fd(25)
    circle(4, 180)
    penup()
    goto(-15, 80)
    pendown()
    begin_fill()
    fillcolor("red")
    seth(-120)
    fd(20)
    seth(150)
    fd(5)
    circle(7, 180)
    fd(15)
    circle(5, 90)
    fd(30)
    seth(160)
    fd(18)
    end_fill()
    penup()
    seth(0)
    goto(100, -230)
    pendown()


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
    color("dark red", "red")  # 定义字体颜色
    # 定义文字、位置、字体、大小
    write(greeting, align="center", font=("Comic Sans MS", font_size, "bold"))


def run():
    """调用上面的所有函数来画整个圣诞场景"""
    # 获取用户输入
    greeting = input("请输入圣诞祝福（最多只能输入10个字符）: ")
    # 如果用户输入的字符超过10个，提示用户重新输入
    while len(greeting) > 10:
        greeting = input("祝福语的字符数超过了10个。请重新输入：")

    setup_turtle()
    draw_section_one()
    draw_section_two()
    draw_section_three()
    draw_section_four()
    draw_section_five()
    draw_section_six()
    draw_tree_branches()
    draw_bow_ties()
    draw_xmas_hat()
    draw_stars()
    draw_socks()
    write_text(greeting)
    done()


if __name__ == "__main__":
    run()  # 当脚本运行时，调用运行画图的函数
