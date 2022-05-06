import pandas as pd
import json

#Variables
year = 2022
folder_path = 'E:/Personal/Github/electionsni/2022/NI/'

cons_info = pd.read_csv(folder_path + 'all-constituency-info.csv',encoding='UTF-8')
cons_info.fillna('', inplace=True)
#cons_info.options.display.float_format = '{:,.0f}'.format

#cons_info["constituency_number"] = (cons_info[int("constituency_number")])
cons_info['constituency_number'] = cons_info['constituency_number'].astype(str)
cons_info['valid_poll'] = cons_info['valid_poll'].astype(str)
cons_info['number_of_seats'] = cons_info['number_of_seats'].astype(str)

cons_info = cons_info.rename(columns={"constituency_name":"Constituency_Name",
                                        "constituency_number":"Constituency_Number",
                                        "directory":"Directory",
                                        "valid_poll":"Valid_Poll",
                                        "number_of_seats":"Number_Of_Seats",
                                        "total_poll":"Total_Poll",
                                        "voting_age_pop":"Voting_Age_Pop",
                                        "quota":"Quota",
                                        "total_electorate":"Total_Electorate",
                                        "spoiled":"Spoiled"})

cons_info = (cons_info.groupby(['Constituency_Name', 'Constituency_Number', 'Directory'])
                        .apply(lambda x: x[['Valid_Poll', 'Number_Of_Seats', 'Total_Poll', 'Voting_Age_Pop', 'Quota', 'Constituency_Name', 'Constituency_Number', 'Total_Electorate', 'Spoiled']].to_dict('records'))
                        .reset_index()
                        .rename(columns={0:'countInfo'})

                        .to_json(orient='records'))

cons_info_full = {'Constituencies':json.loads(cons_info)}

with open(folder_path + 'all-constituency-info.json', 'w') as outfile:
    outfile.write(json.dumps(cons_info_full, indent=4))