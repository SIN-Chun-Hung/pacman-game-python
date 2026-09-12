import turtle
import math
import random

# Setup the turtle window
turtle.setup(800, 700)
turtle.title("Pacman Game Project")
turtle.bgcolor("black")

# Setup the turtle
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Define the game timing (30 frames per second)
frame_time = 1000 // 30

# Define the maze information
maze_x       = -300
maze_y       = -270
maze_columns = 21
maze_rows    = 19

# Define the tile information
tile_size = 30

# Define the food information
food_size  = 10
food_count = 0

# Define the pacman information
pacman_size  = 30
pacman_speed = 6
pacman_x     = 0
pacman_y     = 0

# Create the variables for the pacman movement
current_move = ""   # This is the current movement
next_move = ""      # This is the next movement
pacman_heading_direction = ""

# Define the ghost information
ghost_size = 30
ghost_speed = 6
ghost_start_x = 0
ghost_start_y = 0
ghosts = []


# Maze of the game
#   + : wall
#   . : food
#   o : power food
#   P : starting position of pacman
#   G : starting position of ghosts
maze = [
    #012345678901234567890 - total 21 columns
    "+ +++++++++++++++++ +", # 0
    "+o.................o+", # 1
    "+.++++++++.++++++++.+", # 2
    "+.+o..............+.+", # 3
    "+.+.+++.+++.+...+.+.+", # 4
    "+.+.+....+..++..+.+.+", # 5
    "+.o.+++..+..+.+.+...+", # 6
    "+.+...+..+..+..++.+.+", # 7
    "+.+.+++.+++.+...+.+.+", # 8
    "+.+...............+.+", # 9
    "+.+.+++++++++++++.+.+", # 10
    "+...................+", # 11
    "+++++.+.++ ++.+.+++++", # 12
    "     .+.+ G +.+.     ", # 13
    "+++++.+.+++++.+.+++++", # 14
    "+.........P.........+", # 15
    "+.+++.+++++++++.+++.+", # 16
    "+o....+       +....o+", # 17
    "+ +++++       +++++ +"  # 18 - total 19 rows
]


#
# Draw the maze
#
for col in range(maze_columns):
    for row in range(maze_rows):
        # Get the tile
        tile = maze[row][col]

        # Locate the tile and move to the tile position
        #
        # Find the x, y position of the tile in the turtle window
        tile_x = maze_x + col * tile_size
        tile_y = maze_y + (maze_rows - row - 1) * tile_size
    
        
        # Put the turtle to the tile position
        turtle.goto(tile_x,tile_y)
        
        # Draw the tiles according to the tile symbol
        #
        if tile == "+":   # wall
            turtle.shape("square")
            turtle.shapesize( tile_size/20 ,tile_size/20 )  # 1 denotes 20 pixels
            turtle.color( "blue","black" )
            turtle.stamp()
            
        elif tile == ".": # food
            turtle.color("yellow")
            turtle.dot( food_size/2 )
            food_count += 1
            
            
        elif tile == "o": # power food
            turtle.color( "white" )
            turtle.dot( food_size )
            food_count += 1
            
        elif tile == "P": # pacman
            # Initialize the position of pacman
            pacman_x = tile_x
            pacman_y = tile_y

        elif tile == "G": # ghost
            # Initialize the position of ghost
            ghost_start_x = tile_x
            ghost_start_y = tile_y
            
        # Draw the tiles for walls, food and power food


# Create the pacman turtle
#
# Use turtle.Turtle() to make your pacman
# Make a yellow turtle circle shape as your pacman
# Put your pacman at the starting position
pacman = turtle.Turtle()
pacman.shape( "circle"  )
pacman.shapesize( pacman_size/20 , pacman_size/20 ) # 1 factor denote 20 pixels
pacman.color( "yellow" )
pacman.up()
pacman.goto( pacman_x,pacman_y )
pacman.hideturtle()
pacman_mouth_open = 40  # max mouth open angle
pacman_mouth_change = -8 # it can be either -8  or +8  
						  # if the mouth is open to max -> mouth change is -8 or 
						  # if the mouth is close to 0, mouth chnage to +8 

