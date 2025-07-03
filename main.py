
# Python Slot Machine

import random

def spin_row():
    symbols = ['🍒',  '🍉',  '🍋',  '🔔',  '🌟']

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 8
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🌟':
            return bet * 20
    return 0

def main():
    balance = 100
    print("******************************")
    print("Welcome to python slot machine")
    print("Symbols : 🍒  🍉  🍋  🔔  🌟  ")
    print("******************************")

    while balance > 0:
        print(f"Your current balance :{balance}$")

        bet = input("Enter a bet You need to Place: ")

        if not bet.isdigit():
            print("Please Enter a valid Amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Your bet cannot be greater than balance")
            continue

        if bet <= 0:
            print("Your bet should be greater than zero")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...  \n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won!!!!!!!! : {payout}$")
        else:
            print("You Lost!!!!!!!!!")

        balance += payout

        play_again = input("Do u Want to play again (Y/N): ").upper()
        if play_again == "Y":
            continue
        else:
            print(f"game over ; YOU're Balance is {balance}$")
            break
    if balance == 0:
        print(f"game over ; YOU're Balance is {balance}$")

if __name__ == '__main__':
    main()























