import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if player.at_finish_line():
        player.init_player()
        scoreboard.level += 1
        scoreboard.refresh()
        car_manager.increase_speed()

    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
