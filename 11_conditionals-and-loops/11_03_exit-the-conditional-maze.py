# You wake up in a maze of `if` statements and you need
# to find the path to get out:
#
# .--.--.--.  .--.--.
# |     |        |  |
# :  :--:  :  :  :  :
# |  |     |  |     |
# :  :  :  :--:--:--:
# |  |  |           |
# :  :  :--:--:--:  :
# |  |   You  |  |  |
# :  :--:--:  :  :  :
# |     |     |  |  |
# :--:  :  :--:  :  :
# |        |        |
# :--:--:--:--:--:--:
#
# However, this maze has a BIG limitation!
# There are only two actions you can take, you can only ADD
# either one of the following lines of code:
#
#     flag = True
#     flag = False
#
# You can add as many of them as you want to, but you can't change
# any of the code that is already there.
#
# Add the code so when you run it, it will print out all steps
# that you need to take in order to get out of the maze!
# You are always facing North and you can take sideways steps
# without changing the direction that you're looking.

flag = True
if flag == True: # Step 1. Move left from You. 
    print("left") 

flag = False
if flag == False: # Step 2. Proceed straight.
    print("straight ahead")

flag = False # Do not execute print function.
if flag == True: 
    print("left") 

flag = False
if flag == False: # Step 3. Continue moving straight.
    print("straight ahead")

flag = False
if flag == True: # Do not execute print function. Too many straights, will lead into wall.
    print("straight ahead")

flag = False
if flag == True: # Do not execute print function. Too many straight, will lead into wall.
    print("straight ahead")

flag = False
if flag == True: # Dead end, avoid. Take a right for next step.
    print("DEAD END") 

flag = False
if flag == True: # Do not execute print function. Left would run into wall. 
    print("left")

flag = False  
if flag == False: # Step 4. Take a right.
    print("right")

flag = False 
if flag == True: # Skip, would run into wall.
    print("straight ahead")

flag = False  
if flag == False: # Step 5. Proceed Straight towards exit of Maze. 
    print("straight ahead")

flag = True
if flag == False: # Deadend, avoiding.
    print("DEAD END")

flag = True # Step 6. Take right, towards Exit.
if flag == True:
    print("right")

flag = True # Step 7. Proceed straight. 
if flag == True:
    print("straight ahead")

flag = False # Do not execute print function. Left would run into wall. 
if flag == True:
    print("left")

flag = False # Step 8. Print EXIT at the end
if flag == False:
    print("EXIT!!")

flag = False # Dead end, avoid. Maze completed.
if flag == True:
    print("DEAD END")