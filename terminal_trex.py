from blessings import Terminal
import time
import threading
import keyboard

t = Terminal()

last_obstacle_position = 0
last_ball_position = 0
score = 0

def serve_obstracles():
    global last_obstacle_position, last_ball_position, score
    if(score == -1):
        return
    # checking for colision
    if(last_obstacle_position == 4):
        if(last_ball_position > 1):
            score += 100
        else:
            score = -1
    if not last_obstacle_position:
        last_obstacle_position = 20
    with t.location(0,t.height):
        print(
            "_"*(last_obstacle_position-1) + 
            t.red("|") + 
            "_"*(20-last_obstacle_position), end="", flush=True)
    last_obstacle_position -= 1

        

def bounce(level = 0):
    if(score == -1):
            return
    with t.location(4,t.height-level):
        print(t.green("0"), end="", flush=True)

def print_score():
    if(score == -1):
        with t.location(10-len("game over")//2, t.height-5):
            print(t.blink(t.white_on_red("game over")) + t.normal, end="", flush=True)
        return
    s = f"score = {score}"
    with t.location(10-len(s)//2, t.height-5):
        print(t.blue_on_yellow(s), end="", flush=True)

def clear_screen():
    print(t.clear_eos, end="", flush=True)


def periodic_obstacle_server():
    while(1):
        serve_obstracles()
        bounce(last_ball_position)
        print_score()
        time.sleep(0.3)
        clear_screen()

def handle_bounce():
    global last_ball_position
    while(1):
        if(keyboard.is_pressed('space')):
            for i in range(1,4):
                last_ball_position = i
                time.sleep(0.3)

            for i in range(3,0, -1):
                last_ball_position = i
                time.sleep(0.3)
            break

    return handle_bounce()

threading.Thread(target=periodic_obstacle_server).start()
threading.Thread(target=handle_bounce).start()


    

