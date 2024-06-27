from tkinter import *
import tkinter.font as font
import math

# globally declare the expression variable
g_expression = ""

# setting maximum number of digits in final result and storing it in a global variable
g_max_answer_length = 10

# parameter for identification numbers in expression to be evaluated, using loops; storing it in a global variable
g_num_parameter = ['+', '-', '//', '**', '/', '*', '(']


# function to get result of various operstions
def otherfunctions(op_argumnt):
    global g_expression
    length = len(g_expression)
    disp_msg = ''
    global g_num_parameter
    try:
        ck_paramtr = 0
        for traverse in range(length - 1, -1, -1):
            if g_expression[traverse] not in g_num_parameter:
                ck_paramtr += 1
            else: break
        if float(g_expression[length - ck_paramtr:]) % (math.pi / 2) == 0.0:
            number = (math.pi / 2) * (int(float(g_expression[length - ck_paramtr:]) / (math.pi / 2)))
        else:
            number = float(g_expression[length - ck_paramtr:])
        ans = ''
        if op_argumnt == 's':
            ans = str(math.sin(number))
        elif op_argumnt == 'c':
            ans = str(math.cos(number))
        elif op_argumnt == 't':
            if int(number / (math.pi / 2)) % 2 != 0 and str(float(number / (math.pi / 2))).split('.')[1] == '0':
                disp_msg = 'not defined!'
            else:
                ans = str(math.tan(number))
        elif op_argumnt == 'e':
            ans = str(math.exp(number))
        elif op_argumnt == 'l10':
            if number > 0 and g_expression[0:(length - ck_paramtr)].strip() != '-':
                ans = str(math.log10(number))
            else:
                disp_msg = 'not defined!'
        elif op_argumnt == 'fl':
            ans = str(math.floor(number))
        elif op_argumnt == 'ln':
            if number > 0 and g_expression[0:(length - ck_paramtr)].strip() != '-':
                ans = str(math.log(number))
            else:
                disp_msg = 'not defined!'
        if disp_msg != 'not defined!':
            g_expression = g_expression[0:(length - ck_paramtr)] + ans
            equation.set(g_expression)
        else:
            g_expression = ''
            equation.set(disp_msg)
    except:
        g_expression = ''
        equation.set('sorry error!')


# function to evaluate the expression inside of round brackets
def bracketop():
    global g_expression
    ck_paramtr = 0
    # try and catch block to generate and find the error
    try:
        expresn_in_brackt = ''
        if '(' in g_expression:
            for traverse in range(len(g_expression) - 1, 0, -1):
                if g_expression[traverse] == '(':
                    ck_paramtr = traverse
                    break
            expresn_in_brackt = str(eval(g_expression[ck_paramtr + 1:]))
        else:
            expresn_in_brackt = str(eval(g_expression))
        g_expression = g_expression[:ck_paramtr] + expresn_in_brackt
        equation.set(g_expression)
    except:
        g_expression = ''
        equation.set('')


# function to get the factorial of the preceeding number
def factoriall():
    # global expression
    global g_expression
    global g_max_answer_length
    global g_num_parameter
    if g_max_answer_length in range(0, 11):
        max_num = 13
    else:
        max_num = 21
    # try and catch block to generate and find the error
    try:
        ck_paramtr = 0
        disp_msg = ''
        length = len(g_expression)
        for i in range(length - 1, -1, -1):
            if g_expression[i] not in g_num_parameter:
                ck_paramtr += 1
            else:
                break
        if g_expression[0:(length - ck_paramtr)][
           len(g_expression[0:(length - ck_paramtr)]) - 2:] == '(-' or g_expression[0:(length - ck_paramtr)] == '-':
            disp_msg = 'Factorial of negative number does not exist!!'
        else:
            if '.' in g_expression[(length - ck_paramtr):] and g_expression[(length - ck_paramtr):].split('.')[1].count(
                    '0') != len(g_expression[(length - ck_paramtr):].split('.')[1]):
                disp_msg = 'Factorial for decimal numbers does not exist!!'
            else:
                if int(g_expression[length - ck_paramtr:].split('.')[0]) <= max_num:
                    g_expression = g_expression[0:(length - ck_paramtr)] + str(
                        math.factorial(int(g_expression[(length - ck_paramtr):].split('.')[0])))
                    equation.set(g_expression)
                else:
                    disp_msg = 'out of range!!'

        if len(disp_msg) > 0:
            g_expression = ''
            equation.set(disp_msg)


    except:
        equation.set('sorry,error!')
        g_expression = ''


# function to update expression in the text entry box
def press(num):
    # point out the global expression variable
    global g_expression

    operator = ''
    if num==math.e or num==math.pi:
        if g_expression!='':
            if '0'<=g_expression[-1]<='9': operator='*'

    # concatenation of string
    g_expression = g_expression+operator+str(num)

    # update the expression by using set method
    equation.set(g_expression)


