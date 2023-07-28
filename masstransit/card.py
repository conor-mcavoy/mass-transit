from route import Route
from enum import Enum

class CardType(Enum):
    GRAY = 0
    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4

class Card:
    def __init__(self, cardtype: CardType, routes: dict[CardType, Route], urgent: bool = False, suburb: bool = False, suburb_distance: int = 0) -> None:
        '''
        if cardtype not in [CardType.GREEN, CardType.YELLOW] and suburb:
            raise ValueError('Suburb cards are only gray, blue, or red')
     
        if len(routes) != 3 and not suburb:
            raise ValueError('A non-suburb card must have exactly 3 routes')
        elif len(routes) != 1 and suburb:
            raise ValueError('A suburb card must have exactly 1 route')

        if urgent and suburb:
            raise ValueError('A card cannot be both urgent and a suburb card')
        
        if suburb and suburb_distance not in [3, 4]:
            raise ValueError('A suburb card must have a distance of 3 or 4')
        '''
     
        self.cardtype = cardtype
        self.routes = routes
        self.urgent = urgent
        self.suburb = suburb
        self.suburb_distance = suburb_distance

    def __str__(self, width: int = 7) -> str:
        print_str = ('-' * width) + '\n'
        if self.cardtype == CardType.GRAY:
            left_letter = 'G'
        elif self.cardtype == CardType.BLUE:
            left_letter = 'B'
        elif self.cardtype == CardType.RED:
            left_letter = 'R'
        elif self.cardtype == CardType.GREEN:
            left_letter = 'W'
        else:
            left_letter = 'X'
        
        if self.suburb:
            right_letter = str(self.suburb_distance)
        elif self.urgent:
            right_letter = '!'
        else:
            right_letter = ' '

        print_str += f'|{left_letter}{" "*(width-4)}{right_letter}|\n'
        print_str += f'|{" "*(width-2)}|\n'

        if CardType.GRAY in self.routes:
            print_str += f'|{self.routes[CardType.GRAY].__str__(width-2)}|\n'
        else:
            print_str += f'|{" "*(width-2)}|\n'

        if CardType.BLUE in self.routes:
            print_str += f'|{self.routes[CardType.BLUE].__str__(width-2)}|\n'
        else:
            print_str += f'|{" "*(width-2)}|\n'
        
        if CardType.RED in self.routes:
            print_str += f'|{self.routes[CardType.RED].__str__(width-2)}|\n'
        else:
            print_str += f'|{" "*(width-2)}|\n'
        
        print_str += ('-' * width) + '\n'
        return print_str
    