def draw_pacman():
    global pacman_mouth_open, pacman_mouth_change 
    pacman.clear()
    pacman.begin_fill()
    pacman.left(pacman_mouth_open/2)
    pacman.forward(pacman_size/2)
    pacman.left(90)
    pacman.circle(pacman_size/2,360 - pacman_mouth_open)
    pacman.left(90)
    pacman.forward(pacman_size/2)
    pacman.right(180)
    pacman.left(pacman_mouth_open/2)    
    pacman.end_fill()
    pacman_mouth_open = pacman_mouth_open + pacman_mouth_change
    
    if  pacman_mouth_open == 0 :
        pacman_mouth_change = 8

    elif pacman_mouth_open == 40:
        pacman_mouth_change = -8

    
# Handle the movement keys
#
# Complete the down, left and right movement keys for the pacman

# Handle the "Up" key for moving up
def move_up():
    global next_move
    next_move = "up"
    
def move_down():
    global next_move
    next_move = "down"
    
def move_right():
    global next_move
    next_move = "right"
    
def move_left():
    global next_move
    next_move = "left"
    

# cheat mode	
#----------------------

protect_mode = False

def no_toggle_protect():
    global protect_mode 
    pacman.color( "yellow" )
    protect_mode = False

    turtle.onkeypress(toggle_protect,"c")

def toggle_protect():
    global protect_mode

    pacman.color( "green" )
    protect_mode = True

    turtle.onkeypress(no_toggle_protect,"c")

    


# Set up the key press events
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(toggle_protect,"c")


# Need to use listen for key events to work
turtle.listen()


# Create 4 ghosts of different colors
for color in ["red", "pink", "cyan", "orange"]:
# Save and put your ghost at the starting position
    ghost = turtle.Turtle()
    ghost.shape( "circle"  )
    ghost.shapesize( ghost_size/20 , ghost_size/20 ) # 1 factor denote 20 pixels
    ghost.color("", color)
    ghost.up()
    ghost.goto( ghost_start_x,ghost_start_y )
# add a ghost into the ghosts [] list ; each list item is a
# dictionary which contains ghost ref. and the current ghost moving direction 
    ghosts.append( {"turtle": ghost,"move":"left" ,"colors":color} )
# call up draw_ghost( ghost, "left")  # parameter 1: ghost ref, param. 2: move dir. 
    ghost.hideturtle()# hide the default turtle  "arrow"

    
# Drawing the ghost

def draw_ghost(ghost,color,move):
    ghost.clear()
    ghost.color(color)
    ghost.begin_fill()
    ghost.forward( ghost_size/2 )
    ghost.left(90)
    ghost.forward( ghost_size/2)
    ghost.left(90)
    ghost.forward( ghost_size )
    ghost.left(90)
    ghost.forward( ghost_size )
    ghost.left(90)
    ghost.forward( ghost_size )
    ghost.left(90)
    ghost.forward( ghost_size/2 )
    ghost.left(90)
    ghost.forward( ghost_size/2)
    ghost.right(180)
    ghost.end_fill()


    ghost.forward( ghost_size/4 )
    ghost.color("white")
    ghost.begin_fill()
    ghost.circle( 7 )
    ghost.end_fill()

    ghost.backward( 2*ghost_size/4)
    ghost.color("white")
    ghost.begin_fill()
    ghost.circle( 7 )
    ghost.end_fill()

    ghost.forward(ghost_size/4)

    if move == "up":
        ghost.forward(ghost_size/4)
        ghost.circle(7,180)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        ghost.circle(7,180)

        ghost.backward( 2*ghost_size/4)
        ghost.circle(7,180)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        ghost.circle(7,180)
        
        
    elif move == "down":
        ghost.forward(ghost_size/4)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        
        ghost.backward( 2*ghost_size/4)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()


    elif move == "left":
        ghost.forward(ghost_size/4)
        ghost.circle(7,270)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        ghost.circle(7,90)

        ghost.backward( 2*ghost_size/4)
        ghost.circle(7,270)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        ghost.circle(7,90)

    elif move == "right":
        ghost.forward(ghost_size/4)
        ghost.circle(7,90)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        ghost.circle(7,270)

        ghost.backward( 2*ghost_size/4)
        ghost.circle(7,90)
        ghost.color("blue")
        ghost.begin_fill()
        ghost.circle(4)
        ghost.end_fill()
        ghost.circle(7,270)

    
        
    
