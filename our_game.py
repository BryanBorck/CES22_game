#!/usr/bin/env python3

import json
import pygame
import sys

from threading import Timer

pygame.mixer.pre_init()
pygame.init()

# Window settings
scale_factor = 1920/pygame.display.get_desktop_sizes()[0][0]
TITLE = "Formation"
WIDTH = int(1920/scale_factor)
HEIGHT = int(1080/scale_factor)
FPS = 60
GRID_SIZE = int(90/scale_factor)

screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Options
#sound_on = True

# Controls
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
JUMP = pygame.K_SPACE

# Levels
levels = ["levels/world-1.json", "levels/world-2.json", "levels/world-3.json"]

# Colors
TRANSPARENT = (0, 0, 0, 0)
DARK_BLUE = (16, 86, 103)
ORANGE = (255,165,0)
WHITE = (255, 255, 255)

# Fonts
FONT_SM = pygame.font.Font("assets/fonts/8514fix.fon", 64)
FONT_DS = pygame.font.Font("assets/fonts/Roboto-Bold.ttf", 32)
FONT_MD = pygame.font.Font("assets/fonts/8514fix.fon", 64)
FONT_LG = pygame.font.Font("assets/fonts/OCRAEXT.ttf", 100)

# Helper functions
def load_image(file_path, width=GRID_SIZE, height=GRID_SIZE):
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, (width, height))

    return img

def load_image_bigger(file_path, width=GRID_SIZE * 2, height=GRID_SIZE * 2):
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, (width, height))

    return img

#def play_sound(sound, loops=0, maxtime=0, fade_ms=0):
#     if sound_on:
#         sound.play(loops, maxtime, fade_ms)

# #def play_music():
#     if sound_on:
#         pygame.mixer.music.play(-1)

# Images

# BOY
# hero_walk1 = load_image("assets/character/boy_walk1.png")
# hero_walk2 = load_image("assets/character/boy_walk2.png")
# hero_jump = load_image("assets/character/boy_jump.png")
# hero_idle = load_image("assets/character/boy_idle.png")

#GIRL
hero_walk1 = load_image("assets/character/girl_walk1.png")
hero_walk2 = load_image("assets/character/girl_walk2.png")
hero_jump = load_image("assets/character/girl_jump.png")
hero_idle = load_image("assets/character/girl_idle.png")
hero_dead = load_image("assets/character/girl_dead.png")

hero_images = {"run": [hero_walk1, hero_walk2],
               "jump": hero_jump,
               "idle": hero_idle,
               "dead": hero_dead}

block_images = {"TL": load_image("assets/tiles/top_left.png"),
                "TM": load_image("assets/tiles/top_middle.png"),
                "TR": load_image("assets/tiles/top_right.png"),
                "ER": load_image("assets/tiles/end_right.png"),
                "EL": load_image("assets/tiles/end_left.png"),
                "TP": load_image("assets/tiles/top.png"),
                "CN": load_image("assets/tiles/center.png"),
                "LF": load_image("assets/tiles/lone_float.png"),
                "SP": load_image("assets/tiles/special.png"),
                "TL2": load_image("assets/tiles/top_left2.png"),
                "TM2": load_image("assets/tiles/top_middle2.png"),
                "TR2": load_image("assets/tiles/top_right2.png"),
                "ER2": load_image("assets/tiles/end_right2.png"),
                "EL2": load_image("assets/tiles/end_left2.png"),
                "TP2": load_image("assets/tiles/top2.png"),
                "CN2": load_image("assets/tiles/center2.png"),
                "LF2": load_image("assets/tiles/lone_float2.png"),
                "TL3": load_image("assets/tiles/top_left3.png"),
                "TM3": load_image("assets/tiles/top_middle3.png"),
                "TR3": load_image("assets/tiles/top_right3.png"),
                "ER3": load_image("assets/tiles/end_right3.png"),
                "EL3": load_image("assets/tiles/end_left3.png"),
                "TP3": load_image("assets/tiles/top3.png"),
                "CN3": load_image("assets/tiles/center3.png"),
                "LF3": load_image("assets/tiles/lone_float3.png")}

