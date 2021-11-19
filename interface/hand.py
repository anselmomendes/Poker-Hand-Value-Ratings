from abc import ABC, abstractclassmethod

#Establish the rules for poker hand combinations
class Hand(ABC):
    
    #This function is responsible for comparing the hands of decks and evaluating which one has the strongest formation and score.
    @abstractclassmethod
    def compare_with(self) -> bool:
        pass
    
    
    #This function is responsible for showing which combinations and highest card was formed.     
    @abstractclassmethod
    def show_score(self) -> str:
        pass
    
    #Check if the cards have the highest values ​​and are of the same suit
    @abstractclassmethod
    def royal_flush(self) -> bool:
        pass
    
    
    #Check if the cards are straight and of the same suit
    @abstractclassmethod
    def straight_flush(self) -> bool:
        pass
    
    #Check if there are four cards with the same value
    @abstractclassmethod
    def four_of_a_kind(self) -> bool:
        pass
    
    
    #Checks if there is a combination with 3 cards of the same value and 2 cards of the same value
    @abstractclassmethod
    def full_house(self) -> bool:
        pass
    
    #Check if there are 5 cards with the same suit
    @abstractclassmethod
    def flush(self) -> bool:
        pass
    
    #Check if all cards are in sequence
    @abstractclassmethod
    def straight(self) -> bool:
        pass
    
    #Check if there are 3 cards of the same suit
    @abstractclassmethod
    def three_of_a_kind(self) -> bool:
        pass
    
    #Check if there are 2 pairs of cards of the same suit
    @abstractclassmethod
    def tho_pair(self) -> bool:
        pass
    
    #Check if there are 1 pairs of cards of the same suit
    @abstractclassmethod
    def one_pair(self) -> bool:
        pass
    
    #Check the value of the highest card in the hand
    @abstractclassmethod
    def high_card(self) -> bool:
        pass
    
    #Check the value of the highest card in the hand (in decimal)
    @abstractclassmethod
    def high_card_full(self) -> int:
        pass
