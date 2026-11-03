"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    if ('K' in card or 'Q' in card or 'J' in card):
        actual_result = int(10)
    elif ('A' in card):
        actual_result = int(1)
    else:
        actual_result = int(card)
    return actual_result
        
    pass


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    card_face_one = card_one
    card_face_two = card_two 
    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)
    
    if (card_one > card_two): 
        return card_face_one 
    elif (card_one == card_two): 
        return card_face_one,card_face_two
    else: 
        return card_face_two 

    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    if card_one == 'A':
        card_one = 11
    else:
        card_one = value_of_card(card_one)

    if card_two == 'A':
        card_two = 11
    else:
        card_two = value_of_card(card_two)

    if (card_one + card_two <= 10):
        value_ace = 11
    else:
        value_ace = 1
    return value_ace


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    ##card_one = value_of_card(card_one)
    ##card_two = value_of_card(card_two)

    black_jack_draw = ['10', 'K', 'Q', 'J']

    if (((card_one in black_jack_draw) and card_two == 'A')  or ((card_two in black_jack_draw) and card_one == 'A')):
        black_jack = True
    else:
        black_jack = False
    return black_jack


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two) 

    if (card_one_value == card_two_value):
        split = True 
    else: 
        split = False
    return split 
    
    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    co = value_of_card(card_one)
    ct = value_of_card(card_two) 

    if ((8 < co+ct < 12 )): 
        double = True
    else: 
        double = False
    return double 


    pass
