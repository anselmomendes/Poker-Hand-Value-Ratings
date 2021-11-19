'''
Anselmo Mendes Oliveira
Engenheiro da Computação
Universidade Federal do Sul e Sudeste do Pará - UNIFESSPA
https://www.linkedin.com/in/anselmomendes/

Desafio de programação Python
I2A2 - Institut d'Intelligence Artificielle Appliquée.
'''

#Shows which combinations were satisfied and the score of the highest card.
from core.poker_hand import PokerHand

print('Royal Straight Flush')
PokerHand("AH TH KH QH JH").show_score()

print('Straight Flush')
PokerHand("9C 7C 8C JC TC").show_score()

print('Four of a kind')
PokerHand("2S 2D 2C 5C 2H").show_score() 

print('Full House')
PokerHand("7S 8D 2S 9S 4D").show_score() 

print('Flush')
PokerHand("7S 5S 3S 4S 2S").show_score()

print('Straight')
PokerHand("4D 5C 6S 7S 8D").show_score() 

print('Three of a kind')
PokerHand("5S 5D 8C 7S 5H").show_score() 

print('Two Pairs')
PokerHand("7D 7S 5H 5D JS").show_score()  

print('One Pair')
PokerHand("AS AD KD 7C 3D").show_score()  

print('High Card')
PokerHand("AD 2H KD 7C 4S").show_score()

