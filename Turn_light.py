import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

class Turn_Light(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("First GUI") #Controls the window title.
        master.geometry("350x350+200+200") #size
        self.pack()
        self.createWidgets()
        text = tk.Label(self, text="LIGHT OUT",fg="Black",font=('Helvetica bold', 26))
        text.place(x=1,y= 20)
        self.move = 0
        self.Moves = tk.Button(self, text=f"Moves\n{self.move}",width=7,height=2,state="disabled")
        self.Moves.grid(row = 2, column = 7 ,padx=(25,0))
        self.count = 0
        master.resizable(False, False)
        icon_1 = Image.open("light_on\img.png")
        photo = ImageTk.PhotoImage(icon_1)
        root.wm_iconphoto(False, photo)

    def createWidgets(self):
        floors = [i for i in range(1,26)]
        self.buttons = {}
        global e
        e = []
        xPos = 0
        yPos = 0
        for floor in floors:
            if(yPos == 5):
                xPos = xPos + 1
                yPos = 0
            if (xPos == 0):
                self.buttons[floor] = tk.Button(self, width=4,height=2,bg="Grey",fg= "White", text="OFF", 
                                                    command = lambda f=floor: self.pressed(f))
                self.buttons[floor].grid(row=xPos, column =yPos,pady=(80,0))
                e.append([xPos,yPos])
                yPos = yPos +1
            else:
                self.buttons[floor] = tk.Button(self, width=4,height=2,bg="Grey",fg= "White", text="OFF", 
                                                    command = lambda f=floor: self.pressed(f))
                self.buttons[floor].grid(row=xPos, column =yPos)
                e.append([xPos,yPos])
                yPos = yPos +1
        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                    command=root.destroy,width=7,height=2).grid(row = 4, column = 7 ,padx=(25,0))
        self.restart = tk.Button(self, text="RESTART", fg="red",
                    command=self.restart_program,width=7,height=2).grid(row =3, column = 7 ,padx=(25,0))

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
        if self.count == 25:
            self.game_over()

    def game_over(self):
        showinfo("You won", "Congratulations you passed the game!")
        for i in range(1,26):
            self.buttons[i]["state"] = "disabled"

    def restart_program(self):
        self.createWidgets()
        self.move = 0
        self.Moves.config(text = f"Moves\n{self.move}")
        self.count = 0
if __name__ == "__main__":
    root = tk.Tk()
    app = Turn_Light(master=root)
    app.mainloop()
