from src.tennis_katas.tennis import Player, ScoreSystem


class TennisGame1:
    def __init__(
        self,
        player1_name: Player,
        player2_name: Player,
    ):
        self.player1 = Player(player1_name, 0)
        self.player2 = Player(player2_name, 0)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score_point()
        else:
            self.player2.score_point()

    def score(self):
        if self.player1.points == self.player2.points:
            return self.draw_result()
        elif self.player1.points >= 4 or self.player2.points >= 4:
            return self.final_result()
        else:
            return self.live_result()

    def draw_result(self):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player1.points, "Deuce")

    def final_result(self):
        minus_result = self.player1.points - self.player2.points
        if minus_result == 1:
            result = "Advantage player1"
        elif minus_result == -1:
            result = "Advantage player2"
        elif minus_result >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"
        return result

    def live_result(self):
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
