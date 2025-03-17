from tkinter import *
import math

MAINBG = 'dodgerblue'
MAINFG = 'white'
MAINBG1 = 'SkyBlue'
MAINFG1 = 'RoyalBlue'
BLACK = '#444849'
LIGHT_GRAY = "silver"
MAINFONT = ('arial', 14)


def itog(value, znak):
    s = value.split(znak)
    x = s[1]
    y = x[:x.find('%')]
    rezult = eval(s[0] + znak + y + '*(' + s[0] + '/100)')
    return rezult


def per_define(value):
    znak = 'N'
    if '+' in value:
        znak = '+'
        calcpercent = itog(value, znak)
    elif '-' in value:
        znak = '-'
        calcpercent = itog(value, znak)
    elif '*' in value:
        znak = '*'
        calcpercent = itog(value, znak)
    elif '/' in value:
        znak = '/'
        calcpercent = itog(value, znak)
    else:  # '%' in value:
        s = value.split('%')
        calcpercent = eval(s[0].strip() + '*(' + s[1].strip() + '/100)')
    return calcpercent


def click(value):
    ex = calcentry.get()
    answer = ''
    try:
        if value == 'C':
            answer = ex[0:len(ex) - 1]

        elif value == 'CE':
            answer = ''

        elif value == '\u221A':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cos0':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tan0':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sin0':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            calcentry.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == 'rad':
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log':
            answer = math.log10(eval(ex))

        elif value == 'n!':
            answer = math.factorial(round(eval(ex)))

        elif value == chr(247):
            calcentry.insert(END, '/')
            return

        elif value == '=':
            if '%' in ex:
                answer = per_define(ex)
            else:
                answer = eval(ex)

        else:
            calcentry.insert(END, value)
            return

        calcentry.delete(0, END)
        calcentry.insert(0, answer)

    except SyntaxError:
        pass


root = Tk()
root.title('Калькулятор')
root.config(bg=MAINBG)
root.iconbitmap('calc.ico')
root.geometry('536x370+500+200')
logoimg = PhotoImage(file='calculator_.png')
logolabel = Label(root, image=logoimg, bg=MAINBG)
logolabel.grid(row=0, column=0)

calcentry = Entry(root, font=('arial', 18, 'bold'), bg=LIGHT_GRAY, fg=BLACK, bd=3, relief=SUNKEN, width=30,
                  justify='right')
calcentry.grid(row=0, column=0, pady=5, columnspan=8)

# microimg = PhotoImage(file='microphone_.png')
# microlabel = Button(root, image=microimg, bd=0, bg=MAINBG, activebackground=MAINBG)
# microlabel.grid(row=0, column=7)

button_text = ['C', 'CE', '\u221A', '%', 'π', 'cos0', 'tan0', 'sin0',
               '1', '2', '3', '+', '2π', 'cosh', 'tanh', 'sinh',
               '4', '5', '6', '-', chr(8731), 'x\u02b8', 'x\u00B3', 'x\u00B2',
               '7', '8', '9', '*', 'ln', 'deg', 'rad', 'e',
               '0', '.', '=', chr(247), 'log', '(', ')', 'n!']

row_val = 1
col_val = 0
for i in button_text:
    button = Button(root, width=5, height=2, bd=2, bg=MAINBG1, fg=MAINFG1, relief=RAISED,
                    text=i, font=MAINFONT, activebackground=BLACK, command=lambda button=i: click(button))
    button.grid(row=row_val, column=col_val, padx=1, pady=1)
    if row_val > 1 and col_val < 4:
        button['bg'] = MAINBG
        button['fg'] = MAINFG
    else:
        button['bg'] = MAINBG1
        button['fg'] = MAINFG1
    col_val += 1

    if col_val > 7:
        row_val += 1
        col_val = 0

root.mainloop()
