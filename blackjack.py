import random
player_In = True
dealer_In = True
#deck of cards / player dealer hand
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
"J", "Q", "K", "A","J", "Q", "K", "A","J", "Q", "K", "A","J", "Q", "K", "A"]
player_Hand = []
dealer_Hand = []

# deal the cards
def deal_Cards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calculate the total of each hand
def total(turn):
    total = 0
    face = ["J", "Q", "K"]
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
            
#game loop
for _ in range(2):
    deal_Cards(dealer_Hand)
    deal_Cards(player_Hand)

while player_In or dealer_In:
    print(f"You have {player_Hand} for a total of {total(player_Hand)}")
    if player_In:
        stay_Hit = input("1: Hit or 2: Stay ")
    if total(dealer_Hand) > 16:
        dealer_In = False
    else:
        deal_Cards(dealer_Hand)
    if stay_Hit == "1":
        deal_Cards(player_Hand)
    elif stay_Hit == "2":
        player_In = False
    else:
        print("Invaild Input")
    if total(player_Hand) >= 21:
        break
    elif total (dealer_Hand) >= 21:
        break

# winner
if total(player_Hand) == 21:
    print(f"You have {player_Hand} for a total of {total(player_Hand)} and the dealer has {dealer_Hand} for a total of {total(dealer_Hand)}")
    print("Blackjack! You Win!")
elif total(dealer_Hand) == 21:
   print(f"You have {player_Hand} for a total of {total(player_Hand)} and the dealer has {dealer_Hand} for a total of {total(dealer_Hand)}")
   print("BlackJack! Dealer Win!") 
elif total(player_Hand) > 21:
    print(f"You have {player_Hand} for a total of {total(player_Hand)} and the dealer has {dealer_Hand} for a total of {total(dealer_Hand)}")
    print("You Bust! Dealer Wins!")
elif total(dealer_Hand) > 21:
    print(f"You have {player_Hand} for a total of {total(player_Hand)} and the dealer has {dealer_Hand} for a total of {total(dealer_Hand)}")
    print("Dealer Bust! You Win!")
elif 21 - total(dealer_Hand) < 21 - total(player_Hand):
     print(f"You have {player_Hand} for a total of {total(player_Hand)} and the dealer has {dealer_Hand} for a total of {total(dealer_Hand)}")
     print("Dealer Wins!")
elif 21 - total(dealer_Hand) > 21 - total(player_Hand):
     print(f"You have {player_Hand} for a total of {total(player_Hand)} and the dealer has {dealer_Hand} for a total of {total(dealer_Hand)}")
     print("You Wins!")

