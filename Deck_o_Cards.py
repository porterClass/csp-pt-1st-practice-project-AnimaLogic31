#This makes the code random
import random
def roll_random(low, high):
    return random.randint(low, high)

# This is the suit of the card
def card_suit(): 
    num = roll_random(1,100)
    if 1 <= num <= 25 :
     return "Hearts"
    elif 26 <= num <= 50 :
     return "Clubs"
    elif 51 <= num <= 75 :
     return "Diamonds"
    elif 76 <= num <= 100 :
     return "Spades"

#This is the card's number   
def card_face() :
  face = roll_random(1,10)
  if face == 1 :
    return "Ace"
  elif face == 2 :
    return "Two"
  elif face == 3 :
    return "Three"
  elif face == 4 :
    return "Four"
  elif face == 5 :
    return "Five"
  elif face == 6 :
    return "Six"
  elif face == 7 :
    return "Seven"
  elif face == 8 :
    return "Eight"
  elif face == 9 :
    return "Nine"
  elif face == 10 :
    return royal()

#This determines what face card it is
def royal(): 
  royal_suit = roll_random(1,4)
  if royal_suit == 1 :
    return "Ten"
  elif royal_suit == 2 :
    return "Jack"
  elif royal_suit == 3 :
    return "Queen"
  elif royal_suit == 4 :
    return "King"

#Out of a total pack of 54 cards there may be a chance of you getting a Joker (2 out of 54)
def draw_Joker(): 
  card = roll_random(1,54)
  if 1 <= card <= 2 :
    return "Joker"

#Now we draw a card (52 normal cards and one Joker)
def draw_card():
  if draw_Joker() == "Joker" :
    print("You have drawn a Joker")
  elif card_suit() == "Spades" and card_face() == "Ace" :
    print("Congrats! You have drawn the trump card, the Ace of Spades!")
  else:
    print("You have drawn the", card_face(), "of", card_suit())

# This defines what our cards we can draw in our Poker hand (because we can't draw Jokers)
def poker_card():
    print("The", card_face(), "of", card_suit())

# This defines what our Poker Hand looks like
def poker_hand(): 
  print("Your Poker Hand is:")
  poker_card()
  poker_card()
  poker_card()
  poker_card()
  poker_card()

#Here we can draw ONE card
draw_card()

#Split it up and make the output neat
print("\n")

# Now we can draw our Poker hand
poker_hand()