import argparse
import os

import jsonpickle


# from card import Card
import masstransit

def main() -> None:
    parser = argparse.ArgumentParser(prog='masstransit', description='Run a game of masstransit')
    parser.add_argument('-d', '--deck', type=str, default='decks/standard_deck', help='The deck folder to use')
    parser.add_argument('-n', '--num-players', type=int, default=1, help='The number of players to play with')

    args = parser.parse_args()

    card_list = load_cards(args.deck)
    print(card_list[0].__class__)
    print(card_list[0])

    # print(card_list)



def load_cards(folder: str) -> list[masstransit.card.Card]:
    deck_files = os.listdir(folder)
    card_list = []
    for deck_file in deck_files:
        with open(os.path.join(folder, deck_file), 'r') as f:
            for line in f.readlines():
                card_list.append(jsonpickle.decode(line[:-1], classes=masstransit.card.Card))
    return card_list

if __name__ == '__main__':
    main()