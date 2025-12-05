import turtle

def koch_line(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch_line(length, level - 1)
        turtle.left(60)
        koch_line(length, level - 1)
        turtle.right(120)
        koch_line(length, level - 1)
        turtle.left(60)
        koch_line(length, level - 1)

def koch_snowflake(length, level):
    for _ in range(3):
        koch_line(length, level)
        turtle.right(120)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    koch_snowflake(400, level)
    turtle.done()

if __name__ == "__main__":
    main()