#Pacman Game Score Calculator
score = 0
score_turtle = turtle.Turtle()
score_turtle.up()
score_turtle.hideturtle()
score_turtle.goto( -300 , 300 )
score_turtle.color("white")
score_turtle.write("Score:"+str(score),font=("Arial",20,"bold"))

	

	
#--------------------------------------------------------------------------
# This is the game main loop, which is mainly used to:
#
# Determine the movement of pacman
# Determine if pacman hits a wall or food

def game_loop():
    global current_move, next_move
    global pacman_x, pacman_y
    global food_count
    global score
    global pacman_mouth_open
    global pacman_mouth_change


    # Handle the pacman next move
    #
    # Update the condition of the following if statement so that
    # pacman can only move along the rows and columns of the maze
    if (pacman_x - maze_x) % tile_size == 0 and \
       (pacman_x - maze_x) % tile_size == 0 and \
        next_move != "":
        
        current_move = next_move
        next_move = ""


    # Find the pacman new position
    #
    # Complete the down, left and right moves

    # new_x, new_y is the position where the pacman wants to go,BUT
    # it has Not take effect yet. (until it passes the collision detect:
    
    if current_move == "up":
        new_x = pacman_x
        new_y = pacman_y + pacman_speed   #pacman_speed= 6 pix
        pacman.setheading(90)
    elif current_move == "down":
        new_x = pacman_x
        new_y = pacman_y - pacman_speed
        pacman.setheading(270)
    elif current_move == "right":
        new_x = pacman_x + pacman_speed
        new_y = pacman_y
        pacman.setheading(0)
    elif current_move == "left":
        new_x = pacman_x - pacman_speed
        new_y = pacman_y
        pacman.setheading(180)
    else:
        new_x = pacman_x
        new_y = pacman_y


    # tunelling
    # going out of Left / Right of gameboard
    if new_x < maze_x: # going out left border
        new_x = maze_x + (maze_columns - 1)*tile_size
    elif new_x > maze_x + (maze_columns - 1)*tile_size : #exit rt border
        new_x = maze_x

    if new_y < maze_y: # going out bottom border
        new_y = maze_y + (maze_rows - 1)*tile_size
    elif new_y > maze_y + (maze_rows - 1)*tile_size : #exit top border
        new_y = maze_y


    #
    # Handle the collision of pacman, food and walls
    #
    for col in range(maze_columns):
        for row in range(maze_rows):
            # Get the tile
            tile = maze[row][col]

            # Locate the tile and calculate the distance
            #
            # Find the x, y position of the tile in the turtle window
            tile_x = maze_x + col * tile_size
            tile_y = maze_y + (maze_rows - row - 1) * tile_size
            # Find the distance between pacman and the tile in dx, dy
            dx = math.fabs( new_x - tile_x )
            dy = math.fabs( new_y - tile_y )


            # Collision detection
            #
            # If pacman collides with any wall, stop pacman from moving
            if dx < (pacman_size + tile_size) / 2 and \
               dy < (pacman_size + tile_size) / 2 and \
               tile == "+":
               # reset the new_x, new_y to the curr. pacman_x,y
                new_x = pacman_x
                new_y = pacman_y
               
            #  Hit normal food, remove the food from the window
            #  and remove it from the maze list
            elif tile == "."  and \
                dx < (pacman_size + food_size/2) / 2 and \
                dy < (pacman_size + food_size/2) / 2 :
                turtle.goto( tile_x, tile_y )
                turtle.color("black")
                turtle.dot( food_size/2 )
                # delete the food from teh maze list
                # rebuild the whole string in maze[row]

                maze[row] = maze[row][ :col] + " " + maze[row][col+1: ]
                food_count -= 1
                score = score + 1 

            # power food

            elif tile == "o"  and \
                dx < (pacman_size + food_size) / 2 and \
                dy < (pacman_size + food_size) / 2 :
                turtle.goto( tile_x, tile_y )
                turtle.color("black")
                turtle.dot( food_size )
                # delete the food from teh maze list
                # rebuild the whole string in maze[row]

                maze[row] = maze[row][ :col] + " " + maze[row][col+1: ]
                food_count -= 1
                score = score + 5

                



    # Move the pacman
    #
    # Move pacman to the new position
    # Update pacman_x and pacman_y
    pacman.goto( new_x , new_y )
    pacman_x = new_x
    pacman_y = new_y

    
    # Score Calculator
    if score != 0:
        score_turtle.clear()      
        score_turtle.write("Score:"+str(score),font=("Arial",20,"bold"))

    draw_pacman()

