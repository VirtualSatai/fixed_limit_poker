from json import JSONEncoder
from typing import Dict, List, Sequence

from pyfancy.pyfancy import pyfancy

from environment.Constants import Stage
from environment.PlayerObservation import PlayerObservation
from utils.handValue import getHandPercent


class OmnipotentObservation:
    boardCards: List[str]
    stage: Stage
    totalPot: int
    stagePot: int
    players: List[PlayerObservation]
    hands: Dict[str, Sequence[str]]

    def __init__(self) -> None:
        self.boardCards = []
        self.players = []
        self.stage = Stage.PREFLOP
        self.totalPot = 0
        self.stagePot = 0
        self.hands = dict()

    def __str__(self):
        header = pyfancy().red(f"{str(self.stage):<31}").get()
        pots_str = f"TotalPot: {self.totalPot:>3} StagePot: {self.stagePot:>3}"
        pots = pyfancy().green(pots_str).get()

        player_hands_list = []
        for ph in self.hands.items():
            percent, _ = getHandPercent(ph[1], self.boardCards)
            percent_str = str(round(percent, 2))
            cards = ' '.join(ph[1])
            player_name = f"'{ph[0]}':"
            player_hands_list.append(f"{player_name} {cards} ({percent_str})")

        player_hands = pyfancy().yellow(" ".join(player_hands_list)).get()
        current_board = " ".join(self.boardCards)
        community = pyfancy().blue(f'Community: {current_board}').get()
        return f"{header} | {pots} | {player_hands} | {community}"


class OmnipotentObservationEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
