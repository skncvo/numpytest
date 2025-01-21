# import tkinter
# tkinter.Widget = tkinter.Label(None, text = 'I love Python!!')
# tkinter.Widget.pack()

# from tkinter import *

# widget = Label(None, text = 'I love Python!!')
# widget.pack()

# import tkinter
# window = tkinter.Tk()

# window.title('Hello Python')
# window.geometry("300x200+10+20")
# window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Tkinter 예제")

label = tk.Label(window, text="Hello, Tkinter!", height=10, width= 40)
label.pack()

button = tk.Button(window, text="클릭")
button.pack()

window.mainloop()

