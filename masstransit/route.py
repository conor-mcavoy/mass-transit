from enum import Enum

class Route:
    def __init__(self, station: bool = False, traffic_stop: bool = False, deadend: bool = False) -> None:
        # if routetype == CardType.GREEN or routetype == CardType.YELLOW:
            # raise ValueError('A route cannot be green or yellow')
        
        # self.routetype = routetype
        self.station = station
        self.traffic_stop = traffic_stop
        self.deadend = deadend  # by convention, a suburb is considered a deadend
    
    def __str__(self, width: int = 5) -> str:
        if self.station:
            symbol = 'O'
        elif self.traffic_stop:
            symbol = 'T'
        else:
            symbol = '-'

        beginning = "-"*(width//2)
        end = "-"*(width//2) if not self.deadend else " "*(width//2)

        return beginning + symbol + end
