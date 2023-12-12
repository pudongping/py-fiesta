# https://github.com/pygame/pygame
# https://github.com/pyinstaller/pyinstaller
# Windows 下打包：pyinstaller -F -i "snow.ico" snow.py
# Mac 下打包：pyinstaller -F -i "snow.icns" snow.py
import os
# 关闭掉 pygame 文档提示
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import sys
import requests
from io import BytesIO

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen_width, screen_height = 800, 600

# 设置雪花数量
num_snowflakes = 200

# 设置雪花最大和最小半径
min_snowflake_radius = 2
max_snowflake_radius = 4

# 设置雪花最大和最小速度
min_snowflake_speed = 1
max_snowflake_speed = 4

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)

# 获取背景图片链接
background_url = input("请输入背景图片的链接地址（如果没有，直接按 Enter）：")

# 下载背景图片
background_image = None
if background_url:
    response = requests.get(background_url)
    background_image = pygame.image.load(BytesIO(response.content))
    # 调整背景图片大小以适应屏幕
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# 创建屏幕
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snowfall")


# 定义雪花类
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.radius = random.randint(min_snowflake_radius, max_snowflake_radius)
        self.speed = random.uniform(min_snowflake_speed, max_snowflake_speed)

    def update(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = 0
            self.x = random.randint(0, screen_width)

    def draw(self):
        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), self.radius)


# 创建雪花列表
snowflakes = [Snowflake() for _ in range(num_snowflakes)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if background_image:
        # 绘制背景图片
        screen.blit(background_image, (0, 0))
    else:
        # 使用默认黑色背景
        screen.fill(black)

    # 更新雪花
    for flake in snowflakes:
        flake.update()

    # 绘制雪花
    for flake in snowflakes:
        flake.draw()

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(30)
