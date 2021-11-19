#Support variables for suit checking and card scoring

class Common():

    ROYAL_FLUSH_CARD:str =  {"T": "10",
                             "J": "11",
                             "Q": "12",
                             "K": "13",
                             "A": "14"}

    VALUE_CARD:str =    {"2": "2",
                         "3": "3",
                         "4": "4",
                         "5": "5",
                         "6": "6",
                         "7": "7",
                         "8": "8",
                         "9": "9",
                         "T": "10",
                         "J": "11",
                         "Q": "12",
                         "K": "13",
                         "A": "14"}

    VALUE_CARD_INV:str =    {"2": "2",
                             "3": "3",
                             "4": "4",
                             "5": "5",
                             "6": "6",
                             "7": "7",
                             "8": "8",
                             "9": "9",
                             "10": "T",
                             "11": "J",
                             "12": "Q",
                             "13": "K",
                             "14": "A"}

    SUIT_CARD:str =    {"S": "0",
                        "H": "1",
                        "D": "2",
                        "C": "3"}