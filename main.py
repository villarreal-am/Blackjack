import math
import random
import time

dealer_score = 0
player_score = 0
dealer_cards = []
player_cards = []
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
picture_cards = [10, "Jack", "Queen", "King"]

# Draws a card
def draw_card():
    suit = random.choice(suits)
    number = random.randint(1, 11)
    
    # Changes Ace value to 1 if 11 will lead to a bust
    if number == 11 or number == 1:
        number = "Ace"
        
    # If the number is 10, chooses a picture card for it
    if number == 10:
        number = random.choice(picture_cards)

    card = (suit, number)
    
    # Redraws card if either player has already been dealt it
    if card in dealer_cards or card in player_cards:
        card = draw_card()
    else:
        return card

# Calculates a player's score, given their cards
def calculate_score(cards):
    score = 0
    ace_count = 0
    
    # Adds score of each card to total score
    for card in cards:
        if card[1] in picture_cards:
            score += 10
        elif card[1] == "Ace":
            ace_count += 1
        else:
            score += card[1]
            
    # Counts Ace cards seperately based off current score        
    for i in range(ace_count):
        if score < 11:
            score += 11
        else:
            score += 1
    return score

game_start = input("Welcome to Blackjack. Type 'START' to play\n")

if game_start != "START":
    print("Not a valid command.")
    quit()

player_turn = True
    
# Draws Inital cards
dealer_cards.append(draw_card())
for i in range(2):
    player_cards.append(draw_card())
dealer_score = calculate_score(dealer_cards)
player_score = calculate_score(player_cards)

# Prints inital cards
print("The dealer begins with a(n) " + str(dealer_cards[0][1]) + " of " + dealer_cards[0][0])
print("You begin with a(n) " + str(player_cards[0][1]) + " of " + player_cards[0][0]
+ " and a(n) " + str(player_cards[1][1]) + " of " + player_cards[1][0])
    
# Player's turn
while player_turn:
    p_input = input("Would you like to HIT or STAND?\n")
    
    if p_input == "HIT":
        p_new_card = draw_card()
        player_cards.append(p_new_card)
        player_score = calculate_score(player_cards)
        print("You draw a(n) " + str(p_new_card[1]) + " of " + p_new_card[0])

        # Player Bust
        if player_score > 21:
            print("Bust! You lose :(")
            quit()

        time.sleep(0.3)
        print("Your current score is " + str(player_score))
        time.sleep(0.5)

    elif p_input == "STAND":
        print("You stand with a score of " + str(player_score))
        player_turn = False
    else:
        print("Please provide valid command.")
            

# Dealer's turn
while dealer_score < 17:
    new_card = draw_card()
    dealer_cards.append(new_card)
    print("The dealer draws a(n) " + str(new_card[1]) + " of " + new_card[0])
    dealer_score = calculate_score(dealer_cards)
    time.sleep(1)
        
    # Dealer Bust
    if dealer_score > 21:
        print("Dealer Busts! You win :)")
        quit()
        
print("The dealer stands with a score of " + str(dealer_score))
    
# Determine results
if player_score > dealer_score:
    print("You win! Good job!")
elif player_score < dealer_score:
    print("You lose :( Try again next time")
else:
    print("Tie. Good game.")

time.sleep(1)
quit()
