import turtles

leo = turtles.Leonardo("Leonardo", "Blue Turtle")
michel = turtles.Michelangelo("Michelangelo", "Orange Turtle")
tello = turtles.Donatello("Donatello", "Purple Turtle")
raph = turtles.Raphael("Raphael", "Red Turtle")

turtle = [leo, michel, tello, raph]
for each in turtle:
    print(each.name)