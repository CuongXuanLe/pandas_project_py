import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dask.dataframe as dd
import csv
# add -> commit -> push

chess_df = pd.read_csv('chess_games_small.csv')
# chess_df.info()


def winner_players():
    chess_df['Winner'] = np.where(chess_df['Result'] == '1-0', 'White_win', np.where(chess_df['Result'] == '0-1', 'Black_win', 'Draw'))
    chess_games = chess_df[['White', 'WhiteElo', 'Black', 'BlackElo', 'AN', 'Winner']]
    chess_games.to_csv('List_Winner.csv')
    return chess_df


# Look at summary of differences in Elo ratings
def summary_elo():
    chess_df['Summary_Elo'] = chess_df['WhiteElo'] - chess_df['BlackElo']
    smr_df = chess_df['Summary_Elo'].describe()
    return smr_df


def draw_chart():
    # Calculate difference between White_Elo and Black_Elo ratings
    chess_df['Elo_ratings'] = chess_df['WhiteElo'] - chess_df['BlackElo']
    # Draw chart
    plt.figure(figsize=(10, 6))
    plt.xlim(-1200, 1200)
    plt.title("Difference Between Player Elo Ratings", fontsize=20)
    plt.xlabel("Difference in Elo Ratings", fontsize=15)
    plt.ylabel("Number of \n Event", fontsize=15, rotation=0, labelpad=45)
    plt.hist(chess_df['Elo_ratings'], bins=50)
    plt.tight_layout()
    plt.savefig("Compare_elo.png")
    return chess_df


# Ques 4: Create column to find who won and draw game
winner_players()
# Ques 5:
# Ques 8: Summary of differences in Elo ratings
print(summary_elo())
# Ques 9: draw chart about Elo ratings between Black and White players
draw_chart()

