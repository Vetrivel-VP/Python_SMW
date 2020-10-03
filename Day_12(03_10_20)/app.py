import tkinter as tk
import os

root = tk.Tk()


def calc_add():
    # get() : Gets the value from the text box in the string format
    result = eval(a_text.get()) + eval(b_text.get())

    ans.configure(text="Answer : "+a_text.get()+" + " +
                  b_text.get() + " = " + str(result))


def clear_btn():
    a_text.delete(first=0, last=100)
    b_text.delete(first=0, last=100)
    a_text.focus()
    ans.configure(text="")


canvas = tk.Canvas(root, height=600, width=400, bg="#263d42")
canvas.pack()

#frame : Frame()

frame = tk.Frame(root, bg="#3e646c")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

# Label()
lbl_heading = tk.Label(
    frame, text="Addition of Two Numbers", bg="#3e646c", fg="White")
lbl_heading.place(x=80, y=20)

# label 1 : Enter the value of a:

lbl_a = tk.Label(frame, text="Enter the value of a", bg="#3e646c", fg="White")
lbl_a.place(x=20, y=80)

# label2 : Enter the value of b
lbl_b = tk.Label(frame, text="Enter the value of b", bg="#3e646c", fg="White")
lbl_b.place(x=20, y=120)

# Text Box  : Entry()
a_text = tk.Entry(frame, width=20, bd=1)
a_text.place(x=170, y=80)

# Text Box  : Entry()
b_text = tk.Entry(frame, width=20, bd=1)
b_text.place(x=170, y=120)

#button : Button()
cal_btn = tk.Button(frame, text="ADD", padx=25,
                    pady=5, bg="#263d42", fg="White", command=calc_add)
cal_btn.place(x=50, y=170)

#button : Button()
clr_btn = tk.Button(frame, text="CLEAR", padx=25,
                    pady=5, bg="#263d42", fg="White", command=clear_btn)
clr_btn.place(x=170, y=170)

# Label()
ans = tk.Label(
    frame, text="", bg="#3e646c", fg="White")
ans.place(x=80, y=220)


root.mainloop()


# def calc_add():
#     # get() : Gets the value from the text box in the string format
#     result = eval(a_text.get()) + eval(b_text.get())

#     ans.configure(text="Answer : "+a_text.get()+" + " +
#                   b_text.get() + " = " + str(result))
