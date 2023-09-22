from dataclasses import dataclass
from enum import IntEnum


class ScoreSystem(IntEnum):
    """It is used to translate the score points to the tennis terms.
    Also used to get rid of the "magic numbers" inside the code.
    """

    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE = 4
    ADVANTAGE = 5


@dataclass
class Player:
    """Class that represents the player entity. The player has name and points and an action that is related to,
    the score of the point."""

    name: str
    points: int

    def score_point(self):
        self.points += 1


class Result:
    """The main class of the solution. It is extended by Draw, OngoingResult, Advantage and Win."""

    def __init__(self, _player1, _player2) -> None:
        self.player1 = _player1
        self.player2 = _player2

    def get_result(
        self,
    ) -> str:
        """The main method of the solution. Here are defined the rules of the game and also the winner is decided.

        Returns:
            str: description of the final result
        """
        if self.player1.points == self.player2.points:
            return Draw.get_result(self)
        elif Result.there_is_advantage(self) and abs(self.player1.points - self.player2.points) == ScoreSystem.FIFTEEN:
            return Advantage.get_result(self)
        elif Result.there_is_advantage(self):
            return Win.get_result(self)
        else:
            return OngoingScore.get_result(self)

    def result_description(self, score: int = 0) -> str:
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[score]

    def there_is_advantage(self):
        return True if (self.player1.points >= ScoreSystem.DEUCE or self.player2.points >= ScoreSystem.DEUCE) else False


class Draw(Result):
    def get_result(self) -> str:
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player1.points, "Deuce")


class OngoingScore(Result):
    def get_result(self) -> str:
        return f"{self.result_description(self.player1.points)}-{self.result_description(self.player2.points)}"


class Advantage(Result):
    def get_result(self) -> str:
        if self.player1.points > self.player2.points:
            return "Advantage player1"
        else:
            return "Advantage player2"


class Win(Result):
    def get_result(self) -> str:
        if self.player1.points > self.player2.points:
            return "Win for player1"
        else:
            return "Win for player2"
