from Coffemachineproject import MENU, resources
money = 0
run_machine = True
espresso = MENU['espresso']['ingredients']
latte = MENU['latte']['ingredients']
capuccino = MENU['cappuccino']['ingredients']
prices = MENU['espresso']['cost'] ,MENU['latte']['cost'] , MENU['cappuccino']['cost']



def coffee_picker(coffee, resources):

    if resources['water'] < coffee['water']:
        print('Sorry there is not enough Water')
        return False
    elif resources['milk'] < coffee['milk']:
        print('Sorry there is not enough Milk')
        return False
    elif resources['coffee'] < coffee['coffee']:
        print('Sorry there is not enough Coffee')
        return False
    return True

def price_checker(price):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: ")) * 0.25
    dime = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    coins_inserted= quarters + dime + nickles + pennies.__round__(3)
    if price > coins_inserted:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coins_inserted > price:
        change = (coins_inserted-price).__round__(3)
        global money
        money += price
        print(f"Here is the ${change} in change.")
        return True
    else:
        money+=price
        return True

def coffee_maker(coffee,resources,coffe_name):
    resources['water'] -= coffee['water']
    resources['milk'] -= coffee['milk']
    resources['coffee'] -= coffee['coffee']
    print(f"Here is your {coffee_name}. Enjoy!")




while run_machine:
    command = input("What would you like? (espresso/latte/cappuccino):").lower()
    if command == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money} ")
    elif command == 'off':
        run_machine = False
    else:
        if command == 'espresso':
            price = prices[0]
            coffee = espresso
            coffee_name='espresso'
        elif command == 'latte':
            price = prices[1]
            coffee = latte
            coffee_name='latte'
        else:
            coffee = capuccino
            price = prices[2]
            coffee_name='capuccino'
        if coffee_picker(coffee,resources):
            if price_checker(price):
                coffee_maker(coffee,resources,coffee_name)





