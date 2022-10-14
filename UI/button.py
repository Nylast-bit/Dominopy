import turtle


def button(title, color, x, y):
  button = turtle.Turtle()
  button.shape("square")
  button.shapesize(3,5)
  button.write(title)
  button.color(color)
  button.goto(x, y)
  return button