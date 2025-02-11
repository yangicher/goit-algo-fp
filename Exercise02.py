import turtle
import math

def draw_tree(branch_length, level):
    if level == 0:
        return
    
    turtle.forward(branch_length)
    turtle.left(45)
    turtle.color("red")
    draw_tree(branch_length / math.sqrt(2), level - 1)
    
    turtle.right(90)
    draw_tree(branch_length / math.sqrt(2), level - 1)
    
    turtle.left(45)
    turtle.backward(branch_length)

def main():
    try:
        level = int(input("Enter recursion level: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return
    
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()
    
    draw_tree(100, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
