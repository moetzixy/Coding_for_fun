import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Demo")
window.geometry("300x300")

# title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 24")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame, width = 7)
button = ttk.Button(master = input_frame, text = "Convert")
# run
window.mainloop()
