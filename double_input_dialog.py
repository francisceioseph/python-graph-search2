from Tkinter import *


class DoubleInputDialog:
	def __init__(self, parent, message_one, message_two):
		self.value = None
		self.parent = parent
		self.top = Toplevel(parent)
		self.top.wm_title('Input')
		
		self.label = Label(self.top, text = message_one, justify=LEFT)
		self.label.pack(padx=10, pady=8)

		self.entry = Entry(self.top)
		self.entry.pack(padx=10, pady=8)

		self.label2 = Label(self.top, text = message_two, justify=LEFT)
		self.label2.pack(padx=10, pady=8)

		self.entry2 = Entry(self.top)
		self.entry2.pack(padx=10, pady=8)

		self.button = Button(self.top, text='OK', command=self.on_ok_click)
		self.button.pack(pady=8)

	def show(self):
		self.parent.wait_window(self.top)
		return self.value

	def on_ok_click(self):
		self.value = (self.entry.get(), self.entry2.get())
		self.top.destroy()
