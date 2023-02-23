import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import random


class Turn_Light(tk.Frame):
    row = 5
    column = 5
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("First GUI") #Controls the window title.
        self.pack()
        self.move = 0
        self.ran = ["OFF","OFF"]
        self.count = 0
        self.FirstStart = True
        master.resizable(False, False)
        self.var = tk.StringVar(value="Easy")
        self.createWidgets()

    def createWidgets(self):
        self.master.geometry(f"{160+38*Turn_Light.column}x{200+38*Turn_Light.row}+200+200")
        floors = [i for i in range(1,Turn_Light.row*Turn_Light.column+1)]
        self.buttons = {}
        global e
        e = []
        xPos = 0
        yPos = 0
        self.text = tk.Label(self, text="LIGHT OUT",fg="Black",font=('Helvetica bold', 26))
        self.text.grid(row= 0, column= 0,columnspan=Turn_Light.column)
        self.Moves = tk.Button(self, text=f"Moves\n{self.move}",width=15,height=2,state="disabled")
        self.Moves.grid(row = Turn_Light.row+2, column = 0 ,columnspan=Turn_Light.column,pady=(0,80))
        for floor in floors:
            if(yPos == Turn_Light.column):
                xPos = xPos + 1
                yPos = 0
            if (xPos == 0):
                self.buttons[floor] = tk.Button(self, width=4,height=2,text=random.choice(self.ran), 
                                                    command = lambda f=floor: self.pressed(f))
                self.buttons[floor].grid(row=xPos, column =yPos,pady=(80,0))
                e.append([xPos,yPos])
                yPos = yPos +1
            else:
                self.buttons[floor] = tk.Button(self, width=4,height=2,text=random.choice(self.ran), 
                                                    command = lambda f=floor: self.pressed(f))
                self.buttons[floor].grid(row=xPos, column =yPos)
                e.append([xPos,yPos])
                yPos = yPos +1  
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        file = tk.Menu(menubar, tearoff= 0)
        file.add_command(label = "New Game",command=self.restart_program)
        file.add_command(label = "Exit",command=root.destroy)
        menubar.add_cascade(label="File", menu=file)
        difficulty_settings = tk.Menu(menubar,tearoff=0)
        difficulty_settings.add_radiobutton(label="Easy",command=lambda : self.change_difficulty("Easy"),variable=self.var)
        difficulty_settings.add_radiobutton(label="Normal",command=lambda : self.change_difficulty("Normal"),variable=self.var)
        difficulty_settings.add_radiobutton(label="Hard(SOON)",command=lambda : self.change_difficulty("Hard"),variable=self.var,state="disabled")
        difficulty_settings.add_separator()
        difficulty_settings.add_command(label = "Row and Colum", command= self.row_columnWidgets)
        menubar.add_cascade(label="Difficulty", menu=difficulty_settings)
        row_column = tk.Menu(menubar, tearoff=0)
        row_column.add_radiobutton
        help = tk.Menu(menubar, tearoff= 0)
        help.add_command(label="How to play", command=lambda : self.show_info(0))
        help.add_command(label="About us",command=lambda : self.show_info(1))
        menubar.add_cascade(label="Help",menu=help)
        for i in range(1,Turn_Light.row*Turn_Light.column+1):
            if self.buttons[i]["text"] == "OFF":
                self.buttons[i]["bg"] = "Gray"
                self.buttons[i]["fg"] = "White"
            elif self.buttons[i]["text"] == "ON": 
                self.buttons[i]["bg"] = "Yellow"
                self.buttons[i]["fg"] = "Black"
                self.count +=1
    
    def row_columnWidgets(self):
        self.raw_column_settings = tk.Toplevel(self.master)
        self.raw_column_settings.wm_title("row_column")
        tk.Label(self.raw_column_settings,text="ROW\n(MIN 5;MAX 12)").grid(row=0,column=0,pady=10,padx=10)
        row_entry = tk.Entry(self.raw_column_settings)
        row_entry.insert(0,Turn_Light.row)
        row_entry.grid(row=0,column=1,pady=10,padx=10)
        tk.Label(self.raw_column_settings,text="COLUMN\n(MIN 5;MAX 12)").grid(row=1,column=0,pady=10,padx=10)
        column_entry = tk.Entry(self.raw_column_settings)
        column_entry.insert(0,Turn_Light.column)
        column_entry.grid(row=1,column=1,pady=10,padx=10)
        tk.Button(self.raw_column_settings,text="apply", command= lambda:self.row_column(row_entry,column_entry)).grid(row=2,column=0,columnspan=2)

    def row_column(self,row,column):
        try:
                int(row.get()),int(column.get())
        except ValueError:
            showerror("ERROR", "Try to input numbers!")
            return
        if int(row.get()) >= 5 and int(row.get()) <= 12:

            Turn_Light.row = int(row.get())
            Turn_Light.column = int(column.get())
            self.restart_program()
            self.raw_column_settings.destroy()
        else:
            showerror("ERROR", "Try to input numbers between 5 and 12!")

    def show_info(self,status):
        show_info = tk.Toplevel(self.master)
        if status == 0 :
            show_info.wm_title("How to play")
            text = tk.Label(show_info, text="How to play Lights Outs?\nThe player must think about which squares to press to turn off all the lights.\nExample: A game board with 2 states: 0 or 1 is in the initial position:\n0	0	0\n0	0	0\n0	0	0\nA click on the middle box gives the following result:\n0	1	0\n1	1	1\n0	1	0\n(the box clicked as well as the 4 adjacent cells (top, bottom, right, left) have changed state) \nFor a game with n states, pressing a box n times returns it to its initial state.",   
                                            fg="Black",font=('Helvetica bold',12))
            text.grid()
        elif status == 1:
            show_info.wm_title("About us")
            text = tk.Label(show_info, text="Play for fun!",fg="Black",font=('Helvetica bold',12))
            text.grid()
    
    def change_difficulty(self, status):
        dct = {"Easy":["OFF","OFF"],"Normal":["OFF","OFF","ON"],"Hard":["OFF","OFF","ON","Eaea"]}
        self.ran = dct[status]
        self.restart_program()
    
    def pressed(self, button):
        self.move +=1
        self.Moves.config(text = f"Moves\n{self.move}")
        first = button
        lst = [first]
        try:
            second = e.index([e[button-1][0],e[button-1][1]+1])+1
            lst.append(second)
        except(ValueError):
            pass
        try:
            third = e.index([e[button-1][0],e[button-1][1]-1])+1
            lst.append(third)
        except(ValueError):
            pass
        try:
            four = e.index([e[button-1][0]+1,e[button-1][1]])+1
            lst.append(four)
        except(ValueError):
            pass
        try:
            five = e.index([e[button-1][0]-1,e[button-1][1]])+1
            lst.append(five)
        except(ValueError):
            pass
        for i in lst:
            if self.buttons[i]["text"] == "OFF":
                self.buttons[i]['text'] = 'ON'
                self.buttons[i]['bg'] = 'Yellow'
                self.buttons[i]["fg"] = "Black"
                self.count +=1
            else:
                self.buttons[i]['text'] = 'OFF'
                self.buttons[i]['bg'] = 'Gray'
                self.buttons[i]["fg"] = "White"
                self.count -=1
        if self.count == Turn_Light.row*Turn_Light.column:
            self.game_over()

    def game_over(self):
        showinfo("You won", "Congratulations you passed the game!")
        for i in range(1,Turn_Light.row*Turn_Light.column+1):
            self.buttons[i]["state"] = "disabled"

    def restart_program(self):
        self.move = 0
        self.count = 0
        self.Moves.destroy()
        self.text.destroy()
        for i in range(1,len(self.buttons)+1):
            self.buttons[i].destroy()
        self.createWidgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = Turn_Light(master=root)
    app.mainloop()
