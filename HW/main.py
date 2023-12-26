from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from random import randint
from kivy.core.window import Window
import math


class Fire(Widget):
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            ball.velocity = vx + self.velocity_x/4, vy + self.velocity_y /4
            self.velocity_x *= -100000
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def check_bounds(self, height):
        if (self.y < 0 or self.top > height):
            self.velocity_y *= -1

class Gun(Widget):
    rot = NumericProperty(0)

    def updater1(self):
        self.rot += 2

    def updater2(self):
        self.rot -= 2


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class GunGame(Widget):
    ball = ObjectProperty(None)
    gun1 = ObjectProperty(None)
    gun2 = ObjectProperty(None)
    fire1 = ObjectProperty(None)
    fire2 = ObjectProperty(None)

    def set(self):
        self.gun1.rot = 90
        self.gun2.rot = 180
    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(0, 0)

    def serve_fire1(self):
        self.fire1.center = (self.gun1.pos[0] + self.gun1.width/2 * math.cos(math.radians(self.gun1.rot + 270)) + self.gun1.height/8 * math.cos(math.radians(360 - self.gun1.rot)),
                             self.gun1.pos[1] + self.gun1.width/2 * math.sin(math.radians(self.gun1.rot + 270)))
        self.fire1.velocity = Vector(3, 0).rotate(self.gun1.rot + 270)

    def serve_fire2(self):
        self.fire2.center = (self.gun2.pos[0] + self.gun2.width / 2 * math.cos(
            math.radians(self.gun2.rot + 270)) + self.gun2.height / 8 * math.cos(math.radians(360 - self.gun2.rot)),
                             self.gun2.pos[1] + self.gun2.width / 2 * math.sin(math.radians(self.gun2.rot + 270)))
        self.fire2.velocity = Vector(3, 0).rotate(self.gun2.rot + 270)

    def update(self, dt):
        self.ball.move()
        self.fire1.move()
        self.fire2.move()

        self.fire1.bounce_ball(self.ball)
        self.fire2.bounce_ball(self.ball)

        self.gun1.updater1()
        self.gun2.updater2()

        if (self.ball.y < 0 or self.ball.top > self.height):
            self.ball.velocity_y *= -1

        self.fire1.check_bounds(self.height)
        self.fire2.check_bounds(self.height)

        if self.ball.x < self.width * 1 / 6 - self.ball.width:
            self.fire2.score += 1
            self.serve_ball()

        if self.ball.x > self.width * 5 / 6 :
            self.fire1.score += 1
            self.serve_ball()

    def __init__(self, **kwargs):
        super(GunGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self.key_action)

    def key_action(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'a':  # Например, если вы хотите запустить функцию при нажатии клавиши "a"
            self.serve_fire1()

        if keycode[1] == 'l':  # Например, если вы хотите запустить функцию при нажатии клавиши "a"
            self.serve_fire2()
class GunApp(App):
    def build(self):
        game = GunGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 120)
        return game


if __name__ == '__main__':
    GunApp().run()
