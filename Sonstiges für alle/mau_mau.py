"""Docstring: implementation of a simple mau-mau-game"""

import random

def create_deck():
    """Docstring: Creates a 32-card deck

    The deck will be automatically shuffeled. It is saved as a list of tuples
    Each tuple has the form (symbol, value)"""
    
    symbols = ["Herz", "Karo", "Kreuz", "Pik"]
    numbers = ["7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

    deck = []
    #All combinations of cards
    for s in symbols:
        for n in numbers:
            deck.append((s,n))
    random.shuffle(deck)
    return deck



def get_number_of_players():
    """Docstring: Gets the user's choice for number of players

    Repeats asking the user until he types a valid input"""

    
    number_of_players = 0
    while number_of_players == 0:
        user_input = input("Wie viele Spieler sollen mitspielen (2-4)? >>> ")
        if not user_input.isdigit():
            print("Bitte eine Zahl eingeben")
            continue
        number = int(user_input)
        if number < 2 or number > 4:
            print("Bitte Zahl zwischen 2 und 4 eingeben.")
            continue
        number_of_players = number
    return number_of_players


def get_players_names(number_of_palyers):
    """Docstring: Asks Users for their names

    Repeats asking for every players. Fills in default names if input is empty"""
    current = 1
    names = []
    while current <= number_of_palyers:
        user_input = input("Spieler " + str(current) + ", wie heißt du? >>> ")
        if user_input == "":
            #e.g. Splieler 1, Spieler 2, ...
            names.append("Spieler "+str(current))
        else:
            names.append(user_input)
        current += 1
    return names


def draw_card(deck):
    """Docstring: Removes the first card of the given deck and returns it"""
    return deck.pop()


def get_start_card_amount():
    """Docstring: Asks the user for the number of cards to start with"""
    
    number_of_cards = 0
    while number_of_cards == 0:
        user_input = input("Wie viele Karten sollen jeder kriegen (2-5)? >>> ")
        if not user_input.isdigit():
            print("Bitte eine Zahl eingeben")
            continue
        number = int(user_input)
        if number < 2 or number > 5:
            print("Bitte Zahl zwischen 2 und 4 eingeben.")
            continue
        number_of_cards = number
    return number_of_cards


def fill_hands(number_of_players, number_of_cards, deck):
    """Docstring: Initializes the hand-cards of all players

    Draws number_of_cards cards from deck and adds them to the cards of each player
    Returns a list of lists"""
    hands = []
    for player in range(number_of_players):
        hand = []
        for card in range(number_of_cards):
            hand.append(draw_card(deck))
        hands.append(hand)
    return hands


def print_cards(index, hand, name, deck, topdeck):
    """Docstring: Handles one turn"""
    
    print("\n"*20) #lol
    print(" "*10, "Deck:", len(deck), "Karten")
    print(" "*15, topdeck[0][0], topdeck[0][1])
    print("\n"*5)
    print(name+", du bist dran!\n")
    print("Deine Karten:")
    for card in hand:
        print(" -", card[0], card[1])
    print("")

    possible = possible_cards(hand, topdeck)
    if len(possible) == 0:
        new = draw_card(deck)
        print("Du kannst keine Karte legen. Du ziehst", new[0], new[1])
        if can_lay(new, topdeck[0]):
            while True:
                answer = input("Diese kannst du legen. willst du das tun (ja, nein)? >>> ")
                if answer == "ja":
                    return new
                elif answer == "nein":
                    hand.append(new)
                    return None
                else:
                    print("Ja oder nein eingeben!")
        else:
            print("Diese kannst du auch nicht legen.")
            input()
    else:
        print("Folgende Karte(n) kannst du legen:")
        for i in range(len(possible)):
            card = possible[i]
            print("", str(i)+". ", card[0], card[1])
        while True:
            answer = input("Wähle eine der angegebenen Nummern ("+\
                           str(0)+"-"+str(len(possible)-1)+")")
            if not answer.isdigit():
                print("Bitte eine Zahl angeben")
                continue
            number = int(answer)
            if number < 0 or number >= len(possible):
                print("Falsche Zahl")
                continue
            card = possible[number]
            hand.remove(card)
            return card


def can_lay(card1, card2):
    """Docstring: Checks if card1 can be layed on card2

    Returns true if symbols or values are equal"""
    return card1[0] == card2[0] or card1[1] == card2[1]

def possible_cards(hand, topdeck):
    """Docstring: Finds possible cards in hand to lay on the topdeck"""
    possible = []
    for card in hand:
        if can_lay(card, topdeck[0]):
            # possible if a card could be layed on topdeck
            possible.append(card)
    return possible

def has_won(hand):
    """Docstring: Checks if a player wins with the given hand cards"""
    return len(hand) == 0

def next_player(current, number):
    """Docstring: Returns the index of the next player"""
    return (current + 1) % number

def main():
    """Docstring: Main function. Starts the game"""
    deck = create_deck()
    topdeck = []
    #topdeck gets one opened card from deck
    topdeck.insert(0, draw_card(deck))

    number_of_players = get_number_of_players()
    names = get_players_names(number_of_players)
    number_of_cards = get_start_card_amount()
    hands = fill_hands(number_of_players, number_of_cards, deck)

    current_player = 0
    

    while True:
        # shuffle topdeck if the hidden deck is empty
        if len(deck) == 0:
            top = topdeck[0]
            random.shuffle(topdeck)
            deck = topdeck
            topdeck = [top]
        
        card = print_cards(current_player, hands[current_player], \
                    names[current_player], deck, topdeck)
        
        if card != None:
            topdeck.insert(0, card)
        if has_won(hands[current_player]):
            break
        current_player = next_player(current_player, number_of_players)

    # this is only be reached when a player has won
    print("\n"*5)
    print("Glückwunsch,", names[current_player]+".", "Du hast gewonnen! Mau Mau")
    print("Anzahl Karten der anderen Spieler:")
    while len(hands) > 0:
        minl = 32 #32 because you nobody can have more cards in his hand
        minindex = 0
        for i in range(len(hands)):
            if len(hands[i]) < minl:
                minl = len(hands[i])
                minindex = i
        print(names[i], "-", len(hands[i]))
        names.remove(names[i])
        hands.remove(hands[i])


        
if __name__ == "__main__":
    main()
