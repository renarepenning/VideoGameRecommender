import pandas as pd
import numpy as np
import os

df = pd.read_csv('C:/Users/Matthew Raw/Downloads/IGDB_games.csv').set_index('id')
test = df.iloc[5005]

def conjunction(lst1, lst2):
    return list(set(lst1) & set(lst2))

def disjunction(lst1, lst2):
    return list(set(set(lst1) | set(lst2)))

def clean(array):
    try:
        array = array.split('[')[1].split(']')[0].split(', ')
    except:
        print(array)
    return list(map(lambda x: int(x), array))

def transform_column(target, column, df=df):
    test = clean(target[column])
    col = df[column].dropna().apply(clean)
    func = lambda x: conjunction(x, test)
    conj = col.apply(func)
    func = lambda x: disjunction(x, test)
    disj = col.apply(func)
    score = conj.apply(lambda x: len(x)) / disj.apply(lambda x: len(x)) 
    return score
    
def transform(columns, test, df=df):
    df['Columns Counted'] = 0
    for col in columns:
        print(col)
        col_name = col + ' score'
        df[col_name] = 0
        try:
            ser = transform_column(test, col)
            for id in ser.index:
                try:
                    df.loc[id, col_name] = ser.loc[id]
                    df.loc[id, 'Columns Counted'] = df.loc[id, 'Columns Counted'] + 1
                except:
                    pass
        except:
            pass
    col_map = list(map(lambda x: x + ' score', columns))
    df['Total'] = df[col_map].sum(axis=1)
    return df
transform(['genres', 'themes', 'game_modes','tags', 'platforms', 'keywords'], test).sort_values('Total')
