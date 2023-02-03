from tkinter import *
from cell import Cell
import settings
import utilities

#To intialize tkinter we have to create Tk root widget which is a window with a titlebar and other decorations

root = Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.configure(bg="black")
root.resizable(False, False)

#Edit the frame
#This is the top. Despite the bg being black there is partitions on the followinng frames
top_frame = Frame(
    root,
    bg='black', #change later to black
    width = settings.WIDTH,
    height = utilities.height_prct(25) # Will calculate 25 % of the original height(720)
)
top_frame.place(x=0, y=0)

game_title=  Label(
    top_frame,
    bg = "black",
    fg = "white",
    text = "Minesweeper Game",
    font = ('', 40)
)

game_title.place(
    x = utilities.width_prct(25), y = 0
)
#The left side frame edited despite it being hard to distinguish
left_frame = Frame(
    root,
    bg='black', #To change to black
    width = utilities.width_prct(25), # 25% of the original width(1200)
    height = utilities.height_prct(75) # 75% of the original height(720)
)
left_frame.place(x=0, y=utilities.height_prct(25))#25 % Original height(720) =180


#The centre frame edited despite it being hard to distinguish
center_frame = Frame(
    root,
    bg="black",
    width = utilities.width_prct(75),
    height = utilities.height_prct(80)
)
center_frame.place(
    x = utilities.width_prct(25),
    y = utilities.height_prct(20)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y 
        )



#Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()

#Run the program
root.mainloop()