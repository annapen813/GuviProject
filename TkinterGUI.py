
import tkinter as tk

def createButton():
    r = tk.Tk()
    r.title('Python GUI')
    button = tk.Button(r, text='Option', width=25, command=r.destroy)
    button.pack()
    r.mainloop()


createButton()