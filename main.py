import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt


def _recommend():
    pd.set_option("display.max_columns", None)

    data = pd.read_excel('Football_Fantasy_Data_v2.1.xls', sheet_name='2020')
    # df = pd.DataFrame(data)
    # print(df.shape)
    # print(df.head(5))
    # return 0
    # df.drop(['Team', 'Games G',], axis=1, inplace=True)
    # print(df.head())
    # print(df.columns)
    # print(df['Year'].unique())
    # df.drop(['Rk', 'Year', 'Fantasy DKPt', 'Fantasy FDPt', 'Fantasy VBD', 'Scoring TD', 'Scoring 2PM', 'Scoring 2PP','Fumbles Fmb', 'Fumbles FL', 'Fantasy PosRank', 'Fantasy OvRank', 'Games G', 'Games GS']
    #         , axis=1
    #         , inplace=True)
    # print(df['Age'].value_counts())
    # print(df['Team'].value_counts())
    # print(df.head(5))
    # pd.set_option("display.max_columns", None, "display.max_columns", None)
    # print(df.columns)
    # print(df.tail(5))

    # df = pd.DataFrame(data,columns=['Player', 'Team', 'FantPos', 'Age', 'Fantasy FantPt',
    #    'Fantasy PPR', 'Fantasy DKPt', 'Fantasy FDPt', 'Fantasy VBD',
    #    'Fantasy PosRank', 'Fantasy OvRank'])
    # print(df.columns)
    # print(df.shape)
    # print(df.head(5))
    # print(df.tail(5))

    # print(df['Player'].isna().sum())
    # print(df['Player'].isnull().sum())
    # print(df['Team'].isna().sum())
    # print(df['Team'].isnull().sum())
    # print(df['FantPos'].isna().sum())
    # print(df['FantPos'].isnull().sum())

    # print(df['Age'].isna().sum())
    # print(df['Age'].isnull().sum())

    # print(df['Fantasy FantPt'].isna().sum())
    # print(df['Fantasy FantPt'].isnull().sum())

    # print(df['Fantasy PPR'].isna().sum())
    # print(df['Fantasy PPR'].isnull().sum())

    # print(df['Fantasy DKPt'].isna().sum())
    # print(df['Fantasy DKPt'].isnull().sum())

    # print(df['Fantasy FDPt'].isna().sum())
    # print(df['Fantasy FDPt'].isnull().sum())

    # print(df['Fantasy VBD'].isna().sum())
    # print(df['Fantasy VBD'].isnull().sum())

    # print(df['Fantasy PosRank'].isna().sum())
    # print(df['Fantasy PosRank'].isnull().sum())

    # print(df['Fantasy OvRank'].isna().sum())
    # print(df['Fantasy OvRank'].isnull().sum())

    # df.drop('Fantasy VBD', axis=1, inplace=True)
    # df.drop('Fantasy OvRank', axis=1, inplace=True)
    # df = df[df['Fantasy FantPt'].notna()]
    # df = df[df['Fantasy FDPt'].notna()]
    # df = df[df['Fantasy DKPt'].notna()]
    # df = df[df['Fantasy PPR'].notna()]
    # df = df[df['FantPos'].notna()]

    # print(df.head(5))

    # print(df['Fantasy FantPt'].isna().sum())
    # print(df['Fantasy FantPt'].isnull().sum())

    # print(df['Age'].mean())
    # print(df['Age'].quantile(0.7))

    # print(df['Fantasy FantPt'].mean())
    # print(df['Fantasy FantPt'].quantile(0.7))

    # print(df['Fantasy PPR'].mean())
    # print(df['Fantasy PPR'].quantile(0.7))

    # print(df['Fantasy DKPt'].mean())
    # print(df['Fantasy DKPt'].quantile(0.7))
    #
    # print(df['Fantasy FDPt'].mean())
    # print(df['Fantasy FDPt'].quantile(0.7))

    # print(df['Fantasy PosRank'].mean())
    # print(df['Fantasy PosRank'].quantile(0.7))

    # print(df.columns)
    # print(df.head(5))
    # print(df['FantPos'].value_counts())

    # pos_num_set = {'QB': 2, 'WR': 3, 'RB': 2, 'TE': 2}
    # df_pos = pd.DataFrame(list(pos_num_set.items()), columns=['Position', 'Count'])
    # # print(df_pos)
    #
    # # print(df.head(5))
    # # return 0
    # df_team = pd.DataFrame(columns=['Player', 'Position'])
    # point_left = 2000
    # for p in range(len(df)):
        # print('Name:%s ID: %s', str(p['Player']).split('\\'))
    #     if point_left > 0:
    #         position = df.iloc[p, 2]
    #         print(position)
    #         spots = df_pos[position]
    #         print(spots)
    #         if spots > 0:
    #             df_team['Player'] = df.iloc[p, 0]
    #             print(df_team['Player'])
    #             df_team['Position'] = df.iloc[p, 2]
    #
    #             df_pos[df.iloc[p, 2]] = spots -1
    #             # ({df.iloc[p, 2]:str(int(pos_num_set.get(df.iloc[p, 2]))-1)})
    #
    #             point_left - df.iloc[p, 4]
    #             print("Points remaining-"+point_left)
    #     else:
    #         break;
    # print('Completed one iteration')
    # print(df_team)

    # filter out unnecessary columns
    df = pd.DataFrame(data, columns=['Player', 'Team', 'FantPos', 'Receiving Rec', 'Fantasy FantPt'])
    # print(df.head())
    # remove filler rows put there by pro-football-reference
    # df = df.loc[df['Player'] != 'Player']
    # print(df.shape)

    # drop rows with NA values
    df = df.dropna()
    # print(df.shape)

    # format these columns as integers (A rough estimation of fantasy points is fine)
    df['Rec'] = df['Receiving Rec'].astype(int)
    df['FantPt'] = df['Fantasy FantPt'].astype(int)

    # create a column for full PPR
    df = df.assign(PPRFantPt=lambda x: x.FantPt + x.Rec)

    print(df.head(5))

    position_cutoff = {
        'RB': 25,
        'QB': 13,
        'WR': 25,
        'TE': 13
    }

    replacement_values = dict()

    for position, cutoff in position_cutoff.items():
        pos_df = df.loc[df['FantPos'] == position]
        pos_df = pos_df.sort_values(by='PPRFantPt', ascending=False)
        replacement_player = pos_df.iloc[cutoff, :]
        replacement_values[replacement_player.FantPos] = replacement_player.FantPt

    # make a dataframe out of the dictionary above
    replacement_values = pd.DataFrame(replacement_values, index=range(0, 1)).transpose().reset_index()

    replacement_values.columns = ['FantPos', 'Replacement']

    ppr_vor_df = df.merge(replacement_values).assign(PPR_Value=lambda x: x.PPRFantPt - x.Replacement).sort_values(
        by='PPR_Value', ascending=False)
    # print(ppr_vor_df.head(10).reset_index(drop=True))

    # print(ppr_vor_df.head(10))

    ppr_team_vor = ppr_vor_df[:100].groupby('Team', as_index=False)['PPR_Value'].sum().sort_values(by='PPR_Value', ascending=False)[:10]

    print(ppr_team_vor.head(10))






def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


if __name__ == '__main__':
    # print_hi('PyCharm')
    _recommend()