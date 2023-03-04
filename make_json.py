import pandas as pd
import numpy as np
import os


# extract top n users, each with 7/1/1/1, ten songs in total
def top_player_filter(all_player_data: pd.DataFrame, n):
    n_players = list(all_player_data.groupby("player_id"))
    n_players.sort(key=lambda a: len(a[1]), reverse=True)
    for i in range(0, n):
        songs = n_players[i][0].sort(by=['play_date'], ascending=[False])