diamond_img = load_image("assets/items/new/diamond_icon.png")
star_img = load_image("assets/items/new/star_icon.png")
heart_img = load_image("assets/items/new/heart_icon.png")
oneup_img = load_image("assets/items/new/life_icon.png")
deathblock_img = load_image("assets/tiles/deathblock.png")
flag_img = load_image("assets/items/flag.png")
flagpole_img = load_image("assets/items/flagpole.png")
girl_img = pygame.image.load("assets/items/new/girl_icon.png").convert_alpha()

full_heart = pygame.image.load('assets/items/new/full_heart.png').convert_alpha()
half_heart = pygame.image.load('assets/items/new/half_heart.png').convert_alpha()
empty_heart = pygame.image.load('assets/items/new/empty_heart.png').convert_alpha()

monster_walk = []

for x in range(1,25):
    monster_walk.append(load_image("assets/enemies/golem_01/golem_01_{:02d}.png".format(x)))

monster_dead = []

for x in range(1,15):
    monster_dead.append(load_image("assets/enemies/golem_01/golem_01_dead_{:02d}.png".format(x)))

monster_images = [{"walk": monster_walk,
                  "dead": monster_dead}]

bear_walk1 = []

for x in range(1,13):
    bear_walk1.append(load_image("assets/enemies/wraith_01/wraith_01_{:02d}.png".format(x)))

bear_walk2 = []

for x in range(1,13):
    bear_walk2.append(load_image("assets/enemies/wraith_02/wraith_02_{:02d}.png".format(x)))

bear_walk3 = []

for x in range(1,13):
    bear_walk3.append(load_image("assets/enemies/wraith_03/wraith_03_{:02d}.png".format(x)))

bear_dead = []

for x in range(1,16):
    bear_dead.append(load_image("assets/enemies/wraith_03/wraith_03_dead_{:02d}.png".format(x)))

bear_images = [{"walk": bear_walk1, "dead": bear_dead},
               {"walk": bear_walk2, "dead": bear_dead},
               {"walk": bear_walk3, "dead": bear_dead}]

# Sounds
#JUMP_SOUND = pygame.mixer.Sound("assets/sounds/jump.wav")
#COIN_SOUND = pygame.mixer.Sound("assets/sounds/pickup_coin.wav")
#POWERUP_SOUND = pygame.mixer.Sound("assets/sounds/powerup.wav")
#HURT_SOUND = pygame.mixer.Sound("assets/sounds/hurt.ogg")
#DIE_SOUND = pygame.mixer.Sound("assets/sounds/death.wav")
#LEVELUP_SOUND = pygame.mixer.Sound("assets/sounds/level_up.wav")
#GAMEOVER_SOUND = pygame.mixer.Sound("assets/sounds/game_over.wav")

class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vy = 0
        self.vx = 0

    def apply_gravity(self, level):
        self.vy += level.gravity
        self.vy = min(self.vy, level.terminal_velocity)

