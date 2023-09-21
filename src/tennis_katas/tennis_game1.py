from src.tennis_katas.tennis import Player, Result


class TennisGame1:
    def __init__(
        self,
        player1_name: str,
        player2_name: str,
    ):
        self.player1 = Player(player1_name, 0)
        self.player2 = Player(player2_name, 0)

    def won_point(self, player_name: str):
        if player_name == self.player1.name:
            self.player1.score_point()
        else:
            self.player2.score_point()

    def score(self) -> str:
        return Result(self.player1, self.player2).get_result()
