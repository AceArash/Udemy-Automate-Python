# WORK IN PROGRESS

# fcc python project: probability calculator

import copy
import random

# Consider using the modesl imported above.

class Hat:
    def __init__(self, **kwargs):

        self.contents = []

        for k, v in kwargs.items():
            self.contents += v * [k]

        print(self.contents)


    def draw(self, num):
        balls = random.sample(self.contents, num)

        # print(balls)
        for _ in range(num):
            random.shuffle()
        # randomly select num of balls

        for ball in balls:
            self.contents.remove(ball)

        print(self.contents)

        return balls


hat = Hat(red = 5, orange = 4)
hat.draw(3)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        balls = hat.draw(num_balls_drawn)
        #check if balls match expectation

        eb_list = []
        for k, v in expected_balls.items():
            eb_list += v * [k] 
        if all(x in balls for x in eb_list):
            M += 1

    probability = M / num_experiments

    return probability


    balls = hat.draw(num_balls_drawn)