# function to evaluate the final expression
def equalpress():
    # Put that code inside the try block which may generate the error
    global g_expression
    global g_max_answer_length
    try:
        # global expression
        if len(g_expression) == 0:
            g_expression = '0'
            equation.set(g_expression)

        if g_expression.count('(') != g_expression.count(')'):
            if g_expression.count('(') > g_expression.count(')'):
                for traverse in range(g_expression.count('(') - g_expression.count(')')):
                    g_expression += ')'
            else:
                for traverse in range(g_expression.count(')') - g_expression.count('(')):
                    g_expression = '(' + g_expression

        # eval function evaluate the expressionand str function convert the result into string
        total = str(eval(g_expression))

        if ('.' in total and len(total.split('.')[0]) <= g_max_answer_length) or (len(total) <= g_max_answer_length):
            if total.split('.')[0] == '-0' and total.split('.')[1] == '0':
                total = '0'
            equation.set(total)

            # initialize the expression variable by previous result to perform further calculation, if any!
            g_expression = total
        else:
            g_expression = ''
            equation.set('out of range!')
    # if error is generate then handle by the except block
    except:

        equation.set("sorry, its an error ")
        g_expression = ""


# function to undo/clear/backspace the previous character just entered
def erase():
    global g_expression
    if len(g_expression) != 0:
        g_expression = g_expression[0:len(g_expression) - 1]
    equation.set(g_expression)


