from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('570x600')
window.resizable(False, False)
window.configure(bg="#17161b")

equation = ""


# action listener functions
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = " "
    label_result.config(text=equation)


def calc():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)


def remove_last():
    global equation
    label_result.config(text=equation[:-1])


label_result = Label(window, width=25, height=2, text="", font=("arial", 30))
label_result.pack()
# first row from the top buttons
Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
Button(window, text="*", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=290, y=100)
Button(window, text="clear", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: remove_last()).place(x=430, y=100)

# second row from the top buttons
Button(window, text="7", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(window, text="8", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(window, text="9", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(window, text="-", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

# third row from the top buttons
Button(window, text="4", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(window, text="5", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(window, text="6", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(window, text="+", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

# fourth row from the top buttons
Button(window, text="1", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(window, text="2", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(window, text="3", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)

# fifth row from the top buttons
Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=10, y=500)
Button(window, text="0", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=150, y=500)
Button(window, text=".", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)

# equal sign button
Button(window, text="=", width=5, height=3, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#fe9037", command=lambda: calc()).place(x=430, y=405)

window.mainloop()
