import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result
        except Exception as e:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

expression = ""
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=8, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(expand=True, fill='both')
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 18", height=2, width=6)
        btn.pack(side=tk.LEFT, expand=True, fill='both')
        btn.bind("<Button-1>", click)

root.mainloop()
