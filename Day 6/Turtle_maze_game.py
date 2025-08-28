import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Maze Generation and Turtle Navigation")
screen.setup(width=700, height=700)

# Maze parameters
cols, rows = 10, 10
cell_size = 50

# Turtle for drawing maze walls
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.color("red")
maze_turtle.pensize(6)
maze_turtle.penup()

# Turtle for navigation
nav_turtle = turtle.Turtle()
nav_turtle.shape("turtle")
nav_turtle.color("blue")
nav_turtle.penup()
nav_turtle.speed(1)

# Create grid of cells; each cell has walls on all sides initially
grid = [[{'visited': False, 'walls': [True, True, True, True]} for _ in range(cols)] for _ in range(rows)]
# Walls order: [top, right, bottom, left]

def draw_cell_walls(x, y):
    screen_x = (x - cols//2) * cell_size
    screen_y = (rows//2 - y) * cell_size
    maze_turtle.goto(screen_x, screen_y)
    maze_turtle.setheading(0)
    maze_turtle.pendown()
    # Draw top wall
    if grid[y][x]['walls'][0]:
        maze_turtle.forward(cell_size)
    else:
        maze_turtle.penup()
        maze_turtle.forward(cell_size)
        maze_turtle.pendown()
    maze_turtle.right(90)
    # Draw right wall
    if grid[y][x]['walls'][1]:
        maze_turtle.forward(cell_size)
    else:
        maze_turtle.penup()
        maze_turtle.forward(cell_size)
        maze_turtle.pendown()
    maze_turtle.right(90)
    # Draw bottom wall
    if grid[y][x]['walls'][2]:
        maze_turtle.forward(cell_size)
    else:
        maze_turtle.penup()
        maze_turtle.forward(cell_size)
        maze_turtle.pendown()
    maze_turtle.right(90)
    # Draw left wall
    if grid[y][x]['walls'][3]:
        maze_turtle.forward(cell_size)
    else:
        maze_turtle.penup()
        maze_turtle.forward(cell_size)
        maze_turtle.pendown()
    maze_turtle.penup()

def get_neighbours(x, y):
    neighbours = []
    if y > 0 and not grid[y-1][x]['visited']:  # Top
        neighbours.append(('top', x, y-1))
    if x < cols-1 and not grid[y][x+1]['visited']:  # Right
        neighbours.append(('right', x+1, y))
    if y < rows-1 and not grid[y+1][x]['visited']:  # Bottom
        neighbours.append(('bottom', x, y+1))
    if x > 0 and not grid[y][x-1]['visited']:  # Left
        neighbours.append(('left', x-1, y))
    return neighbours

def remove_walls(current_x, current_y, next_x, next_y):
    dx = next_x - current_x
    dy = next_y - current_y
    if dx == 1:  # next is to right
        grid[current_y][current_x]['walls'][1] = False
        grid[next_y][next_x]['walls'][3] = False
    elif dx == -1:  # next is to left
        grid[current_y][current_x]['walls'][3] = False
        grid[next_y][next_x]['walls'][1] = False
    elif dy == 1:  # next is below
        grid[current_y][current_x]['walls'][2] = False
        grid[next_y][next_x]['walls'][0] = False
    elif dy == -1:  # next is above
        grid[current_y][current_x]['walls'][0] = False
        grid[next_y][next_x]['walls'][2] = False

def generate_maze(x=0, y=0):
    grid[y][x]['visited'] = True
    neighbours = get_neighbours(x, y)
    random.shuffle(neighbours)
    for direction, nx, ny in neighbours:
        if not grid[ny][nx]['visited']:
            remove_walls(x, y, nx, ny)
            generate_maze(nx, ny)

# Generate the maze starting from top-left corner
generate_maze(0, 0)

# Draw the maze walls
maze_turtle.speed(0)
maze_turtle.penup()
for y in range(rows):
    for x in range(cols):
        draw_cell_walls(x, y)

# Navigation turtle start position (top-left)
pos_x, pos_y = 0, 0
nav_turtle.goto((pos_x - cols//2) * cell_size + cell_size//2, (rows//2 - pos_y) * cell_size - cell_size//2)

# Goal position (bottom-right)
goal_x, goal_y = cols - 1, rows - 1
goal_marker = turtle.Turtle()
goal_marker.hideturtle()
goal_marker.penup()
goal_marker.color("green")
goal_marker.goto((goal_x - cols//2) * cell_size + cell_size//2, (rows//2 - goal_y) * cell_size - cell_size//2)
goal_marker.dot(30)

steps = 0

# Movement check (walled or out of bounds)
def can_move(x1, y1, x2, y2):
    if x2 < 0 or y2 < 0 or x2 >= cols or y2 >= rows:
        return False
    dx = x2 - x1
    dy = y2 - y1
    if dx == 1:
        return not grid[y1][x1]['walls'][1]
    if dx == -1:
        return not grid[y1][x1]['walls'][3]
    if dy == 1:
        return not grid[y1][x1]['walls'][2]
    if dy == -1:
        return not grid[y1][x1]['walls'][0]
    return False

# Move the turtle if allowed, update position, and check for goal
def move(dx, dy):
    global pos_x, pos_y, steps
    new_x = pos_x + dx
    new_y = pos_y + dy
    if can_move(pos_x, pos_y, new_x, new_y):
        pos_x, pos_y = new_x, new_y
        nav_turtle.goto((pos_x - cols//2) * cell_size + cell_size//2, (rows//2 - pos_y) * cell_size - cell_size//2)
        steps += 1
        print(f"Moved to ({pos_x}, {pos_y}), steps: {steps}")
        if pos_x == goal_x and pos_y == goal_y:
            print(f"Goal reached in {steps} steps!")
            screen.bye()
    else:
        print("Move blocked by a wall or out of bounds.")

# Key press handlers
def go_up(): move(0, -1)
def go_down(): move(0, 1)
def go_left(): move(-1, 0)
def go_right(): move(1, 0)

# Instructions
print("Use arrow keys to move the turtle. Reach the green spot!")
print("Walls are thick red lines, turtle cannot move through them.")

# Bind keys
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

screen.mainloop()
