import random

def blackjack():
    
     deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
     player=[]
     computer=[]
     for i in range(2):
          player.append(random.choice(deck))
          computer.append(random.choice(deck))
     print( 'YOUR cards are',player)
     print('one of  his card is ',computer[0])
     player_hand_value=player[0]+player[1]
     comp_hand_value=computer[0]+computer[1]
    
     play=input('Do you want to hit or stand : ').lower()
    
     if play=='stand':
        
             if player_hand_value > comp_hand_value:
                 print('You win')
             elif player_hand_value < comp_hand_value:
                 print('Dealer wins')
             elif player_hand_value==comp_hand_value:
                 print('draw')
            
     elif play=='hit':
         player.append(random.choice(deck))
         player_hand_value = player_hand_value+player[2]
         if player_hand_value > 21 and 11  in player :
                 player_hand_value= player_hand_value-10
         print('Your hand is ',player)
         if comp_hand_value < 17:
             print('Dealer also hits')
             computer.append(random.choice(deck))
             comp_hand_value = comp_hand_value + computer[2]
             if comp_hand_value > 21 and 11  in computer :
                 comp_hand_value= comp_hand_value-10
             
             print("Dealer's hand is ",computer)
             if player_hand_value < 22 and comp_hand_value < 22:
                 if player_hand_value > comp_hand_value:
                     print('You win')
                 elif player_hand_value < comp_hand_value:
                     print('Dealer wins')
                 elif player_hand_value==comp_hand_value:
                     print('draw')
    
             elif comp_hand_value > 21:
                 if player_hand_value > 21:
                     print('draw')
                 else:
                     print('you win')
             elif player_hand_value > 21:
                 if comp_hand_value < 22:
                     print('dealer win')
                
                
         elif comp_hand_value > 17:
             print('Dealer chooses to stand')
             print('Your hand is ',player)
            
             if player_hand_value < 22 :
                 if player_hand_value > comp_hand_value:
                     print('You win')
                 elif player_hand_value < comp_hand_value:
                     print('Dealer wins')
                 elif player_hand_value==comp_hand_value:
                     print('draw')
             elif player_hand_value > 21 :
                 print('Dealer Wins')



while True:
     run=input('Play or Exit :').lower()
     if run == 'play' :
         blackjack()
     else:
         break
# modified code
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = """
 ____  _            _    _            _    
|  _ \| |          | |  | |          | |   
| |_) | | __ _  ___| | _| | ___   ___| | __
|  _ <| |/ _` |/ __| |/ / |/ _ \ / __| |/ /
| |_) | | (_| | (__|   <| | (_) | (__|   < 
|____/|_|\__,_|\___|_|\_\_|\___/ \___|_|\_\\
         BLACKJACK GAME – BEAT THE DEALER!
"""

def blackjack():
    clear_screen()
    print(logo)
    print("Welcome to Blackjack! Try to beat the dealer without going over 21.\n")

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    computer = []

    for _ in range(2):
        player.append(random.choice(deck))
        computer.append(random.choice(deck))

    player_hand_value = sum(player)
    comp_hand_value = sum(computer)

    print(f"Your cards: {player} (Total = {player_hand_value})")
    print(f"Dealer's visible card: [{computer[0]}]")

    play = input("\nDo you want to 'hit' or 'stand'? ").lower()

    if play == 'stand':
        clear_screen()
        print(logo)
        print(f"Your cards: {player} (Total = {player_hand_value})")
        print(f"Dealer's cards: {computer} (Total = {comp_hand_value})")

        if player_hand_value > comp_hand_value:
            print("🎉 You win!")
        elif player_hand_value < comp_hand_value:
            print("😞 Dealer wins.")
        else:
            print("🤝 It's a draw.")

    elif play == 'hit':
        player.append(random.choice(deck))
        player_hand_value = sum(player)
        clear_screen()
        print(logo)
        print(f"You drew a card. Your cards: {player} (Total = {player_hand_value})")

        if comp_hand_value < 17:
            computer.append(random.choice(deck))
            comp_hand_value = sum(computer)
            print("Dealer hits.")
        else:
            print("Dealer stands.")

        print(f"Dealer's cards: {computer} (Total = {comp_hand_value})")

        if player_hand_value > 21:
            print("💥 You busted! Dealer wins.")
        elif comp_hand_value > 21:
            print("🎉 Dealer busted! You win.")
        else:
            if player_hand_value > comp_hand_value:
                print("🎉 You win!")
            elif player_hand_value < comp_hand_value:
                print("😞 Dealer wins.")
            else:
                print("🤝 It's a draw.")
    else:
        print("❌ Invalid input. Please choose 'hit' or 'stand'.")

while True:
    print("\n=============================")
    run = input("Type 'play' to start a game or 'exit' to quit: ").lower()
    print("=============================\n")
    if run == 'play':
        blackjack()
    elif run == 'exit':
        clear_screen()
        print("Thanks for playing! Goodbye 👋")
        break
    else:
        print("❌ Invalid input. Please type 'play' or 'exit'.")

























