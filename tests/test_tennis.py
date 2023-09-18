import pytest

from src.tennis_katas.tennis_game1 import TennisGame1
from src.tennis_katas.tennis_game2 import TennisGame2
from src.tennis_katas.tennis_game3 import TennisGame3
from src.tennis_katas.tennis_game4 import TennisGame4

from test_tennis_game import test_cases, play_game


@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game1(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()


@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game2(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()


@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game3(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame3, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()


@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game4(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame4, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()
