import pandas as pd

def load_players(file_path):
    return pd.read_csv(file_path)

def load_matches(file_path):
    return pd.read_csv(file_path)

def merge_players_matches(players_df, matches_df):
    merged = pd.merge(matches_df, players_df, on='PlayerID', how='inner')
    expected_cols = ["PlayerID", "Name", "Team", "Role", "Age", "MatchID", "Runs", "Balls", "Fours", "Sixes", "Wickets", "Catches", "Date"]
    return merged[expected_cols]

def total_runs_per_team(merged_df):
    return merged_df.groupby('Team', as_index=False)['Runs'].sum()

def calculate_strike_rate(merged_df):
    df = merged_df.copy()
    df['StrikeRate'] = (df['Runs'] / df['Balls']) * 100
    df['StrikeRate'] = df['StrikeRate'].fillna(0)
    return df[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]


def runs_agg_per_player(merged_df):
    agg_df = merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'max', 'min']).reset_index()
    return agg_df[['PlayerID', 'Name', 'mean', 'max', 'min']]

def avg_age_by_role(players_df):
    return players_df.groupby('Role', as_index=False)['Age'].mean()

def total_matches_per_player(matches_df):
    counts = matches_df.groupby('PlayerID').size().reset_index(name='MatchCount')
    return counts

def top_wicket_takers(merged_df):
    wickets = merged_df.groupby(['PlayerID', 'Name'], as_index=False)['Wickets'].sum()
    return wickets.sort_values('Wickets', ascending=False).head(3)

def avg_strike_rate_per_team(merged_df):
    df = merged_df.copy()
    df['StrikeRate'] = (df['Runs'] / df['Balls']) * 100
    df['StrikeRate'] = df['StrikeRate'].fillna(0)
    return df.groupby('Team', as_index=False)['StrikeRate'].mean()

def catch_to_match_ratio(merged_df):
    total_catches = merged_df.groupby('PlayerID', as_index=False)['Catches'].sum()
    match_counts = merged_df.groupby('PlayerID').size().reset_index(name='MatchesPlayed')
    merged = pd.merge(total_catches, match_counts, on='PlayerID')
    merged['CatchToMatchRatio'] = merged['Catches'] / merged['MatchesPlayed']
    return merged[['PlayerID', 'CatchToMatchRatio']]