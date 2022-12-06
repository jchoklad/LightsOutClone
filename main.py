import random
import tkinter
import time

#Main Game Window
window = tkinter.Tk()
window.geometry('500x500')
window.title("Lights Out Clone")
window.resizable(False,False)

title_lbl = tkinter.Label(window, text="Lights Out Clone", fg="black", font=("Helvetica", 18))
title_lbl.place(x=170,y=20)
turn_counter_lbl = tkinter.Label(window, text="Turn Counter: 0", fg="black", font=("Helvetica", 10))
turn_counter_lbl.place(x=220,y=470)

button_dict = {}
board_data = {}
move_list = []
initial_random_moves = 7


def initialize_board_buttons():
    for x in range(5):
        for y in range(5):
            bt = tkinter.Button(window, height=3, width=6, bg="green", fg="black", command=lambda posx=x, posy=y: clicked((posx, posy)))
            bt.place(x=x * 100 + (-(x - 3) * 40), y=y * 100 + ((-(y - 3) * 40) - 50))
            button_dict[(x, y)] = bt
    bt_restart = tkinter.Button(window, height=3, width=12, text="Restart", bg="white", fg="black", command=start_new_game)
    bt_restart.place(x=120, y=400)
    bt_solve = tkinter.Button(window, height=3, width=12, text="Solve", bg="white", fg="black", command=solve_board)
    bt_solve.place(x=220, y=400)
    bt_quit = tkinter.Button(window, height=3, width=12, text="Quit", bg="white", fg="black", command=quit)
    bt_quit.place(x=320,y=400)


def initialize_board_data():
    for x in range(5):
        for y in range(5):
            board_data[(x, y)] = 0
            button_dict[(x,y)].configure(bg="green")
    move_list.clear()
    turn_counter_lbl.configure(text=("Turn Counter: {}".format(len(move_list)-initial_random_moves)))
    title_lbl.configure(text="Lights Out Clone")
    title_lbl.place(x=170)


def set_starting_board():
    #function will randomly select moves simulating a starting board
    for x in range(initial_random_moves):
        posx = random.randint(0,4)
        posy = random.randint(0, 4)
        clicked((posx,posy))


def update_board_data(pos):
    #function will update the location selected as well as the north south east and west of the selected location if valid
    board_data[pos] = 1 - board_data[pos]
    if board_data[pos] == 1:
        button_dict[pos].configure(bg="red")
    else:
        button_dict[pos].configure(bg="green")

    if pos[0]<4:
        east = (pos[0]+1,pos[1])
        board_data[east] = 1 - board_data[east]
        if board_data[east] == 1:
            button_dict[east].configure(bg="red")
        else:
            button_dict[east].configure(bg="green")

    if pos[0] > 0:
        west = (pos[0]-1,pos[1])
        board_data[west] = 1 - board_data[west]
        if board_data[west] == 1:
            button_dict[west].configure(bg="red")
        else:
            button_dict[west].configure(bg="green")

    if pos[1] < 4:
        south = (pos[0],pos[1]+1)
        board_data[south] = 1 - board_data[south]
        if board_data[south] == 1:
            button_dict[south].configure(bg="red")
        else:
            button_dict[south].configure(bg="green")

    if pos[1] > 0:
        north = (pos[0],pos[1]-1)
        board_data[north] = 1 - board_data[north]
        if board_data[north] == 1:
            button_dict[north].configure(bg="red")
        else:
            button_dict[north].configure(bg="green")

    check_for_win()


def check_for_win():
    has_won = 0
    for x in range(5):
        for y in range(5):
            if board_data[(x,y)] == 1:
                has_won = 1
    if has_won == 0:
        title_lbl.configure(text="You Win!")
        title_lbl.place(x=220)


def clicked(pos):
    move_list.append(pos)
    turn_counter_lbl.configure(text=("Turn Counter: {}".format(len(move_list)-initial_random_moves)))
    window.update()
    update_board_data(pos)
    print()


def solve_board():
    move_list.reverse()
    for x in range(len(move_list)):
        button_dict[move_list[x]].configure(bg="yellow")
        window.update()
        time.sleep(.7)
        update_board_data(move_list[x])
        window.update()


def quit():
    window.quit()


def start_new_game():
    initialize_board_data()
    set_starting_board()


initialize_board_buttons()
start_new_game()

window.mainloop()