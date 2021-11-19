import sys
sys.path.insert(0,'../challenge/')
from interface.hand import Hand

from core.card_poker import CardPoker
from settings.common import Common
from settings.result import Result
import pandas as pd


#This class has methods of all moves of the boolean type and a function to check which card is stronger.
#The CompareWith method checks which hand has the strongest combinations and checks the tiebreaker.

class PokerHand(Hand):
    
    def __init__(self, data:str):
        cards_split = data.split(" ")
        if len(cards_split) == 5:
            self.card_01 = CardPoker(cards_split[0])
            self.card_02 = CardPoker(cards_split[1])
            self.card_03 = CardPoker(cards_split[2])
            self.card_04 = CardPoker(cards_split[3])
            self.card_05 = CardPoker(cards_split[4])
            
            self.card_value = []
            self.card_value.append(self.card_01.value)
            self.card_value.append(self.card_02.value)
            self.card_value.append(self.card_03.value)
            self.card_value.append(self.card_04.value)
            self.card_value.append(self.card_05.value)
            self.df = pd.DataFrame(self.card_value, columns=['card'])
            
            self.card_suit = []
            self.card_suit.append(self.card_01.suit)
            self.card_suit.append(self.card_02.suit)
            self.card_suit.append(self.card_03.suit)
            self.card_suit.append(self.card_04.suit)
            self.card_suit.append(self.card_05.suit)
            self.df2 = pd.DataFrame(self.card_suit, columns=['card'])
            
        else:
            raise NameError('number of invalid cards')

   
    def compare_with(self, other_player):

        if self.royal_flush() == True and other_player.royal_flush() == False:
            return Result.WIN
        elif self.royal_flush() == False and other_player.royal_flush() == True:
            return Result.LOSS
        elif self.royal_flush() == True and other_player.royal_flush() == True:
            for i in range(5):
                if self.high_card_full(i) > other_player.high_card_full(i):
                    return Result.WIN
                else:
                    return Result.LOSS
            
        if self.straight_flush() == True and other_player.straight_flush() == False:
            return Result.WIN
        elif self.straight_flush() == False and other_player.straight_flush() == True:
            return Result.LOSS
        elif self.straight_flush() == True and other_player.straight_flush() == True:
            for i in range(5):
                if self.high_card_full(i) > self.high_card_full(i):
                    return Result.WIN
                else:
                    return Result.LOSS

        if self.four_of_a_kind() == True and other_player.four_of_a_kind() == False:
            return Result.WIN
        elif self.four_of_a_kind() == False and other_player.four_of_a_kind() == True:
            return Result.LOSS
        elif self.four_of_a_kind() == True and other_player.four_of_a_kind() == True:
            for i in range(5):
                if self.high_card_full(i) > self.high_card_full(i):
                    return Result.WIN
                else:
                    return Result.LOSS
            
        if self.full_house() == True and other_player.full_house() == False:
            return Result.WIN
        elif self.full_house() == False and other_player.full_house() == True:
            return Result.LOSS
        elif self.full_house() == True and other_player.full_house() == True:
            aux1 = self.high_card_full()['aux'].values.astype(int)
            aux2 = other_player.high_card_full()['aux'].values.astype(int)
            for i in range(5):
                if aux1[i] > aux2[i]:
                    return Result.WIN
                else:
                    return Result.LOSS
            
        if self.flush() == True and other_player.flush() == False:
            return Result.WIN
        elif self.flush() == False and other_player.flush() == True:
            return Result.LOSS
        elif self.flush() == True and other_player.flush() == True:
            for i in range(5):
                if self.high_card_full(i) > self.high_card_full(i):
                    return Result.WIN
                else:
                    return Result.LOSS
        
        if self.straight() == True and other_player.straight() == False:
            return Result.WIN
        elif self.straight() == False and other_player.straight() == True:
            return Result.LOSS
        elif self.straight() == True and other_player.straight() == True:
            for i in range(5):
                if self.high_card_full(i) > self.high_card_full(i):
                    return Result.WIN
                else:
                    return Result.LOSS
            
        if self.three_of_a_kind() == True and other_player.three_of_a_kind() == False:
            return Result.WIN
        elif self.three_of_a_kind() == False and other_player.three_of_a_kind() == True:
            return Result.LOSS
        elif self.three_of_a_kind() == True and other_player.three_of_a_kind() == True:
            for i in range(5):
                if self.high_card_full(i) > other_player.high_card_full(i):
                    return Result.WIN
                else:
                    return Result.LOSS
            
        if self.tho_pair() == True and other_player.tho_pair() == False:
            return Result.WIN
        elif self.tho_pair() == False and other_player.tho_pair() == True:
            return Result.LOSS
        elif self.tho_pair() == True and other_player.tho_pair() == True:
            aux1 = self.high_card_full()
            aux2 = other_player.high_card_full()
            pair1 = aux1[self.high_card_full().duplicated(['aux'], keep=False)]
            pair2 = aux2[other_player.high_card_full().duplicated(['aux'], keep=False)]
            pair1 = pair1.astype(int).set_index('aux').sort_index(axis=0, ascending = False)
            pair2 = pair2.astype(int).set_index('aux').sort_index(axis=0, ascending = False)
            for i in range(4):
                if pair1.index[i] > pair2.index[i] or pair1.index[i] < pair2.index[i]:
                    if pair1.index[i] > pair2.index[i]:
                        return Result.WIN
                    else:
                        return Result.LOSS
            if aux1.astype(int).sum() > aux2.astype(int).sum():
                return Result.WIN
            elif aux1.astype(int).sum() < aux2.astype(int).sum():
                return Result.LOSS
            else:
                raise NameError('Tied deck')
                
        if self.one_pair() == True and other_player.one_pair() == False:
            return Result.WIN
        elif self.one_pair() == False and other_player.one_pair() == True:
            return Result.LOSS
        elif self.one_pair() == True and other_player.one_pair() == True:
            aux1 = self.high_card_full()
            aux2 = other_player.high_card_full()
            pair1 = aux1[self.high_card_full().duplicated(['aux'], keep=False)]
            pair2 = aux2[other_player.high_card_full().duplicated(['aux'], keep=False)]
            for i in range(2):
                if pair1['aux'][i] > pair2['aux'][i] or pair1['aux'][i] < pair2['aux'][i]:
                    if pair1.index[i] > pair2.index[i]:
                        return Result.WIN
                    else:
                        return Result.LOSS
            aux1 = aux1[aux1 != pair1['aux'][0]].dropna().values
            aux2 = aux2[aux2 != pair2['aux'][0]].dropna().values
            for i in range(3):
                if aux1[i] > aux2[i]:
                    return Result.WIN
                elif aux1[i] < aux2[i]:
                    return Result.LOSS
                    
        raise NameError('Erro Deck')
           
        
        
    def show_score(self):
        
        '''
        print('POKER AHND VALUE RATINGS')
        print('royal_flush: {0}'.format(self.royal_flush()))
        print('straight_flush: {0}'.format(self.straight_flush()))
        print('four_of_a_kind: {0}'.format(self.four_of_a_kind()))
        print('full_house: {0}'.format(self.full_house()))
        print('flush: {0}'.format(self.flush()))
        print('straight: {0}'.format(self.straight()))
        print('three_of_a_kind: {0}'.format(self.three_of_a_kind()))
        print('tho_pair: {0}'.format(self.tho_pair()))
        print('one_pair: {0}'.format(self.one_pair()))
        print('high_card: {0}\n'.format(self.high_card()))
        '''
        
        print(self.royal_flush(), self.straight_flush(), self.four_of_a_kind(), self.full_house(), self.flush(), self.straight(), self.three_of_a_kind(), self.tho_pair(), self.one_pair(), self.high_card())
        print('')
        
    
    
    def royal_flush(self) -> bool:
        
        if self.card_01.value in Common.ROYAL_FLUSH_CARD:
            if self.card_02.value in Common.ROYAL_FLUSH_CARD:
                if self.card_03.value in Common.ROYAL_FLUSH_CARD:
                    if self.card_04.value in Common.ROYAL_FLUSH_CARD:
                        if self.card_05.value in Common.ROYAL_FLUSH_CARD:
                            if self.df2.value_counts()[0] == 5:
                                return True
        return False


    
    def straight_flush(self) -> bool:
        
        for x in Common.VALUE_CARD:
            if x in self.card_value:
                keys = list(Common.VALUE_CARD.keys())
                n = keys.index(x)
                if n < 9:
                    if Common.VALUE_CARD_INV[str(n+2)] in self.card_value:
                        if Common.VALUE_CARD_INV[str(n+3)] in self.card_value:
                            if Common.VALUE_CARD_INV[str(n+4)] in self.card_value:
                                if Common.VALUE_CARD_INV[str(n+5)] in self.card_value:
                                    if Common.VALUE_CARD_INV[str(n+6)] in self.card_value:
                                        if self.df2.value_counts()[0] == 5:
                                            return True
        return False
    
    
    
    def four_of_a_kind(self) -> bool:
        
        if self.df.value_counts()[0] >= 4:
            return True
        else:
            return False
    
    def full_house(self) -> bool:
        if self.df.value_counts()[0] == 3 or self.df.value_counts()[1] == 3:
            if self.df.value_counts()[0] == 2 or self.df.value_counts()[1] == 2:
                return True
        return False
    
    
     
    def flush(self) -> bool:
        if self.df2.value_counts()[0] == 5:
            return True
        return False 
    
    
    
    def straight(self):
        for x in Common.VALUE_CARD:
            keys = list(Common.VALUE_CARD.keys())
            n = keys.index(x)
            if n < 9:
                if Common.VALUE_CARD_INV[str(n+2)] in self.card_value:
                    if Common.VALUE_CARD_INV[str(n+3)] in self.card_value:
                        if Common.VALUE_CARD_INV[str(n+4)] in self.card_value:
                            if Common.VALUE_CARD_INV[str(n+5)] in self.card_value:
                                if Common.VALUE_CARD_INV[str(n+6)] in self.card_value:
                                    return True
        return False
    
    
    
    def three_of_a_kind(self) -> bool:
        if self.df.value_counts()[0] >= 3:
            return True
        return False
    
    def tho_pair(self) -> bool:
        if len(self.df.value_counts()) > 1:
            if self.df.value_counts()[0] >= 2:
                if self.df.value_counts()[1] >= 2:
                    return True
        return False 
    
    
    
    def one_pair(self) -> bool:
        if self.df.value_counts()[0] >= 2:
            return True
        return False
    
    
    
    def high_card(self) -> float:
        aux = []
        aux.append(Common.VALUE_CARD[self.df.values[0][0]])
        aux.append(Common.VALUE_CARD[self.df.values[1][0]])
        aux.append(Common.VALUE_CARD[self.df.values[2][0]])
        aux.append(Common.VALUE_CARD[self.df.values[3][0]])
        aux.append(Common.VALUE_CARD[self.df.values[4][0]])
        aux1 = pd.DataFrame(aux, columns=['aux'], dtype= float)
        return aux1['aux'].max()



    def high_card_full(self):
        aux = []
        aux.append(Common.VALUE_CARD[self.df.values[0][0]])
        aux.append(Common.VALUE_CARD[self.df.values[1][0]])
        aux.append(Common.VALUE_CARD[self.df.values[2][0]])
        aux.append(Common.VALUE_CARD[self.df.values[3][0]])
        aux.append(Common.VALUE_CARD[self.df.values[4][0]])
        aux = pd.DataFrame(aux, columns=['aux'], dtype= float)
        return aux