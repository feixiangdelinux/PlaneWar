import pygame as pygame

from entity.UserDbInfo import UserDbInfo
from mongo_util import mongo_Helper
from plane_sprites import *


class PlaneGame(object):
    '''
    飞机大战主游戏
    '''
    user_db_info = UserDbInfo()
    screen_y=100
    def __init__(self):
        '''
        游戏初始化
        :return:
        '''
        # 创建游戏的窗口
        self.distory = 0
        self.package_num = 0
        # 把用户名保存到数据模型中（这里暂定为只有一个用户）
        PlaneGame.user_db_info.user_name = 'player1'
        # 把游戏的开始时间以时间戳的格式保存到数据模型中
        t = time.time()
        PlaneGame.user_db_info.start_time = int(t)
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self._create_sprites()
        # 设置定时器事件--创建敌机 每隔1000ms创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件--英雄发射子弹事件 每隔500ms发射一颗子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.mixer.init()
        pygame.mixer.music.load("./images/background_music.mp3")
        pygame.mixer.music.play(loops=-1)
        self.heroSound = pygame.mixer.Sound("./images/hero.wav")


    def _create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()
        # 创建加血包精灵和加血包精灵组
        self.enemy = BloodPack()
        self.bloodPack_group = pygame.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):
        '''
        游戏循环
        :return:
        '''

        while True:
            pygame.init()
            # screen = pygame.display.set_mode((600, 500))
            myfont = pygame.font.Font(None, 30)
            white = 0, 0, 0
            textImage = myfont.render(str(self.package_num), True, white)
            self.screen.blit(textImage, (10, 10))
            if (self.package_num%5) == 0 and self.package_num>0 :
                myfonssst = pygame.font.Font(None, 70)
                bss = 255, 255, 255
                textImage = myfonssst.render("congratulation", True, bss)
                self.screen.blit(textImage, (100, 100))

            pygame.display.update()
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self._even_handler()
            # 3.碰撞检测
            self._check_colide()
            # 4.更新/绘制精灵
            self._update_sprites()
            # 5.更新显示
            pygame.display.update()

    def _even_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame._game_over(self)
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                bloodPack = BloodPack()
                # 将敌机精灵加到敌机精灵组
                self.enemy_group.add(enemy)
                self.bloodPack_group.add(bloodPack)

            # 使用键盘提供的方法获取键盘按键--按键元组
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中对应的按钮索引值
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.height = 2
            elif keys_pressed[pygame.K_UP]:
                self.hero.height = -2
            elif keys_pressed[pygame.K_RETURN]:
                self.hero.fire()
            else:
                self.hero.speed = 0
                self.hero.height = 0

    def _check_colide(self):
        '''
        碰撞检测
        :return:
        '''
        # 子弹摧毁敌机
        collisions = pygame.sprite.groupcollide(self.hero.bullets_group, self.enemy_group, True, True)
        if collisions:
            self.distory += 1
            self.enemy.dead()

        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 如果enemies有值，说明，英雄飞机和敌机碰撞成功，接下来手动杀死英雄
        if len(enemies) > 0:
            self.hero.dead()
            self.enemy.kill()
            pygame.display.update()
            self._score()
        # 英雄吃加血包
        bloodPack = pygame.sprite.spritecollide(self.hero, self.bloodPack_group, True)
        if len(bloodPack)>0:
            self.package_num+=1
            if self.package_num == 3:
                print("第二关")




    def _update_sprites(self):
        '''
        更新精灵
        :return:
        '''
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.bloodPack_group.update()
        self.bloodPack_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets_group.update()
        self.hero.bullets_group.draw(self.screen)
    # 根据得分获取奖励
    def _get_reward(self, core):
        if core == 0:
            return '  You  weak'
        elif core == 1:
            return 'First blood'
        elif core == 2:
            return 'Double kill'
        elif core == 3:
            return 'Triple kill'
        elif core == 4:
            return 'Quadra kill'
        elif core == 5:
            return 'Penta  kill'
        else:
            return 'aced'
    def _score(self):
        '''
        得分结果
        :return:
        '''
        pygame.mixer.music.rewind()
        white = 255, 255, 255
        pygame.init()
        # screen = pygame.display.set_mode((600, 500))
        myfont = pygame.font.Font(None, 30)

        # 把游戏的结束时间以时间戳的格式保存到数据模型中
        t = time.time()
        PlaneGame.user_db_info.end_time = int(t)
        # 把用户的得分保存到数据模型中
        PlaneGame.user_db_info.user_core = self.distory
        # 把最终的数据保存到数据库中
        mongo_Helper().insert_data(PlaneGame.user_db_info)
        # mongo_Helper().remove_all()



        # text = "You score: " + str(self.distory)
        # textImage = myfont.render(text, True, white)
        # 用户名、游戏时长、得分、奖励、排名
        # 用户名
        play_name = PlaneGame.user_db_info.user_name
        # 游戏时长(结束时间减开始时间)
        play_time = str(PlaneGame.user_db_info.end_time - PlaneGame.user_db_info.start_time)
        # 得分
        play_core = str(PlaneGame.user_db_info.user_core)
        # 奖励
        play_reward = self._get_reward(PlaneGame.user_db_info.user_core)
        # 排名
        user_ranking = PlaneGame.user_db_info.user_name
        # 查询数据库,拿到所有数据
        # 按分数高低进行排序
        # 如果超过10条截取前10条
        # 显示
        aa = mongo_Helper().get_all()
        fontObj = pygame.font.Font(None, 30)
        color_green = (255, 255, 255)
        text_new = "name".rjust(10, ' ')  + "  " + "time".rjust(10, ' ')  + "  " + "core".rjust(10, ' ')  + "  " + "reward".rjust(11, ' ')
        textSurfaceObj = fontObj.render(text_new, False, color_green)
        textRectObj = textSurfaceObj.get_rect()
        PlaneGame.screen_y = PlaneGame.screen_y + 40
        textRectObj.center = (200, PlaneGame.screen_y)
        self.screen.blit(textSurfaceObj, textRectObj)

        color_green = (0, 255, 0)
        text_new = play_name.rjust(10, ' ')  + "  " + play_time.rjust(10, ' ')  + "  " + play_core.rjust(10, ' ')  + "  " + play_reward.rjust(11, ' ')
        textSurfaceObj = fontObj.render(text_new, False, color_green)
        textRectObj = textSurfaceObj.get_rect()
        PlaneGame.screen_y = PlaneGame.screen_y + 30
        textRectObj.center = (200, PlaneGame.screen_y)
        self.screen.blit(textSurfaceObj, textRectObj)

        for item in aa:
            # 用户名
            play_name = item['user_name']
            # 游戏时长(结束时间减开始时间)
            play_time = str(item['end_time'] - item['start_time'])
            # 得分
            play_core = str(item['user_core'])
            # 奖励
            play_reward = self._get_reward(item['user_core'])
            # 排名
            user_ranking = item['user_name']
            text_new = play_name.rjust(10, ' ') + "  " + play_time.rjust(10, ' ') + "  " + play_core.rjust(10, ' ') + "  " + play_reward


            color_green = (0, 0, 0)
            textSurfaceObj = fontObj.render(text_new, False, color_green)
            textRectObj = textSurfaceObj.get_rect()
            PlaneGame.screen_y=PlaneGame.screen_y+25
            textRectObj.center = (200,PlaneGame.screen_y)
            self.screen.blit(textSurfaceObj, textRectObj)
            print(item)

        # text_new = play_name+"  "+play_time+"  "+play_core+"  "+play_reward
        #
        # textImage = myfont.render(text_new, True, white)
        while True:
            for event in pygame.event.get():
                # 判断是否退出游戏
                if event.type == pygame.QUIT:
                    PlaneGame._game_over(self)
            # self.screen.blit(textImage, (100, 100))
            pygame.display.update()



    @staticmethod
    def _game_over(self):
        pygame.mixer.music.stop()
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
