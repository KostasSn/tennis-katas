from dataclasses import dataclass

# from abc import ABC, abstractmethod
# from enum import Enum


@dataclass
class Player:
    name: str
    points: int

    def score_point(self):
        self.points += 1


class Result:
    """_summary_"""

    def __init__(self, _player1, _player2) -> None:
        self.player1 = _player1
        self.player2 = _player2

    def get_result(
        self,
    ) -> str:
        pass

    def result_description(self, score: int = 0):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[score]


class Draw(Result):
    def get_result(self):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player1.points, "Deuce")


class MiddleScore(Result):
    def get_result(self):
        return f"{self.result_description(self.player1.points)}-{self.result_description(self.player2.points)}"


class AdvOrWin(Result):
    def get_result(self):
        minus_result = self.player1.points - self.player2.points
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"


# class Advantage(Result):
#     def get_result(self):
#         minus_result = self.player1.points - self.player2.points
#         if minus_result == 1:
#             return "Advantage player1"
#         elif minus_result == -1:
#             return "Advantage player2"


# class Win(Result):
#     def get_result(self):
#         minus_result = self.player1.points - self.player2.points
#         if minus_result >= 2:
#             return "Win for player1"
#         else:
#             return "Win for player2"

# class ScoreSystem(Enum):
#     LOVE = 0
#     FIFTEEN = 1
#     THIRTY = 2
#     FORTY = 3
#     DEUCE = 4
#     ADVANTAGE = 5
