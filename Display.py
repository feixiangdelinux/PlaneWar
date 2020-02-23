import pygame
from plane_sprites import *

"导入并初始化所有Pygame模块，使用其他模块之前，必须先调用init方法"
pygame.init()

#创建游戏的窗口，480*700
screen = pygame.display.set_mode((480,700))

#绘制背景图像
#1.加载图像数据
background = pygame.image.load("./images/background.png")
#2.blit绘制图像
screen.blit(background,(0,0))
#3.pdate更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))

# 创建时钟对象
clock = pygame.time.Clock()
i = 0

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png",1)
enemy1 = GameSprite("./images/enemy1.png",2)
enemy2 = GameSprite("./images/enemy1.png",3)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1,enemy2)


#游戏循环
while True:
    # 指定循环体内部的代码执行频率
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        # 判断事件是否是退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 2.修改飞机的位置
    hero_rect.y -=1
    # 判断飞机的位置
    if hero_rect.y <= -120:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(background,(0,0))
    screen.blit(hero,hero_rect)

    # 让精灵组调用两个方法
    # update--让组中的所有精灵更新位置
    enemy_group.update()
    # draw--在screen上绘制所有的精灵
    enemy_group.draw(screen)
    # 4.调用update方法更新显示
    pygame.display.update()

"卸载所有Pygame模块，在游戏结束之前调用！"
