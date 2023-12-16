import random
SYMBOLS = ['A', 'B', 'C', 'D']

# Depositing the amount the user wants to bet with
def deposit():
    amount = input("How much money would you like to deposit in the bank? $")
    if amount.isdigit(): 
        amount = int(amount)
        if 0 < amount <= 100:
            print(f"You deposited ${amount} for playing")
        else:
            print("Please enter a proper amount")
    else:
        print("Please enter a valid number")
        
    return amount

# How many lines do they want to bet on
def lines_to_bet():
        lines = input("How many lines do you want to bet on? (1-3) ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= 3:
                print(f"You bet on {lines} lines for playing")
            else:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")
            
        return lines
    
def bet(lines):
    bet_per_line = input("How much would you like to bet per line? $")
    if bet_per_line.isdigit():
        total_bet = int(bet_per_line) * lines
        return total_bet
    else:
        print("Please enter a valid bet amount")
        
def play_slot_machine():
    line1 = [random.choice(SYMBOLS) for _ in range(3)]
    line2 = [random.choice(SYMBOLS) for _ in range(3)]
    line3 = [random.choice(SYMBOLS) for _ in range(3)]

    # Print the slot machine result
    print("\nSlot Machine Result:\n")
    print(" ".join(line1))
    print(" ".join(line2))
    print(" ".join(line3))

    # Check for winning conditions
    if all(symbol == line1[0] for symbol in line1) or \
       all(symbol == line2[0] for symbol in line2) or \
       all(symbol == line3[0] for symbol in line3):
        return True
    else:
        return False

def main():
    balance = deposit()
    while True:
        if 0 < balance <= 100:
            print("Valid amount, let's proceed.")
        else:
            continue  # Restart the loop to ask for a valid balance

        while True:
            lines_count = lines_to_bet()  # Call lines_to_bet to get the number of lines
            if 0 < lines_count <= 3:
                break  # Break out of the loop when a valid number of lines is provided
            else:
                continue
                
        while True:
            total_bet_amount = bet(lines_count)  # Call bet and pass the number of lines as an argument
            if total_bet_amount > balance:
                print("Your bet amount is greater than the deposit.")
            else:
                print("Total bet amount:$", total_bet_amount)
                break  # Break out of the inner loop when the bet amount is valid
            
        # Play the slot machine
        if play_slot_machine():
            print("\nCongratulations! You won!")
            balance += total_bet_amount  # Add the winning amount to the balance
        else:
            print("\nSorry, you didn't win this time.")
            balance -= total_bet_amount

        print("Updated balance:", balance)  # Display the updated balance

        while True:
            new_game = input("Would you like to play another round? Please enter Y or N ")
            if new_game.upper() == 'Y':
                print(f"Your current balance is ${balance}")
                break# Continue with the next round
            elif new_game.upper() == 'N':
                print("It was nice playing with you. Goodbye!")
                break  # Exit the loop if the user doesn't want to play another round
            else:
                print("Invalid input. Please enter Y or N.")

        if balance ==0:
            new= input("Would you like to deposit more? Y or N ")
            if new.upper()=='Y':
                main()
            else:
                print("Since your balance is $0, game over.")
                break

main()
