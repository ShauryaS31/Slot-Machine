import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(colunms, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = colunms[0][line]
        for column in colunms:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol_to_check] * bet
            winning_line.append(line +1)
    return winnings, winning_line  
    
        
        
        
        
def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row] , end=" | ")
            else:
                print(column[row], end="")
        print()

def deposite():
    while True:
        amount = input("how much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid deposit amount. Please enter a positive number.")
        else:
            print("Please enter a numner")
    
    return amount

def get_num_of_line():
    while True:
        lines = input("ENter teh number of line to bet on(1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    
    return lines

def get_bet():
    while True:
        amount = input("how much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must eb between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a numner")
    
    return amount
    
    
def spin(balance):
    lines = get_num_of_line()
    while True:
        bet = get_bet()
        total_bet = bet *lines
            
        if total_bet> balance:
            print(f"You do not have enough balance, you curretn balance is {balance}")
        else:
            break
    
    
        
    print(f"You are betting ${bet} on {lines} lines.\nTotal bet is equal to: ${total_bet}")
        
    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_line = check_winning(slots, lines, bet, symbol_value)
    print(f"Tou Won ${winning}!!")
    print(f"Tou Won on lines", *winning_line)
    return winning -total_bet


def main():
    balance = deposite()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Pres s Enter to paly (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")

    
    
main()