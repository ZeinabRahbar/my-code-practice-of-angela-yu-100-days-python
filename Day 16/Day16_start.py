
from turtle import Turtle, Screen

from numpy.ma.core import left_shift

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("coral")

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

#############################
#############################
#############################

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["a", "b", "c"])
table.add_column("Pokemon Name", ["a", "b", "c"])
table.add_column("Pokemon Name", ["a", "b", "c"])

table.align = "l"
print(table)

#############################
#############################
#############################


