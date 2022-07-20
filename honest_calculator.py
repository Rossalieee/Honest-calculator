msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

oper_list = ["+", "-", "*", "/"]

memory = 0

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2) == True:
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 ==0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)    
        

while True:
    print(msg_0)
    calc = input()

    calc_list = calc.split(" ")

    x = calc_list[0]
    oper = calc_list[1]
    y = calc_list[2]
    
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    
    try:
        x = float(x)
    except ValueError:
        print(msg_1)
        continue
    try:
        y = float(y)
    except ValueError:
        print(msg_1)
        continue   
    if oper not in oper_list:
        print(msg_2)
    else:
        check(x, y, oper)
        if oper == "+":
            result = x + y   
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
    print(float(result))
    print(msg_4)
    user_answer = input()
    if user_answer == "y":
        if is_one_digit(result) == True:
            msg_index = 10
            print(msg_[msg_index])
            user_answer = input()
            while user_answer == "y" and msg_index < 12:
                msg_index += 1
                print(msg_[msg_index])
                user_answer = input()      
    if user_answer == "y":
        memory = float(result)   
    print(msg_5)
    user_answer2 = input()
    if user_answer2 == "y":
        continue
    else:
        break
