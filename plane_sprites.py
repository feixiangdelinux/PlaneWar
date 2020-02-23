import random
import time

import pygame

# 屏幕大小
import plance_main

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    '''
    游戏精灵--飞机大战
    '''

    def __init__(self, image_name,dead_image="./images/pause_nor.png",dead_sound="./images/enemy.wav",speed=1, x=0, y=0):
        # 调用父类的初始化方法
        super().__init__()

        pygame.mixer.init()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # 设置大小为图像大小
        self.speed = speed
        self.dead_sound = pygame.mixer.Sound(dead_sound)
        self.dead_image = dead_image

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

    def dead(self):
        '''
        死亡特效
        :return:
        '''
        self.kill()




class Background(GameSprite):
    '''
    游戏背景精灵
    '''

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()
        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class BloodPack(GameSprite):
    '''
    加血包
    '''

    def __init__(self):
        # 1.调用父类方法，创建加血包精灵，同时指定敌机图片
        super().__init__("./images/award2.png","./images/enemy1_down3.png","./images/hero.wav")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(5, 8)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)


    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def dead(self):
        '''
        死亡特效
        :return:
        '''
        pass

class Enemy(GameSprite):
    '''
    敌机精灵
    '''

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png","./images/enemy1_down3.png","./images/hero.wav")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)


    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def dead(self):
        '''
        死亡特效
        :return:
        '''
        self.dead_sound.play()
        self.kill()

class Bullet(GameSprite):
    '''
    子弹精灵
    '''

    def __init__(self):
        # 1.调用父类方法，创建子弹精灵，同时指定子弹图片，设置初始速度
        super().__init__("./images/bullet1.png","./images/pause_nor.png","./images/enemy.wav", -2)

    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断子弹是否飞出屏幕
        if self.rect.bottom <= 0:
            self.kill()


class Hero(GameSprite):
    '''
    英雄精灵
    '''

    def __init__(self):
        # 1.调用父类，设置image/speed
        super().__init__("./images/me1.png","./images/me_destroy_3.png","./images/hero.wav", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.height = self.rect.height

        # 创建子弹精灵组
        self.bullets_group = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
        final_rectx = self.rect.x + self.speed
        if final_rectx >=0 and final_rectx < SCREEN_RECT.width-self.rect.width:
            self.rect.x += self.speed
        # 英雄在垂直方向移动
        final_recty = self.rect.y + self.height
        if final_recty >= 0 and final_recty < SCREEN_RECT.height - self.rect.height:
            self.rect.y += self.height

    def fire(self):
        for i in (0,1,2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.将子弹精灵加到子弹精灵组
            self.bullets_group.add(bullet)

    def dead(self):
        '''
        死亡特效
        :return:
        '''
        self.dead_sound.play()
        time.sleep(1)
        self.kill()