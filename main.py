from tkinter import *
import math


exp2 = expression = ""


def press(sth):
    global expression
    expression = expression + str(sth)


def show(sth):
    global exp2
    if str(sth) == "math.pi":
        sth = 'π'
    elif str(sth) == "math.e":
        sth = "e"
    elif str(sth) == "math.sin":
        sth = "sin"
    elif str(sth) == "math.cos":
        sth = "cos"
    elif str(sth) == "math.tan":
        sth = "tan"
    elif str(sth) == "math.cot":
        sth = "cot"
    elif str(sth) == "**":
        sth = "^"
    elif str(sth) == "math.sqrt":
        sth = "√"
    elif str(sth) == "math.tau":
        sth = "τ"
    exp2 = exp2 + str(sth)
    sequence.set(exp2)


def combined(sth):
    press(sth)
    show(sth)


def equal():
    try:
        global expression
        result = str(eval(expression))
        sequence.set(result)
        expression = ""
    except Exception:
        sequence.set(" error ")
        expression = ""


def clear():
    global expression, exp2
    expression = ""
    exp2 = ""
    sequence.set("")


def delete():
    global expression, exp2
    exp2 = exp2[:-1]
    sequence.set(exp2)


gui = Tk()
gui.configure(bg="maroon", padx="50", pady="20")
gui.title("My first Project")
gui.geometry("495x290")
sequence = StringVar()

entryframe = Frame(gui)
entryframe.grid(columnspan=7)

entryscroll = Scrollbar(entryframe, orient=HORIZONTAL, cursor="mouse")
entryscroll.pack(fill=X)

expression_field = Entry(entryframe, selectbackground="steelblue", bg="white", fg="Black", font="Verdana 15", justify="center", textvariable=sequence,
                         xscrollcommand=entryscroll.set)
expression_field.pack()
entryscroll.config(command=expression_field.xview)
sequence.set("Enter a sequence")

button1 = Button(gui, text="1", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(1), height=2, width=8)  # (master, option=value)
button1.grid(row=2, column=2)

button2 = Button(gui, text="2", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(2), height=2, width=8)
button2.grid(row=2, column=3)

button3 = Button(gui, text="3", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(3), height=2, width=8)
button3.grid(row=2, column=4)

button4 = Button(gui, text="4", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(4), height=2, width=8)  # (master, option=value)
button4.grid(row=3, column=2)

button5 = Button(gui, text="5", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(5), height=2, width=8)  # (master, option=value)
button5.grid(row=3, column=3)

button6 = Button(gui, text="6", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(6), height=2, width=8)  # (master, option=value)
button6.grid(row=3, column=4)

button7 = Button(gui, text="7", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(7), height=2, width=8)  # (master, option=value)
button7.grid(row=4, column=2)

button8 = Button(gui, text="8", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(8), height=2, width=8)  # (master, option=value)
button8.grid(row=4, column=3)

button9 = Button(gui, text="9", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(9), height=2, width=8)  # (master, option=value)
button9.grid(row=4, column=4)

button0 = Button(gui, text="0", activebackground="pink", activeforeground="blue", bg="white",
                 fg="black", command=lambda: combined(0), height=2, width=8)  # (master, option=value)
button0.grid(row=5, column=3)

buttonClear = Button(gui, text="Clear", activebackground="pink", activeforeground="blue", bg="white",
                     fg="black", command=lambda: clear(), height=2, width=8)
buttonClear.grid(row=1, column=1)

image = PhotoImage(file="C:\\Users\\ermei\\Desktop\\1222.png")
buttonDelete = Button(gui, image=image, bg="white", command=lambda: delete(), height=35, width=60, justify="center")
buttonDelete.grid(row=1, column=2)

buttonSin = Button(gui, text="Sin", activebackground="pink", activeforeground="blue", bg="white",
                   fg="black", command=lambda: combined("math.sin"), height=2, width=8)
buttonSin.grid(row=1, column=3)

buttonCos = Button(gui, text="Cos", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                   command=lambda: combined("math.cos"), height=2, width=8)
buttonCos.grid(row=1, column=4)

buttonTan = Button(gui, text="Tan", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                   command=lambda: combined("math.tan"), height=2, width=8)
buttonTan.grid(row=1, column=5)

buttonCot = Button(gui, text="Cot", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                   command=lambda: combined("math.cot"), height=2, width=8)
buttonCot.grid(row=1, column=6)

buttonDot = Button(gui, text=".", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                   command=lambda: combined("."), height=2, width=8)
buttonDot.grid(row=5, column=4)

buttonPlus = Button(gui, text="+", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                    command=lambda: combined("+"), height=2, width=8)
buttonPlus.grid(row=2, column=5)

buttonMinus = Button(gui, text="-", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                     command=lambda: combined("-"), height=2, width=8)
buttonMinus.grid(row=3, column=5)

buttonMultiply = Button(gui, text="*", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                        command=lambda: combined("*"), height=2, width=8)
buttonMultiply.grid(row=4, column=5)

buttonDivide = Button(gui, text="/", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                      command=lambda: combined("/"), height=2, width=8)
buttonDivide.grid(row=5, column=5)

buttonEqual = Button(gui, text="=", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                     command=lambda: equal(), height=2, width=8)
buttonEqual.grid(row=2, column=6)

buttonSqr = Button(gui, text="√", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                   command=lambda: combined("math.sqrt"), height=2, width=8)
buttonSqr.grid(row=4, column=6)

buttonPower = Button(gui, text="^", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                     command=lambda: combined("**"), height=2, width=8)
buttonPower.grid(row=3, column=6)

buttonEuler = Button(gui, text="e", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                     command=lambda: combined("math.e"), height=2, width=8)
buttonEuler.grid(row=2, column=1)

buttonPi = Button(gui, text="π", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                  command=lambda: combined("math.pi"), height=2, width=8)
buttonPi.grid(row=3, column=1)

buttonTau = Button(gui, text="τ", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                   command=lambda: combined("math.tau"), height=2, width=8)
buttonTau.grid(row=4, column=1)

buttonPare1 = Button(gui, text="(", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                     command=lambda: combined("("), height=2, width=8)
buttonPare1.grid(row=5, column=1)

buttonPare2 = Button(gui, text=")", activebackground="pink", activeforeground="blue", bg="white", fg="black",
                     command=lambda: combined(")"), height=2, width=8)
buttonPare2.grid(row=5, column=2)

buttonEmpty = Button(gui, state="disabled", bg="white", height=2, width=8)
buttonEmpty.grid(row=5, column=6)

gui.mainloop()

