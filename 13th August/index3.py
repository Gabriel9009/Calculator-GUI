import tkinter as tk

window = tk.Tk()

e = tk.Entry(window, width=35, borderwidth=10)

e.grid(row=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current + str(number))

def add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, tk.END)

def equal():
    second_number = e.get()
    e.delete(0, tk.END)
    e.insert(0, f_num + int(second_number))
    
def clear():
    e.delete(0, tk.END)

button1 = tk.Button(window, text='1', padx=40, pady=20, command=lambda:button_click(1))

button2 = tk.Button(window, text='2', padx=40, pady=20, command=lambda:button_click(2))

button3 = tk.Button(window, text='3', padx=40, pady=20, command=lambda:button_click(3))
button4 = tk.Button(window, text='4', padx=40, pady=20, command=lambda:button_click(4))
button5 = tk.Button(window, text='5', padx=40, pady=20, command=lambda:button_click(5))
button6 = tk.Button(window, text='6', padx=40, pady=20, command=lambda:button_click(6))
button7 = tk.Button(window, text='7', padx=40, pady=20, command=lambda:button_click(7))
button8 = tk.Button(window, text='8', padx=40, pady=20, command=lambda:button_click(8))
button9 = tk.Button(window, text='9', padx=40, pady=20, command=lambda:button_click(9))
button0 = tk.Button(window, text='0', padx=40, pady=20, command=lambda:button_click(0))


button_add = tk.Button(window, text='+', padx=40, pady=20, command=add)

button_equal = tk.Button(window, text='=', padx=40, pady=20, command=equal)

button_clear = tk.Button(window, text='CLS',  padx=40, pady=20, command=clear)


button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

window.mainloop()