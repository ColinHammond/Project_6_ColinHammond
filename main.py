#general idea: have targets randomly appear around the screen and shoot at where the player is
#player has to dodge and hit at least 20 targets to win, 1st wave starts off as 1 target, second wave 2
#third wave 4 and so on
import random

import arcade

class Comp151Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.score = 0
        self.player = None
        self.targets = arcade.SpriteList()
        self.sound = None
        self.player_dx = 0

    def setup(self):
        self.sound = arcade.load_sound("elec_lightning.wav")
        self.player = arcade.Sprite("f1-ship1-6.png")
        self.target = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
        self.player.center_x = 500
        self.player.center_y = 500
        self.target.center_x = 600
        self.target.center_y = 500
        for number in range(5):
            self.target = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.target.center_x = random.randint(16, 1184)
            self.target.center_y = random.randint(16, 984)
            self.targets.append(self.target)

    def on_update(self, time_since_update):
        self.player.center_x += self.player_dx
        if self.player.center_x >1200:
            self.player.center_x = 0
            arcade.play_sound(self.sound)
        for rock in self.targets:
            rock.center_y -= 2

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.player_dx += -3
        elif symbol == arcade.key.D:
            self.player_dx += 3
        #print(f" key: {symbol} was pressed")

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.player_dx = 0
        elif symbol == arcade.key.D:
            self.player_dx = 0

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.target.draw()
        self.targets.draw()
        arcade.finish_render()