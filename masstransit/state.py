from card import Card
from board import Board

class State:
    def __init__(self, board: Board, turn: int, hands: list[list[Card]], draw_pile: list[Card]) -> None:
        self.board = board
        self.turn = turn
        self.hands = hands
        self.draw_pile = draw_pile

    def detect_win(self) -> bool:
        return self.board.detect_win()
