import pandas as pd


df = pd.read_csv('dataset.csv')

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

unique_teams = df['Team'].nunique()
print("Number of unique teams in Euro2012:", unique_teams)

high_scoring_teams = df[df['Goals'] > 6][['Team', 'Goals']]
print(high_scoring_teams)
