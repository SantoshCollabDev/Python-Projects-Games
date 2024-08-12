from tkinter import Button, Label
import random
import settings

class Cell:
    all = []  # used to capture the cells instantiated
    cell_count_label_obj = None  # class variable since it is not a instance level
    cell_count = 0
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # Append the object to Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,   # on center frame
            width = 12,
            height=6,
            # text = f"{self.x},{self.y}"
        )

        # bind -- to bind the action to a button
        # in bind we don't call function rather pass its name
        btn.bind('<Button-1>',self.left_click_actions )  # left click
        btn.bind('<Button-3>',self.right_click_actions ) # right click
        self.cell_btn_object = btn

    # Function to fetch number of cells left to click at any point in time
    # in the game
    # def create_cell_count_label(self, location): --- converted to static method below
    @staticmethod    # since this is a generic function performed throughout the game
    # independent of any object
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text=f"Cells left : {Cell.cell_count}",
            font= ("", 32)
        )
        Cell.cell_count_label_obj = lbl

    def left_click_actions(self, event): # bind passes 2 arguments - object and action(left)
        # print(event)
        # print("Im left clicked")
        if self.is_mine:
            self.show_mine()
        else:
            # self.show_cell()    # display surrounded cells info on cell clicked

            # speed up the game by auto-filling the surrounding cells info
            # when the number of mines around the clicked cell is ZERO
            self.show_cell()    # display surrounded cells info on cell clicked
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the values of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property   # to mark the surrounded cells info as read only attribute
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),  # (0,0)
            self.get_cell_by_axis(self.x - 1, self.y),      # (0,1)
            self.get_cell_by_axis(self.x - 1, self.y + 1),  # (0,2)
            self.get_cell_by_axis(self.x, self.y - 1),      # (1,0)
            self.get_cell_by_axis(self.x + 1, self.y - 1),  # (2,0)
            self.get_cell_by_axis(self.x + 1, self.y),      # (2,1)
            self.get_cell_by_axis(self.x + 1, self.y + 1),  # (2,2)
            self.get_cell_by_axis(self.x, self.y + 1)       # (1,2)
        ]
        # List comprehension expression - to exclude None values
        cells = [cell for cell in cells if cell is not None]
        return cells

    # iterate through surrounded cells objects and determine which have mines
    # and which are non-mines. in the process track & return the count of mines
    @property       # read only method to get the count of mine cells
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            # print(self.get_cell_by_axis(0,0))
            # print(self.surrounded_cells)   # read surrounded cell object
            # print(self.surrounded_cells_mines_length)  # no of mines around the cell clicked
            # display the count of surrounding mine cells on the cell clicked
            self.cell_btn_object.configure(text=f"{self.surrounded_cells_mines_length}")

            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_obj: # check if it None or carries some value
                Cell.cell_count_label_obj.configure(
                    text=f"Cells left : {Cell.cell_count}"
                )
        # mark the cell as opened ( use it as the last line of the method )
        self.is_opened = True

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost!
        self.cell_btn_object.configure(bg="red") # turn the cell to red

    def right_click_actions(self, event): # bind passes 2 arguments - object and action(right)
        print(event)
        print("Im right clicked")

    @staticmethod    # Class's Global Method - not specific to any cell
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT    # pick 1/4th of total cells
        )
        # print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"