#----------Start of the Ghost Code------------
    #Moving the ghost
    for ghost_item in ghosts:
        ghost = ghost_item["turtle"]
        ghost_move = ghost_item["move"]
        ghost_color= ghost_item["colors"]

        ghost_x = ghost.xcor()
        ghost_y = ghost.ycor()

        ## check the next valid moving direction for the ghost 
        if (ghost_x - maze_x) % tile_size == 0 and \
           (ghost_y - maze_y) % tile_size == 0:
            
            col = int((ghost_x - maze_x) / tile_size)
            row = (maze_rows - 1) - int((ghost_y - maze_y) / tile_size)

            moves=[]
            # check the Valid moving dir. for the ghost
            if row > 0 and maze[row - 1][col] != "+":
                moves.append("up")
            if row < maze_rows-1 and maze[row + 1][col] != "+":
                moves.append("down")
            if col < maze_columns -1 and maze[row][col + 1 ] != "+":
                moves.append("right")
            if col > 0  and maze[row][col - 1 ] != "+":
                moves.append("left")


            # Avoid the ghost moving around

            if len(moves) > 1:
                if ghost_move == "up" and "down" in moves:
                    moves.remove( "down" )
                if ghost_move == "down" and "up" in moves:
                    moves.remove( "up" )
                if ghost_move == "right" and "left" in moves:
                    moves.remove( "left" )
                if ghost_move == "left" and "right" in moves:
                    moves.remove( "right" )



            
            # Select one valid direction randomly from moves[ ]
            ghost_item["move"] = random.choice(moves)
            ghost_move = ghost_item["move"]
            
            
        # move the ghost
        ##### 
        if ghost_move == "up":
            ghost_x = ghost_x
            ghost_y = ghost_y + ghost_speed
        elif ghost_move == "down":
            ghost_x = ghost_x
            ghost_y = ghost_y - ghost_speed
        elif ghost_move == "left":
            ghost_x = ghost_x - ghost_speed
            ghost_y = ghost_y
        elif ghost_move == "right":
            ghost_x = ghost_x + ghost_speed
            ghost_y = ghost_y
        else:
            ghost_x = ghost_x
            ghost_y = ghost_y

        draw_ghost(ghost,ghost_color,ghost_move)

        #move th ghost to the new position    
        ghost.goto( ghost_x , ghost_y )

    # Update the window content
    turtle.update()

    # Handle the collision checking between the pacman and the 4 ghosts


    for ghost_item in ghosts:
        ghost = ghost_item["turtle"]
        ghost_move = ghost_item["move"]

        ghost_x = ghost.xcor()
        ghost_y = ghost.ycor()


        # process one of the ghost-pacman colision
        dx = math.fabs( new_x - ghost_x )
        dy = math.fabs( new_y - ghost_y )


        # If pacman collides with the ghost
        if not protect_mode:
            if dx < (pacman_size + ghost_size) / 2 and \
               dy < (pacman_size + ghost_size) / 2 :

                turtle.goto(0 ,-20)
                turtle.color("red")
                turtle.write("Game over ! ",font=("Arial",50,"bold"),align="center")

                return  ## exit the game loop
    #----------- end of game over processing ---------

    # ---------- Start of you win processing
        if food_count == 0 :
            turtle.goto(0 ,-20)
            turtle.color("white")
            turtle.write("You win!",font=("Arial",50,"bold"),align="center")

            return  ## exit the game loop
    
        
    # Keep on running the game loop
    turtle.ontimer(game_loop, frame_time)

#---------------------------------------------------------------------------
# Start the game loop
game_loop()

turtle.done()
