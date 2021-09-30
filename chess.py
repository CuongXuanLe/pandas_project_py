# import visualization libraries, pandas and numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Ques 2: Read the CSV file as dataframe
chess_df = pd.read_csv('chess_games_small.csv')
# chess_df.info()


def count_num():
    cnt_num = pd.value_counts(chess_df['Termination'])
    print(cnt_num)
    return cnt_num


def winner_players():
    chess_df['Winner'] = np.where(chess_df['Result'] == '1-0', 'White_win',
                                  np.where(chess_df['Result'] == '0-1', 'Black_win', 'Draw'))
    chess_games = chess_df[['White', 'WhiteElo', 'Black', 'BlackElo', 'AN', 'Winner']]
    chess_games.to_csv('List_Winner.csv')
    return chess_df


def rate_win():
    lst_wn = pd.read_csv('List_Winner.csv')
    plt.hist(lst_wn['Winner'], rwidth=20.0, alpha=0.5, color='green', bins=5)
    # x and y-axis labels
    plt.xlabel('Rate win')
    plt.ylabel('Players')
    # plot title
    plt.title('Chess games')
    plt.show()


def excellent_players():
    chess_df['Top_BlackElo'] = chess_df['BlackElo'].astype(int)
    chess_df['Top_WhiteElo'] = chess_df['WhiteElo'].astype(int)
    # Find the all the player have elo above 2000
    ex_plr = chess_df[(chess_df['Top_WhiteElo'] >= 2000) & (chess_df['Top_BlackElo'] >= 2000)]
    # print(ex_plr.head(100))
    print(ex_plr)
    return ex_plr


# Look at summary of differences in Elo ratings
def summary_elo():
    chess_df['Summary_Elo'] = chess_df['WhiteElo'] - chess_df['BlackElo']
    smr_df = chess_df['Summary_Elo'].describe()
    print(smr_df)
    return smr_df


def draw_chart():
    # Calculate difference between White_Elo and Black_Elo ratings
    chess_df['Elo_ratings'] = chess_df['WhiteElo'] - chess_df['BlackElo']
    # Draw chart
    plt.figure(figsize=(10, 6))
    plt.xlim(-1200, 1200)
    plt.xlabel("Difference in Elo Ratings", fontsize=15)
    plt.ylabel("Number of \n Event", fontsize=15, rotation=0, labelpad=45)
    plt.hist(chess_df['Elo_ratings'], bins=200)
    plt.tight_layout()
    plt.savefig("Compare_elo.png")
    return chess_df


def pie_chart():
    cls_tour = 0
    lst_event = list(set(chess_df['Event'].values.tolist()))
    cnt, label = [], []
    lst = chess_df['Event'].value_counts()
    for i in lst_event:
        num = lst[i]
        if num / len(chess_df) < 0.035:
            cls_tour += num
        else:
            cnt.append(num)
            label.append(i)
    cnt.append(cls_tour)
    label.append('Classical tournament')
    colors = ("red", "green", "orange", "cyan", "blue", "grey")
    plt.pie(cnt,
            explode=[0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
            colors=colors,
            labels=label,
            autopct='%1.2f',
            startangle=15,
            shadow=True)
    plt.legend()
    plt.title = 'Pie Chart'
    plt.show()


# Ques 3: Show the first 5 rows of each dataframe
print(chess_df.head(5))
# Ques 4: Count the number of Normal, Time forfeit, Abandoned, Rules infraction, ... in Terminator column
count_num()
# Ques 5: Generating List_Winner.csv file to list who won and draw game
winner_players()
# Ques 6: From the List_Winner.csv, draw a chart to show win rate
rate_win()
# Ques 7: List all Top player between Black and White
excellent_players()
# Ques 8: Summary of differences in Elo ratings
print('Summary of differences in elo ratings')
summary_elo()
# Ques 9: draw pie chart to show top events held
pie_chart()
# Ques 10: Create picture of chart about Elo ratings between Black and White players
draw_chart()
