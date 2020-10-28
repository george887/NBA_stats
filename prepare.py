import matplotlib.pyplot as plt
import pandas as pd

def prepare_nba(df):
    '''
   This function cleans up the column names, deletes columns, renames some columns 
   to read easier and makes histograms of the columns
    '''
    # Lower casing columns names
    df = df.rename(str.lower, axis='columns')

    # Creating dummy df for home
    df = pd.get_dummies(df, columns=['home', 'winorloss'], drop_first=True)

    # Renaming column names
    df = df.rename(columns={'fieldgoals.': 'fieldgoal_pct', 'x3pointshots.': 'x3pointshots_pct', 
                   'freethrows.': 'freethrows_pct', 'opp.fieldgoals.': 'opp_fieldgoal_pct',
                  'opp.freethrows.':'opp_freethrows_pct', 'opp.3pointshots.':'opp_3pointshots_pct',
                  'winorloss_W':'win', 'home_Home':'is_home'})
    # dropping unamed column
    df = df.drop(columns =['unnamed: 0'])
    
    for col in df.columns:
        plt.hist(df[col])
        plt.title(col)
        plt.show()
    
    return df