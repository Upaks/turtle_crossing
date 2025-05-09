from turtle import Screen
import time
from scoreboard import Scoreboard
from body import Body
from cars import Cars

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Crossing Game")
screen.tracer(0)

body = Body()
cars = Cars()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=body.up)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(cars.car_speed)
    cars.move()
    cars.add_cars()
    scoreboard.update_score()
    for car in cars.all_cars:
        if car.distance(body) < 15:
            game_is_on = False
            scoreboard.game_over()

    if body.ycor() > 280:
        scoreboard.score += 1
        body.refresh()
        cars.increase_speed()



screen.exitonclick()