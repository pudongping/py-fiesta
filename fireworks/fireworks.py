import os

# 关闭掉 pygame 文档提示
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from random import randint, uniform, choice
import math

# 使用 pygame 库中的 vector 方法
vector = pygame.math.Vector2
# 定义重力
gravity = vector(0, 0.3)
# 定义显示宽度和高度
DISPLAY_WIDTH = DISPLAY_HEIGHT = 800

# 定义烟花的颜色
trail_colours = [(45, 45, 45), (60, 60, 60), (75, 75, 75),
                 (125, 125, 125), (150, 150, 150)]

# 定义烟花的动态和静态偏移量
dynamic_offset = 1
static_offset = 5


# 定义烟花类
class Firework:

    def __init__(self):
        """
        初始化烟花的颜色，位置，是否爆炸，粒子等属性
        """
        self.colour = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.colours = (
            (randint(0, 255), randint(0, 255), randint(0, 255)
             ), (randint(0, 255), randint(0, 255), randint(0, 255)),
            (randint(0, 255), randint(0, 255), randint(0, 255)))
        self.firework = Particle(randint(0, DISPLAY_WIDTH), DISPLAY_HEIGHT, True,
                                 self.colour)  # Creates the firework particle
        self.exploded = False
        self.particles = []
        self.min_max_particles = vector(100, 225)

    def update(self, win):  # called every frame
        """
        更新烟花的状态，包括应用重力，移动烟花，显示烟花等
        """
        if not self.exploded:
            self.firework.apply_force(gravity)
            self.firework.move()
            for tf in self.firework.trails:
                tf.show(win)

            self.show(win)

            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()
        else:
            for particle in self.particles:
                particle.apply_force(
                    vector(gravity.x + uniform(-1, 1) / 20, gravity.y / 2 + (randint(1, 8) / 100)))
                particle.move()
                for t in particle.trails:
                    t.show(win)
                particle.show(win)

    def explode(self):
        """
        爆炸函数，创建烟花粒子
        """
        amount = randint(self.min_max_particles.x, self.min_max_particles.y)
        for i in range(amount):
            self.particles.append(
                Particle(self.firework.pos.x, self.firework.pos.y, False, self.colours))

    def show(self, win):
        """
        在窗口上显示烟花
        """
        pygame.draw.circle(win, self.colour, (int(self.firework.pos.x), int(
            self.firework.pos.y)), self.firework.size)

    def remove(self):
        """
        移除已爆炸的烟花
        """
        if self.exploded:
            for p in self.particles:
                if p.remove is True:
                    self.particles.remove(p)

            if len(self.particles) == 0:
                return True
            else:
                return False


