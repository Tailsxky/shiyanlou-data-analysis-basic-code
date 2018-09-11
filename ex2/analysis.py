import json
import pandas as pd
from pandas import Series, DataFrame
import os


def analysis(file, user_id):
    times = 0
    minutes = 0

    #check whether file exists
    if not os.path.exists(file):
        return 0
    else:
        # save as dataframe
        jsonData = pd.read_json(file)
        df = DataFrame(jsonData)
        
        minutes = df[df['user_id'] == user_id]['minutes'].sum()
        times = len(df[df['user_id'] == user_id])

    if(times!=0):
        return times, minutes
    else:
        return 0



#print(analysis('../user_study.json', 172984))
