import pandas as pd


df = pd.read_csv('dataset.csv')

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

num_teams = len(df)
print("Number of teams participated in Euro2012:", num_teams)

high_scoring_teams = df[df['Goals'] > 6][['Team', 'Goals']]
print(high_scoring_teams)
