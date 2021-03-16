from collections import namedtuple
from typing import List

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def _all_scores_are_in_range(scores):
    return all(score in DICE_VALUES for score in scores)


def calculate_score(scores: List) -> int:
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    if not _all_scores_are_in_range(scores):
        raise ValueError('Includes invalid dice roll(s)')

    return sum(score for score in scores if score >= MIN_SCORE)


def get_winner(players: List[Player]) -> Player:
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    if not all(_all_scores_are_in_range(player.scores) for player in players):
        raise ValueError

    player_scores_len = {len(player.scores) for player in players}

    if len(player_scores_len) > 1:
        raise ValueError('Players with different amount of score')

    return max(players, key=lambda player: calculate_score(player.scores))






