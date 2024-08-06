from tkinter import *
import settings
import utils

root = Tk()

# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('MineSweeper Game')
root.resizable(False,False)

# define frames(windows) on root(main window)
top_frame = Frame(
    root,
    bg='red',
    width=settings.WIDTH,   # 1440/1440
    height=utils.calc_height(25)    # 180/720
)
top_frame.place(x=0,y=0)   # x=0,y=0

left_frame = Frame(
    root,
    bg='blue',
    width = utils.calc_width(25),   # 360/1440
    height = utils.calc_height(75)   # 540/720
)
left_frame.place(
    x=0,
    y=utils.calc_height(25)
)  # x=0,y=180

center_frame = Frame(
    root,
    bg='green',
    width=utils.calc_width(75),    # 1080/1440
    height=utils.calc_height(75)     # 540/720
)
center_frame.place(
    x=utils.calc_width(25),
    y=utils.calc_height(25)
)   # x=360, y=180

# Run the window
root.mainloop()