from Tkinter import *


class InputDialog:
	def __init__(self, parent, message):
		self.value = None
		self.parent = parent
		self.top = Toplevel(parent)
		self.top.wm_title('Input')
		
		self.label = Label(self.top, text = message, justify=LEFT)
		self.label.pack(padx=10, pady=8)

		self.entry = Entry(self.top)
		self.entry.pack(padx=10, pady=8)

		self.button = Button(self.top, text='OK', command=self.on_ok_click)
		self.button.pack(pady=8)

	def show(self):
		self.parent.wait_window(self.top)
		return self.value

	def on_ok_click(self):
		self.value = self.entry.get()
		self.top.destroy()
