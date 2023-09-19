from enum import Enum
from dataclasses import dataclass


class FindResult:
    """_summary_"""

    def get_result(self, player1_points: int, player2_points: int) -> str:
        if player1_points == player2_points:
            return self.draw_result()


class Draw:
    def draw_result(self):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.Player.points, "Deuce")


class Advantage:
    def adv_result(self):
        minus_result = self.player1.points - self.player2.points
        if minus_result == 1:
            result = "Advantage player1"
        elif minus_result == -1:
            result = "Advantage player2"
        return result


class Win:
    def win_result(self):
        minus_result = self.player1.points - self.player2.points
        if minus_result >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"
        return result


class MiddleScore:
    def middle_score(self):
        temp_score = 0
        result = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1.points
            else:
                result += "-"
                temp_score = self.player2.points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temp_score]
        return result


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
