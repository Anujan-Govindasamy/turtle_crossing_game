from turtle import Screen
from car_manager import CarManager
from player import Player
import time
from scoreboard import Scoreboard

screen=Screen()

screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.tracer(0)

tony = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=tony.player_move,key="Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #collusion with th car
    for car in car_manager.all_cars:
        if car.distance(tony) < 20:
            scoreboard.game_over()
            game_on = False

    #detect if player reached the other end
    if tony.is_at_finishline():
        tony.go_to_start()
        scoreboard.score_increase()
        car_manager.level_up()



screen.exitonclick()