# function to clear the contents of text entry box
def clear():
    global g_expression
    g_expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # creating a GUI window
    window = Tk()

    # setting background colour of the GUI window
    window.configure(background='grey')

    # setting the title of the GUI
    window.title("Scientific Calculator")

    # setting the size configuration of the GUI window
    window.geometry("360x640")

    # locking the size of the GUI window, such that the user cannot expand or contract it with respect to its size
    window.resizable(width=False, height=False)

    # selecting font size and style for the text in the buttons
    myfont = font.Font(size=13, weight='bold')

    # StringVar() is the variable class we create an instance of this class
    equation = StringVar()

    # create the text entry box for showing the expression
    exprfld_bg_color = 'dark blue'
    exprfld_fg_color = 'white'
    expression_field = Entry(window, textvariable=equation, bg=exprfld_bg_color, fg=exprfld_fg_color)
    expression_field['font'] = myfont

    # grid method is used for placing the widgets at respective positions in table like structure
    expression_field.grid(columnspan=4, ipadx=87, ipady=25)

    # setting up the button height and width
    # button height:
    g_butht = 3

    # button width
    g_butwt = 8

    # selecting colours fot the button widgets options are "white", "black", "red","dark red", "green","dark green","dark blue", "blue", "cyan", "yellow", and "magenta"
    # button font color:
    g_butfg = 'black'

    # button background color:
    g_butbg = 'grey'

    # create Buttons and place at a particular grid location using grid method
    button1 = Button(window, text=' 1 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(1), height=g_butht, width=g_butwt)
    button1['font'] = myfont
    button1.grid(row=2, column=0)

    button2 = Button(window, text=' 2 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(2), height=g_butht, width=g_butwt)
    button2['font'] = myfont
    button2.grid(row=2, column=1)

    button3 = Button(window, text=' 3 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(3), height=g_butht, width=g_butwt)
    button3['font'] = myfont
    button3.grid(row=2, column=2)

    button4 = Button(window, text=' 4 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(4), height=g_butht, width=g_butwt)
    button4['font'] = myfont
    button4.grid(row=3, column=0)

    button5 = Button(window, text=' 5 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(5), height=g_butht, width=g_butwt)
    button5['font'] = myfont
    button5.grid(row=3, column=1)

    button6 = Button(window, text=' 6 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(6), height=g_butht, width=g_butwt)
    button6['font'] = myfont
    button6.grid(row=3, column=2)

    button7 = Button(window, text=' 7 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(7), height=g_butht, width=g_butwt)
    button7['font'] = myfont
    button7.grid(row=4, column=0)

    button8 = Button(window, text=' 8 ', fg=g_butfg, bg=g_butbg,
                     command=lambda: press(8), height=g_butht, width=g_butwt)

    button8['font'] = myfont
    button8.grid(row=4, column=1)

    button9 = Button(window, text=' 9 ', fg=g_butfg, bg=g_butbg,
                     command=lambda:press(9), height=g_butht, width=g_butwt)
    button9['font'] = myfont
    button9.grid(row=4, column=2)

    button0 = Button(window, text=' 0 ', bg=g_butbg, fg=g_butfg,
                     command=lambda: press(0), height=g_butht, width=g_butwt)
    button0['font'] = myfont
    button0.grid(row=5, column=0)

    fct = Button(window, text=' ! ', bg=g_butbg, fg=g_butfg,
                 command=lambda: factoriall(), height=g_butht, width=g_butwt)
    fct['font'] = myfont
    fct.grid(row=6, column=1)

    modd = Button(window, text=' % ', bg=g_butbg, fg=g_butfg,
                  command=lambda: press("%"), height=g_butht, width=g_butwt)
    modd['font'] = myfont
    modd.grid(row=6, column=2)

    plus = Button(window, text=' + ', bg=g_butbg, fg=g_butfg,
                  command=lambda: press("+"), height=g_butht, width=g_butwt)
    plus['font'] = myfont
    plus.grid(row=2, column=3)

    minus = Button(window, text=' - ', bg=g_butbg, fg=g_butfg,
                   command=lambda: press("-"), height=g_butht, width=g_butwt)
    minus['font'] = myfont
    minus.grid(row=3, column=3)

    multiply = Button(window, text=' × ', bg=g_butbg, fg=g_butfg,
                      command=lambda: press("*"), height=g_butht, width=g_butwt)
    multiply['font'] = myfont
    multiply.grid(row=4, column=3)

    expwr = Button(window, text='x^y', bg=g_butbg, fg=g_butfg,
                   command=lambda: press("**"), height=g_butht, width=g_butwt)
    expwr['font'] = myfont
    expwr.grid(row=5, column=1)

    divide = Button(window, text=' ÷ ', bg=g_butbg, fg=g_butfg,
                    command=lambda: press("/"), height=g_butht, width=g_butwt)
    divide['font'] = myfont
    divide.grid(row=5, column=3)

    equal = Button(window, text=' = ', bg=exprfld_bg_color, fg=exprfld_fg_color,
                   command=equalpress, height=g_butht, width=g_butwt)
    equal['font'] = myfont
    equal.grid(row=9, column=3)

    erase = Button(window, text=' ⌫ ', bg=g_butbg, fg=g_butfg,
                   command=erase, height=g_butht, width=g_butwt)
    erase['font'] = myfont
    erase.grid(row=7, column=3)

    clear = Button(window, text='Clear', bg=g_butbg, fg=g_butfg,
                   command=clear, height=g_butht, width=g_butwt)
    clear['font'] = myfont
    clear.grid(row=8, column=3)

    Decimal = Button(window, text='.', bg=g_butbg, fg=g_butfg,
                     command=lambda: press('.'), height=g_butht, width=g_butwt)
    Decimal['font'] = myfont
    Decimal.grid(row=6, column=0)

    bracketopen = Button(window, text='(', bg=g_butbg, fg=g_butfg,
                         command=lambda: press('('), height=g_butht, width=g_butwt)
    bracketopen['font'] = myfont
    bracketopen.grid(row=7, column=1)

    bracketclose = Button(window, text=')', bg=g_butbg, fg=g_butfg,
                          command=lambda: bracketop(), height=g_butht, width=g_butwt)
    bracketclose['font'] = myfont
    bracketclose.grid(row=7, column=2)

    pi = Button(window, text='π', bg=g_butbg, fg=g_butfg,
                command=lambda: press(math.pi), height=g_butht, width=g_butwt)
    pi['font'] = myfont
    pi.grid(row=6, column=3)

    sin = Button(window, text='sin(x)', bg=g_butbg, fg=g_butfg,
                 command=lambda: otherfunctions('s'), height=g_butht, width=g_butwt)
    sin['font'] = myfont
    sin.grid(row=8, column=0)

    cos = Button(window, text='cos(x)', bg=g_butbg, fg=g_butfg,
                 command=lambda: otherfunctions('c'), height=g_butht, width=g_butwt)
    cos['font'] = myfont
    cos.grid(row=8, column=1)

    tan = Button(window, text='tan(x)', bg=g_butbg, fg=g_butfg,
                 command=lambda: otherfunctions('t'), height=g_butht, width=g_butwt)
    tan['font'] = myfont
    tan.grid(row=8, column=2)

    exp = Button(window, text='e^x', bg=g_butbg, fg=g_butfg,
                 command=lambda: otherfunctions('e'), height=g_butht, width=g_butwt)
    exp['font'] = myfont
    exp.grid(row=7, column=0)

    log = Button(window, text='log(x)', bg=g_butbg, fg=g_butfg,
                 command=lambda: otherfunctions('l10'), height=g_butht, width=g_butwt)
    log['font'] = myfont
    log.grid(row=9, column=0)

    gif = Button(window, text='[x]', bg=g_butbg, fg=g_butfg,
                 command=lambda: otherfunctions('fl'), height=g_butht, width=g_butwt)
    gif['font'] = myfont
    gif.grid(row=9, column=1)

    ln = Button(window, text='ln(x)', bg=g_butbg, fg=g_butfg,
                command=lambda: otherfunctions('ln'), height=g_butht, width=g_butwt)
    ln['font'] = myfont
    ln.grid(row=9, column=2)

    eulers_constant = Button(window, text='e', bg=g_butbg, fg=g_butfg,
                             command=lambda: press(math.e), height=g_butht, width=g_butwt)
    eulers_constant['font'] = myfont
    eulers_constant.grid(row=5, column=2)

    # start the GUI
    window.mainloop()
