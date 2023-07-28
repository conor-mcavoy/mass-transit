from card import Card, CardType

class Commuter:
    def __init__(self, position: int = -1, last_travel_type: CardType = None) -> None:
        self.position = position  # position of -1 is the big city
        self.last_travel_type = last_travel_type


class Board:
    # todo default arguments
    def __init__(self, lines: list[list[Card]], commuters: list[Commuter]) -> None:
        self.lines = lines
        self.commuters = commuters


    def detect_win(self) -> bool:
        '''A board is in a won position if all commuters are in a suburb'''

        return all(line[commuter.position].suburb for commuter, line in zip(self.commuters, self.lines))
    

    def valid_discard(self, card: Card, line_number: int) -> tuple[bool, int]:
        '''Returns a tuple of whether the card can be discarded and how far a commuter would move if it can be'''

        if card.suburb or card.cardtype == CardType.YELLOW:
            # suburb and yellow cards cannot be discarded
            return False, 0

        # the conditions for a discard are:
        # 1. you can discard a green to walk to the next card
        # 2. you can discard a gray, blue, or red to move from a station/traffic stop to station/traffic stop both of the corresponding color
        # 3. you must leave a traffic stop using the same travel method you entered it with
        # 4. the big city (the starting position) has to be walked out of
        # 5. you have to walk out of a dead end
        # note, a commuter does not have to walk between stations on the same card, a commuter may leave from any station on a card

        discard_type = card.cardtype

        # if you are in the big city, you must walk out
        if commuter.position == -1:
            return discard_type == CardType.GREEN, 1

        line = self.lines[line_number]
        commuter = self.commuters[line_number]
        commuter_card = line[commuter.position]

        # if you are in a suburb, you cannot proceed
        if commuter_card.suburb:
            return False, 0

        if discard_type == CardType.GREEN:
            # the only time you cannot walk is if you are in traffic and you did not walk into the traffic
            in_traffic = commuter_card.traffic_stop
            walked_in = commuter.last_travel_type == CardType.GREEN
            return not (in_traffic and not walked_in), 1
        
        # at this point the card must be gray, blue, or red

        # the current commuter card must have a station or traffic stop of the discarded color, and not a dead end
        route = commuter_card.routes[discard_type]
        if not (route.station or route.traffic_stop) or route.deadend:
            return False, 0
        
        # if it is a traffic stop, the commuter must have entered it by the same manner they are trying to leave
        if route.traffic_stop and discard_type != commuter.last_travel_type:
            return False, 0
        
        # furthermore, there must be another card down the line with a station or traffic stop of the discarded color
        current_position = commuter.position
        max_position = len(line) - 1
        while current_position < max_position:
            current_position += 1
            current_card = line[current_position]
            current_route = current_card.routes[discard_type]
            if current_route.station or current_route.traffic_stop:
                return True, current_position - commuter.position
        
        # no next card was found with a station or traffic stop of the discarded color
        return False, 0
    

    def do_discard(self, card: Card, line_number: int, distance: int) -> None:
        commuter = self.commuters[line_number]
        commuter.position += distance
        commuter.last_travel_type = card.cardtype


    def valid_play(self, card: Card, line_number: int) -> bool:
        # conditions for a valid play are simply that the line does not end in a suburb already
        # and if you are playing a suburb, the suburb distance must be met for this line

        line = self.lines[line_number]
        last_card = line[-1]
        if last_card.suburb:
            return False
        
        if not card.suburb:
            return True
        
        return len(line) >= card.suburb_distance
    
    
    def do_play(self, card: Card, line_number: int) -> None:
        self.lines[line_number].append(card)
