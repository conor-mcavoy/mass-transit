import jsonpickle
import masstransit.card
import masstransit.route

with open('card_file.json', 'a') as f:
    gray_route = masstransit.route.Route(traffic_stop=True)
    blue_route = masstransit.route.Route(traffic_stop=True)
    red_route = masstransit.route.Route(traffic_stop=True)
    
    card = masstransit.card.Card(masstransit.card.CardType.YELLOW, 
                                {
                                    masstransit.card.CardType.GRAY: gray_route,
                                    masstransit.card.CardType.BLUE: blue_route,
                                    masstransit.card.CardType.RED: red_route,
                                }, urgent=True)
    
    count = 1
    for _ in range(count):
        pass
        # f.write(jsonpickle.encode(card) + '\n')