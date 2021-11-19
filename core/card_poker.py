from interface.card import Card
from settings.common import Common

#Creates the card type with the attributes value and nipe
class CardPoker(Card):
    
    def __init__(self, data):
        if data[0] in Common.VALUE_CARD:
            self.value:str = data[0]
        else:
            raise NameError('invalid card values')
        if data[1] in Common.SUIT_CARD:
            self.suit:str = data[1]
        else:
            raise NameError('invalid card suit')