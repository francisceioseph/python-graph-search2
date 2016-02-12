from Tkinter import *
from main_window import MainWindow


root = Tk()
main_window = MainWindow(root)

root.wm_title('Graphs')
root.resizable(width=FALSE, height=FALSE)
root.minsize(width=600, height=350)
root.mainloop()