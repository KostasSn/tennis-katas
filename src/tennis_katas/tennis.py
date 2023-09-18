from enum import Enum
from dataclasses import dataclass


class FindResult:
    """_summary_"""

    def live_result(self, player1_points: int, player2_points: int) -> str:
        if player1_points == player2_points:
            return self.draw_result()


class ScoreSystem(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE = 4
    ADVANTAGE = 5


@dataclass
class Player:
    name: str
    points: int

    def score_point(self):
        self.points += 1
