# simple pong game
import pygame

# create classes ill come back to


class Ball:
    def __init__(self, size, speed):
        self.radius = size
        self.speed = speed

class Paddle:
    def __init__(self, length, speed):
        self.length = length
        self.speed = speed
