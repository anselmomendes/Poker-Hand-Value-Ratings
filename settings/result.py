from enum import Enum, unique

#Support class to display the result of verification output
@unique
class Result(Enum):
    WIN = 1
    LOSS = 0
    