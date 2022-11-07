water_amount = 400
milk_amount = 540
beans_amount = 120
cups = 9
money = 550

action_msg = "Write action (buy, fill, take, remaining, exit):"
buy_msg ="What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
fill_water_msg = "Write how many ml of water you want to add:"
fill_milk_msg = "Write how many ml of milk you want to add:"
fill_beans_msg = "Write how many grams of coffee beans you want to add:"
fill_cups_msg = "Write how many disposable cups you want to add:"
take_msg = f"I gave you ${money}"
machine_state_msg = f"""The coffee machine has:
{water_amount} ml of water
{milk_amount} ml of milk
{beans_amount} g of coffee beans
{cups} disposable cups
${money} of money"""
making_coffee_msg = "I have enough resources, making you a coffee!"

espresso_price = 4
espresso_water = 250
espresso_beans = 16

latte_price = 7
latte_water = 350
latte_milk = 75
latte_beans = 20

cappuccino_price = 6
cappuccino_water = 200
cappuccino_milk = 100
cappuccino_beans = 12

def making_espresso():
    global water_amount
    global milk_amount
    global beans_amount
    global  cups
    global money
    
    if water_amount < espresso_water:
        print("Sorry, not enough water!")
    elif beans_amount < espresso_beans:
        print("Sorry, not enough coffee beans!")
    else:
        water_amount -= espresso_water
        beans_amount -= espresso_beans
        money += espresso_price
        cups -= 1
        print(making_coffee_msg)

def making_latte():
    global water_amount
    global milk_amount
    global beans_amount
    global  cups
    global money
    
    if water_amount < latte_water:
        print("Sorry, not enough water!")
    elif milk_amount < latte_milk:
        print("Sorry, not enough milk!")
    elif beans_amount < latte_beans:
        print("Sorry, not enough coffee beans!")
    else:
        water_amount -= latte_water
        milk_amount -= latte_milk
        beans_amount -= latte_beans 
        money += latte_price
        cups -= 1
        print(making_coffee_msg)
        
def making_cappuccino():
    global water_amount
    global milk_amount
    global beans_amount
    global  cups
    global money
    
    if water_amount < cappuccino_water:
        print("Sorry, not enough water!")
    elif milk_amount < cappuccino_milk:
        print("Sorry, not enough milk!")
    elif beans_amount < cappuccino_beans:
        print("Sorry, not enough coffee beans!")
    else:
        water_amount -= cappuccino_water
        milk_amount -= cappuccino_milk
        beans_amount -= cappuccino_beans 
        money += cappuccino_price
        cups -= 1
        print(making_coffee_msg)
        
def buy():  
    print(buy_msg)
    user_input = input()
    if user_input == "1":
      making_espresso()  
    elif user_input == "2":
        making_latte()
    elif user_input == "3":
        making_cappuccino()
    else:
        pass   

def fill():
    global water_amount
    global milk_amount
    global beans_amount
    global  cups
    
    print(fill_water_msg)
    water_amount += int(input())
    print(fill_milk_msg)
    milk_amount += int(input())
    print(fill_beans_msg)
    beans_amount += int(input())
    print(fill_cups_msg)
    cups += int(input())

def take():
    global money
    
    print(take_msg)
    money = 0
    
def refresh_message():
    global machine_state_msg
    machine_state_msg = f"""The coffee machine has:
    {water_amount} ml of water
    {milk_amount} ml of milk
    {beans_amount} g of coffee beans
    {cups} disposable cups
    ${money} of money"""

def machine_state():
    print(machine_state_msg)

while True:
    print(action_msg)
    action = input()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        refresh_message()
        machine_state()
    else:
        break