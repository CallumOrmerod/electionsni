import pandas as pd
import json

#Variables
year = 2022
folder_path = 'E:/Personal/Github/electionsni/2022/NI/'

cons_info = pd.read_csv(folder_path + 'all-constituency-info.csv',encoding='UTF-8')
cons_info.fillna('', inplace=True)

cons_info = (cons_info.groupby(['constituency_name', 'constituency_number', 'directory'])
                        .apply(lambda x: x[['valid_poll', 'number_of_seats', 'total_poll', 'voting_age_pop', 'quota', 'constituency_name', 'constituency_number', 'total_electorate', 'spoiled']].to_dict('records'))
                        .reset_index()
                        .rename(columns={0:'countInfo'})

                        .to_json(orient='records'))

cons_info_full = {'Constituencies':json.loads(cons_info)}

with open(folder_path + 'all-constituency-info.json', 'w') as outfile:
    outfile.write(json.dumps(cons_info_full, indent=4))