class Block(Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class DeathBlock(Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
    
    def apply(self, character):
        character.hearts -= 1

class Character(Entity):

    def __init__(self, images):
        super().__init__(0, 0, images['idle'])

        self.image_idle_right = images['idle']
        self.image_idle_left = pygame.transform.flip(self.image_idle_right, 1, 0)
        self.images_run_right = images['run']
        self.images_run_left = [pygame.transform.flip(img, 1, 0) for img in self.images_run_right]
        self.image_jump_right = images['jump']
        self.image_jump_left = pygame.transform.flip(self.image_jump_right, 1, 0)
        self.image_dead_right = images['dead']
        self.image_dead_left = pygame.transform.flip(self.image_dead_right, 1, 0)

        self.running_images = self.images_run_right
        self.image_index = 0
        self.steps = 0

        self.speed = 6
        self.jump_power = 24

        self.vx = 0
        self.vy = 0
        self.facing_right = True
        self.on_ground = True

        self.score = 0
        self.stars = 0
        self.lives = 3
        self.hearts = 3
        self.max_hearts = 5
        self.invincibility = 0

    def move_left(self):
        self.vx = -self.speed
        self.facing_right = False

    def move_right(self):
        self.vx = self.speed
        self.facing_right = True

    def stop(self):
        self.vx = 0

    def jump(self, blocks):
        self.rect.y += 1

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        if len(hit_list) > 0:
            self.vy = -1 * self.jump_power
            #play_sound(JUMP_SOUND)

        self.rect.y -= 1

    def check_world_boundaries(self, level):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > level.width:
            self.rect.right = level.width
        if self.rect.top > level.height:
            self.hearts -= 1

    def move_and_process_blocks(self, blocks):
        self.rect.x += self.vx
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.vx = 0

        self.on_ground = False
        self.rect.y += self.vy + 1 # the +1 is hacky. not sure why it helps.
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vy > 0:
                self.rect.bottom = block.rect.top
                self.vy = 0
                self.on_ground = True
            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0

    def process_diamonds(self, diamonds):
        
        hit_list = pygame.sprite.spritecollide(self, diamonds, True)

        for diamond in hit_list:
            #play_sound(COIN_SOUND)
            self.score += diamond.value
    
    def process_stars(self, stars):
        
        hit_list = pygame.sprite.spritecollide(self, stars, True)

        for star in hit_list:
            #play_sound(COIN_SOUND)
            self.stars += star.value

    def process_enemies(self, enemies):

        hit_list = pygame.sprite.spritecollide(self, enemies, False)

        if len(hit_list) > 0 and self.invincibility == 0:
            for enemy in hit_list:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                hero_bottom = self.rect.bottom
                if enemy_top < hero_bottom < enemy_center and self.vy >= 0:
                    self.vy = -1 * self.jump_power
                    enemy.die()
                    t_kill = Timer(0.7, enemy.kill)
                    t_kill.start()
                else:
                    #play_sound(HURT_SOUND)
                    self.hearts -= 1
                    self.invincibility = int(0.75 * FPS)
    
    def process_deathblocks(self, deathblocks):
        # epsilon_h = self.rect.h / 20
        # epsilon_w = self.rect.w / 20
        hit_list = pygame.sprite.spritecollide(self, deathblocks, False)

        for block in hit_list:
            # if self.vx > 0:
            #     self.rect.right = block.rect.left - epsilon_w
            # elif self.vx < 0:
            #     self.rect.left = block.rect.right + epsilon_w
            # if self.vy > 0:
            #     self.rect.bottom = block.rect.top - epsilon_h
            # elif self.vy < 0:
            #     self.rect.top = block.rect.bottom + epsilon_h
            if self.invincibility == 0:
                block.apply(self)
                self.invincibility = int(0.75 * FPS)
                self.vx = 0
                self.vy = 0

    def process_powerups(self, powerups):
        hit_list = pygame.sprite.spritecollide(self, powerups, True)

        for p in hit_list:
            #play_sound(POWERUP_SOUND)
            p.apply(self)

    def check_flag(self, level):
        hit_list = pygame.sprite.spritecollide(self, level.flag, False)

        if len(hit_list) > 0 and self.stars >= 3:
            level.completed = True
            #play_sound(LEVELUP_SOUND)
        if len(hit_list) > 0 and self.stars < 3:
            level.incompleted = True

    def set_image(self): 
        if self.on_ground:
            if self.vx != 0:
                if self.facing_right:
                    self.running_images = self.images_run_right
                else:
                    self.running_images = self.images_run_left

                self.steps = (self.steps + 1) % self.speed

                if self.steps == 0:
                    self.image_index = (self.image_index + 1) % len(self.running_images)
                    self.image = self.running_images[self.image_index]
            else:
                if self.facing_right:
                    self.image = self.image_idle_right
                else:
                    self.image = self.image_idle_left
        else:
            if self.facing_right:
                self.image = self.image_jump_right
            else:
                self.image = self.image_jump_left

    def die(self):
        self.lives -= 1
        if self.facing_right:
            self.image = self.image_dead_right
        else:
            self.image = self.image_dead_left

        # if self.lives > 0:
        #     play_sound(DIE_SOUND)
        # else:
        #     play_sound(GAMEOVER_SOUND)

    def respawn(self, level):
        self.rect.x = level.start_x
        self.rect.y = level.start_y
        self.hearts = 3
        self.invincibility = 0
        self.facing_right = True

    def update(self, level):
        self.process_enemies(level.enemies)
        self.apply_gravity(level)
        self.move_and_process_blocks(level.blocks)
        self.check_world_boundaries(level)
        self.set_image()
        
        if self.hearts > 0:
            self.process_diamonds(level.diamonds)
            self.process_stars(level.stars)
            self.process_powerups(level.powerups)
            self.process_deathblocks(level.deathblocks)
            self.check_flag(level)

            if self.invincibility > 0:
                self.invincibility -= 1
        else:
            self.die()

class Coin(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image) 

        self.value = 1

class Diamond(Coin):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Star(Coin):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Enemy(Entity):
    def __init__(self, x, y, images):
        super().__init__(x, y, images['walk'][0])

        self.images_right = images['walk']
        self.images_left = [pygame.transform.flip(img, 1, 0) for img in self.images_right]
        self.images_dead_right = images['dead']
        self.images_dead_left = [pygame.transform.flip(img, 1, 0) for img in self.images_dead_right]
        self.current_images = self.images_left
        self.image_index = 0
        self.image_death_index = 0
        self.steps = 0
        self.vivo = True
        self.facing_right = True

    def reverse(self):
        self.vx *= -1
         
        if self.vx < 0:
            self.current_images = self.images_left
        else:
            self.current_images = self.images_right

        self.image = self.current_images[self.image_index]

    def check_world_boundaries(self, level):
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse()
        elif self.rect.right > level.width:
            self.rect.right = level.width
            self.reverse()

    def move_and_process_blocks(self, blocks, deathblocks):
        reverse = False

        self.rect.x += self.vx
        hit_list1 = pygame.sprite.spritecollide(self, blocks, False)
        hit_list2 = pygame.sprite.spritecollide(self, deathblocks, False)
        hit_list = hit_list1 + hit_list2

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.reverse()
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.reverse()
 
        self.rect.y += self.vy + 1 # the +1 is hacky. not sure why it helps.
        hit_list1 = pygame.sprite.spritecollide(self, blocks, False)
        hit_list2 = pygame.sprite.spritecollide(self, deathblocks, False)
        hit_list = hit_list1 + hit_list2

        reverse = True

        for block in hit_list:
            if self.vy >= 0:
                self.rect.bottom = block.rect.top
                self.vy = 0

                if self.vx > 0 and self.rect.right <= block.rect.right:
                    reverse = False

                elif self.vx < 0 and self.rect.left >= block.rect.left:
                    reverse = False

            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0

        if reverse:
            self.reverse()

    def process_deathblocks(self, deathblocks):
        reverse = False

        self.rect.x += self.vx
        hit_list = pygame.sprite.spritecollide(self, deathblocks, False)

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.reverse()
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.reverse()
        
        self.rect.y += self.vy + 1 # the +1 is hacky. not sure why it helps.
        hit_list = pygame.sprite.spritecollide(self, deathblocks, False)

        reverse = True

        for block in hit_list:
            if self.vy >= 0:
                self.rect.bottom = block.rect.top
                self.vy = 0

                if self.vx > 0 and self.rect.right <= block.rect.right:
                    reverse = False

                elif self.vx < 0 and self.rect.left >= block.rect.left:
                    reverse = False

            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0

        if reverse:
            self.reverse()


    def set_images(self):
        if self.steps == 0:
            self.image = self.current_images[self.image_index]
            self.image_index = (self.image_index + 1) % len(self.current_images)
        if not self.vivo and self.image_death_index == len(self.images_dead_right) - 1:
            if self.facing_right:
                self.image = self.images_dead_right[self.image_death_index]
                self.steps = (self.steps + 1)
            else:
                self.image = self.images_dead_left[self.image_death_index]
                self.steps = (self.steps + 1)
        if not self.vivo and self.image_death_index < len(self.images_dead_right) - 1:
            if self.facing_right:
                self.image = self.images_dead_right[self.image_death_index]
                self.image_death_index = (self.image_death_index + 1) % len(self.images_dead_right)
                self.steps = (self.steps + 1)
            else:
                self.image = self.images_dead_left[self.image_death_index]
                self.image_death_index = (self.image_death_index + 1) % len(self.images_dead_left)
                self.steps = (self.steps + 1)
        
        if self.vivo:
            self.steps = (self.steps + 1) % 2

    def is_near(self, hero):
        return abs(self.rect.x - hero.rect.x) < 2 * WIDTH

    def update(self, level, hero):
        if self.is_near(hero):
            self.apply_gravity(level)
            self.move_and_process_blocks(level.blocks, level.deathblocks)
            self.check_world_boundaries(level)
            self.set_images()

    def die(self):
        if self.vx < 0:
            self.facing_right = True
        else:
            self.facing_right = False
        self.vx = 0
        self.vivo = False

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.vx = self.start_vx
        self.vy = self.start_vy
        self.current_images = self.images_left
        self.image = self.current_images[0]
        self.steps = 0
        self.vivo = True

class Bear(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.start_x = x
        self.start_y = y
        self.start_vx = -2
        self.start_vy = 0

        self.vx = self.start_vx
        self.vy = self.start_vy

class Monster(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.start_x = x
        self.start_y = y
        self.start_vx = -2
        self.start_vy = 0

        self.vx = self.start_vx
        self.vy = self.start_vy

class OneUp(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        character.lives += 1

class Heart(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        character.hearts += 1
        character.hearts = min(character.hearts, character.max_hearts)

class Flag(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Level():

    def __init__(self, number, file_path):
        self.starting_blocks = []
        self.starting_enemies = []
        self.starting_diamonds = []
        self.starting_stars = []
        self.starting_powerups = []
        self.starting_deathblocks = []
        self.starting_flag = []

        self.number = number

        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.diamonds = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.deathblocks = pygame.sprite.Group()
        self.flag = pygame.sprite.Group()

        self.active_sprites = pygame.sprite.Group()
        self.inactive_sprites = pygame.sprite.Group()

        with open(file_path, 'r') as f:
            data = f.read()

        map_data = json.loads(data)

        self.width = map_data['width'] * GRID_SIZE
        self.height = map_data['height'] * GRID_SIZE

        self.start_x = map_data['start'][0] * GRID_SIZE
        self.start_y = map_data['start'][1] * GRID_SIZE

        for item in map_data['blocks']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            img = block_images[item[2]]
            self.starting_blocks.append(Block(x, y, img))

        for item in map_data['bears']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_enemies.append(Bear(x, y, bear_images[self.number - 1]))

        for item in map_data['monsters']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_enemies.append(Monster(x, y, monster_images[self.number - 1]))

        for item in map_data['diamonds']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_diamonds.append(Diamond(x, y, diamond_img))

        for item in map_data['stars']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_stars.append(Star(x, y, star_img))

        for item in map_data['oneups']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_powerups.append(OneUp(x, y, oneup_img))

        for item in map_data['deathblocks']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_deathblocks.append(DeathBlock(x, y, deathblock_img))

        for item in map_data['hearts']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_powerups.append(Heart(x, y, heart_img))

        for i, item in enumerate(map_data['flag']):
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            if i == 0:
               img = flag_img
            else:
               img = flagpole_img

            self.starting_flag.append(Flag(x, y, img))

        self.background_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        # self.scenery_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        self.inactive_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        self.active_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)

        if map_data['background-color'] != "":
            self.background_layer.fill(map_data['background-color'])

        if map_data['background-img'] != "":
            background_img = pygame.image.load(map_data['background-img']).convert_alpha()

            if map_data['background-fill-y']:
                h = background_img.get_height()
                w = int(background_img.get_width() * HEIGHT / h)
                background_img = pygame.transform.scale(background_img, (w, HEIGHT))

            if "top" in map_data['background-position']:
                start_y = 0
            elif "bottom" in map_data['background-position']:
                start_y = self.height - background_img.get_height()

            if map_data['background-repeat-x']:
                for x in range(0, self.width, background_img.get_width()):
                    self.background_layer.blit(background_img, [x, start_y])
            else:
                self.background_layer.blit(background_img, [0, start_y])

        # if map_data['scenery-img'] != "":
        #     scenery_img = pygame.image.load(map_data['scenery-img']).convert_alpha()

        #     if map_data['scenery-fill-y']:
        #         h = scenery_img.get_height()
        #         w = int(scenery_img.get_width() * HEIGHT / h)
        #         scenery_img = pygame.transform.scale(scenery_img, (w, HEIGHT))

        #     if "top" in map_data['scenery-position']:
        #         start_y = 0
        #     elif "bottom" in map_data['scenery-position']:
        #         start_y = self.height - scenery_img.get_height()

        #     if map_data['scenery-repeat-x']:
        #         for x in range(0, self.width, scenery_img.get_width()):
        #             self.scenery_layer.blit(scenery_img, [x, start_y])
        #     else:
        #         self.scenery_layer.blit(scenery_img, [0, start_y])

        pygame.mixer.music.load(map_data['music'])

        self.gravity = map_data['gravity']
        self.terminal_velocity = map_data['terminal-velocity']

        self.completed = False
        self.incompleted = False

        self.blocks.add(self.starting_blocks)
        self.enemies.add(self.starting_enemies)
        self.diamonds.add(self.starting_diamonds)
        self.stars.add(self.starting_stars)
        self.powerups.add(self.starting_powerups)
        self.deathblocks.add(self.starting_deathblocks)
        self.flag.add(self.starting_flag)

        self.active_sprites.add(self.diamonds, self.stars, self.enemies, self.powerups, self.deathblocks)
        self.inactive_sprites.add(self.blocks, self.flag)

        for s in self.active_sprites:
            s.image.convert()

        for s in self.inactive_sprites:
            s.image.convert()

        self.inactive_sprites.draw(self.inactive_layer)

        self.background_layer.convert()
        # self.scenery_layer.convert()
        self.inactive_layer.convert()
        self.active_layer.convert()

    def reset(self):
        self.enemies.add(self.starting_enemies)
        self.diamonds.add(self.starting_diamonds)
        self.stars.add(self.starting_stars)
        self.powerups.add(self.starting_powerups)
        self.deathblocks.add(self.starting_deathblocks)

        self.active_sprites.add(self.stars, self.enemies, self.powerups, self.deathblocks)

        for e in self.enemies:
            e.reset()

class Game():

    SPLASH = 0
    START = 1
    PLAYING = 2
    PAUSED = 3
    LEVEL_COMPLETED = 4
    GAME_OVER = 5
    VICTORY = 6
    LEVEL_INCOMPLETED = 7

    def __init__(self):
        self.window = screen
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.done = False

        self.reset()

    def start(self):
        self.level = Level(self.current_level, levels[self.current_level])
        self.level.reset()
        self.hero.respawn(self.level)

    def advance(self):
        self.current_level += 1
        self.start()
        self.stage = Game.START

    def reset(self):
        self.hero = Character(hero_images)
        self.current_level = 0
        self.start()
        self.stage = Game.SPLASH

    def display_splash(self, surface):
        line1 = FONT_LG.render(TITLE, 1, ORANGE)
        line2 = FONT_SM.render("Press any key to start.", 1, WHITE)

        x1 = WIDTH / 2 - line1.get_width() / 2
        y1 = HEIGHT / 3 - line1.get_height() / 2

        x2 = WIDTH / 2 - line2.get_width() / 2
        y2 = y1 + line1.get_height() + 16

        surface.blit(line1, (x1, y1))
        surface.blit(line2, (x2, y2))

    def display_message(self, surface, primary_text, secondary_text):
        line1 = FONT_MD.render(primary_text, 1, ORANGE)
        line2 = FONT_SM.render(secondary_text, 1, WHITE)

        x1 = WIDTH / 2 - line1.get_width() / 2
        y1 = HEIGHT / 3 - line1.get_height() / 2

        x2 = WIDTH / 2 - line2.get_width() / 2
        y2 = y1 + line1.get_height() + 16

        surface.blit(line1, (x1, y1))
        surface.blit(line2, (x2, y2))

    def display_stats(self, surface):
        # hearts_text = FONT_SM.render("Hearts: " + str(self.hero.hearts), 1, WHITE)
        # lives_text = FONT_SM.render("Lives: " + str(self.hero.lives), 1, WHITE)
        score_text = FONT_DS.render(str(self.hero.score), 1, WHITE)
        stars_text = FONT_DS.render(str(self.hero.stars), 1, WHITE)

        # surface.blit(hearts_text, (32, 32))
        # surface.blit(lives_text, (32, 64))
        surface.blit(score_text, (WIDTH - score_text.get_width() - 32, 18))
        surface.blit(diamond_img, (WIDTH - score_text.get_width() - 100, 0))
        surface.blit(stars_text, (WIDTH - stars_text.get_width() - 32, 66))
        surface.blit(star_img, (WIDTH - stars_text.get_width() - 100, 40))

    def full_hearts(self, surface):
        for heart in range(self.hero.hearts):
            surface.blit(full_heart, (heart * 50 + 28, 20))

    def full_lives(self, surface):
        for life in range(self.hero.lives):
            surface.blit(girl_img, (life * 50 + 28, 64))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            elif event.type == pygame.KEYDOWN:
                if self.stage == Game.SPLASH or self.stage == Game.START:
                    self.stage = Game.PLAYING
                    #play_music()

                elif self.stage == Game.PLAYING:
                    if event.key == JUMP:
                        self.hero.jump(self.level.blocks)
                
                elif self.stage == Game.LEVEL_INCOMPLETED:
                    if event.key == JUMP:
                        self.hero.jump(self.level.blocks)
                    self.stage = Game.PLAYING

                elif self.stage == Game.PAUSED:
                    pass

                elif self.stage == Game.LEVEL_COMPLETED:
                    self.advance()

                elif self.stage == Game.VICTORY or self.stage == Game.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset()

        pressed = pygame.key.get_pressed()

        if self.stage == Game.PLAYING:
            if pressed[LEFT]:
                self.hero.move_left()
            elif pressed[RIGHT]:
                self.hero.move_right()
            else:
                self.hero.stop()
        
        if self.stage == Game.LEVEL_INCOMPLETED:
            if pressed[LEFT]:
                self.hero.move_left()
            elif pressed[RIGHT]:
                self.hero.move_right()
            else:
                self.hero.stop()
            self.stage = Game.PLAYING

    def update(self):
        if self.stage == Game.PLAYING:
            self.hero.update(self.level)
            self.level.enemies.update(self.level, self.hero)
        
        if self.stage == Game.LEVEL_INCOMPLETED:
            self.hero.update(self.level)
            self.level.enemies.update(self.level, self.hero)
            self.stage = Game.PLAYING
        
        if self.level.incompleted:
            self.stage = Game.LEVEL_INCOMPLETED

        if self.level.completed:
            if self.current_level < len(levels) - 1:
                self.stage = Game.LEVEL_COMPLETED
            else:
                self.stage = Game.VICTORY
            pygame.mixer.music.stop()

        elif self.hero.lives == 0:
            self.stage = Game.GAME_OVER
            pygame.mixer.music.stop()

        elif self.hero.hearts == 0:
            self.level.reset()
            self.hero.respawn(self.level)

    def calculate_offset(self):
        x = -1 * self.hero.rect.centerx + WIDTH / 2

        if self.hero.rect.centerx < WIDTH / 2:
            x = 0
        elif self.hero.rect.centerx > self.level.width - WIDTH / 2:
            x = -1 * self.level.width + WIDTH

        return x, 0

    def draw(self):
        offset_x, offset_y = self.calculate_offset()

        self.level.active_layer.fill(TRANSPARENT)
        self.level.active_sprites.draw(self.level.active_layer)

        if self.hero.invincibility % 3 < 2:
            self.level.active_layer.blit(self.hero.image, [self.hero.rect.x, self.hero.rect.y])

        self.window.blit(self.level.background_layer, [offset_x / 3, offset_y])
        # self.window.blit(self.level.scenery_layer, [offset_x / 2, offset_y])
        self.window.blit(self.level.inactive_layer, [offset_x, offset_y])
        self.window.blit(self.level.active_layer, [offset_x, offset_y])

        self.display_stats(self.window)
        self.full_hearts(self.window)
        self.full_lives(self.window)

        if self.stage == Game.SPLASH:
            self.display_splash(self.window)
        elif self.stage == Game.START:
            self.display_message(self.window, "Ready?!!!", "Press any key to start.")
        elif self.stage == Game.PAUSED:
            pass
        elif self.stage == Game.LEVEL_COMPLETED:
            self.display_message(self.window, "Level Complete", "Press any key to continue.")
        elif self.stage == Game.LEVEL_INCOMPLETED:
            self.display_message(self.window, "Level Incomplete", "Please collect at least three stars.")
        elif self.stage == Game.VICTORY:
            self.display_message(self.window, "You Win!", "Press 'R' to restart.")
        elif self.stage == Game.GAME_OVER:
            self.display_message(self.window, "Game Over", "Press 'R' to restart.")

        pygame.display.flip()

    def loop(self):
        while not self.done:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start()
    game.loop()
    pygame.quit()
    sys.exit()
