from abc import ABC, abstractclassmethod

#Requires creation of letter type
class Card(ABC):
    @abstractclassmethod
    def __init__(self):
        pass
