import tkinter as tk
from novelai import main
import asyncio


def run_main():
    asyncio.run(main())
    with open('story.txt', 'r') as file:
        content = file.read()
    novelaiPrinting.config(text=content)
    label.config(text="Finished writing.")

def on_button_click():
    label.config(text="Writing...")
    root.after(0, run_main)


root = tk.Tk()
root.title("My Simple GUI")
root.geometry("300x200")

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

novelaiPrinting = tk.Label(root, text="", wraplength=250)
novelaiPrinting.pack()

root.mainloop()
