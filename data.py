import pandas

data_frame = pandas.read_csv('euro-2020.csv')

group_games = data_frame.iloc[0: 36]

home_teams = group_games['Home Team'].tolist()
away_teams = group_games['Away Team'].tolist()
dates = group_games['Away Team'].tolist()
locations = group_games['Location'].toList()