# 定义粒子类
class Particle:

    def __init__(self, x, y, firework, colour):
        """
        初始化粒子的位置，大小，颜色，是否为烟花，速度等参数
        :param x:
        :param y:
        :param firework:
        :param colour:
        """
        self.firework = firework
        self.pos = vector(x, y)
        self.origin = vector(x, y)
        self.radius = 20
        self.remove = False
        self.explosion_radius = randint(5, 18)
        self.life = 0
        self.acc = vector(0, 0)
        # trail variables
        self.trails = []  # stores the particles trail objects
        self.prev_posx = [-10] * 10  # stores the 10 last positions
        self.prev_posy = [-10] * 10  # stores the 10 last positions

        if self.firework:
            self.vel = vector(0, -randint(17, 20))
            self.size = 5
            self.colour = colour
            for i in range(5):
                self.trails.append(Trail(i, self.size, True))
        else:
            self.vel = vector(uniform(-1, 1), uniform(-1, 1))
            self.vel.x *= randint(7, self.explosion_radius + 2)
            self.vel.y *= randint(7, self.explosion_radius + 2)
            self.size = randint(2, 4)
            self.colour = choice(colour)
            for i in range(5):
                self.trails.append(Trail(i, self.size, False))

    def apply_force(self, force):
        """
        应用力量，改变速度
        :param force:
        :return:
        """
        self.acc += force

    def move(self):
        """
        移动粒子
        :return:
        """
        if not self.firework:
            self.vel.x *= 0.8
            self.vel.y *= 0.8

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        if self.life == 0 and not self.firework:  # check if particle is outside explosion radius
            distance = math.sqrt((self.pos.x - self.origin.x)
                                 ** 2 + (self.pos.y - self.origin.y) ** 2)
            if distance > self.explosion_radius:
                self.remove = True

        self.decay()

        self.trail_update()

        self.life += 1

    def show(self, win):
        """
        在窗口上显示粒子
        :param win:
        :return:
        """
        pygame.draw.circle(win, (self.colour[0], self.colour[1], self.colour[2], 0), (int(self.pos.x), int(self.pos.y)),
                           self.size)

    def decay(self):  # random decay of the particles
        """
        粒子衰减
        :return:
        """
        if 50 > self.life > 10:  # early stage their is a small chance of decay
            ran = randint(0, 30)
            if ran == 0:
                self.remove = True
        elif self.life > 50:
            ran = randint(0, 5)
            if ran == 0:
                self.remove = True

    def trail_update(self):
        """
        更新粒子尾迹
        :return:
        """
        self.prev_posx.pop()
        self.prev_posx.insert(0, int(self.pos.x))
        self.prev_posy.pop()
        self.prev_posy.insert(0, int(self.pos.y))

        for n, t in enumerate(self.trails):
            if t.dynamic:
                t.get_pos(self.prev_posx[n + dynamic_offset],
                          self.prev_posy[n + dynamic_offset])
            else:
                t.get_pos(self.prev_posx[n + static_offset],
                          self.prev_posy[n + static_offset])


# 定义尾迹类
class Trail:

    def __init__(self, n, size, dynamic):
        """
        初始化尾迹的位置，大小，颜色等参数
        :param n:
        :param size:
        :param dynamic:
        """
        self.pos_in_line = n
        self.pos = vector(-10, -10)
        self.dynamic = dynamic

        if self.dynamic:
            self.colour = trail_colours[n]
            self.size = int(size - n / 2)
        else:
            self.colour = (255, 255, 200)
            self.size = size - 2
            if self.size < 0:
                self.size = 0

    def get_pos(self, x, y):
        """
        获取尾迹的位置
        :param x:
        :param y:
        :return:
        """
        self.pos = vector(x, y)

    def show(self, win):
        """
        在窗口上显示尾迹
        :param win:
        :return:
        """
        pygame.draw.circle(win, self.colour, (int(
            self.pos.x), int(self.pos.y)), self.size)


def update(win, fireworks):
    """
    更新窗口和烟花
    :param win:
    :param fireworks:
    :return:
    """
    for fw in fireworks:
        fw.update(win)
        if fw.remove():
            fireworks.remove(fw)

    pygame.display.update()


# 定义主函数，初始化 pygame，创建窗口，设置窗口标题，定义时钟，定义烟花列表，定义运行状态
# 然后进入主循环，每帧更新窗口，创建新的烟花，更新烟花，直到用户退出程序
def main():
    print("点击 pygame 烟花界面之后，分别按下数字键 1 （会绽放新烟花）或者 2（会出现更多的烟花）")
    pygame.init()
    pygame.display.set_caption("Fireworks in Pygame")
    win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    fireworks = [Firework() for i in range(2)]  # create the first fireworks
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:  # Change game speed with number keys
                if event.key == pygame.K_1:  # number key 1
                    print("按下数字键 1，可以绽放新的烟花")
                    fireworks.append(Firework())
                if event.key == pygame.K_2:  # number key 2
                    print("按下数字键 2，可以绽放更多的烟花")
                    for i in range(10):
                        fireworks.append(Firework())
        win.fill((20, 20, 30))  # draw background

        if randint(0, 20) == 1:  # create new firework
            fireworks.append(Firework())

        update(win, fireworks)

    pygame.quit()
    quit()


main()
