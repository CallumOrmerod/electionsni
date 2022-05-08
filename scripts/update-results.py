import json
import pandas as pd

path_init = 'C:/Personal/Github/electionsni/2022/constituency/'

constituency = 'strangford'

full_path = path_init + constituency + '/'

info = pd.read_csv(full_path + 'ConstituencyCount.csv',encoding='UTF-8')
counts = pd.read_csv(full_path + 'Count.csv', encoding='UTF-8')
counts.fillna('', inplace=True)


info = info.rename(columns={"constituency_name":"Constituency_Name",
                            "constituency_number":"Constituency_Number",
                            "directory":"Directory",
                            "valid_poll":"Valid_Poll",
                            "number_of_seats":"Number_Of_Seats",
                            "total_poll":"Total_Poll",
                            "voting_age_pop":"Voting_Age_Pop",
                            "quota":"Quota",
                            "total_electorate":"Total_Electorate",
                            "spoiled":"Spoiled"})



#cast all cols to strings
info['Constituency_Number'] = info['Constituency_Number'].astype(str)
info['Total_Electorate'] = info['Total_Electorate'].astype(str)
info['Total_Poll'] = info['Total_Poll'].astype(str)
info['Valid_Poll'] = info['Valid_Poll'].astype(str)
info['Spoiled'] = info['Spoiled'].astype(str)
info['Quota'] = info['Quota'].astype(str)
info['Number_Of_Seats'] = info['Number_Of_Seats'].astype(str)
info['Voting_Age_Pop'] = info['Voting_Age_Pop'].astype(str)

counts['Constituency_Number'] = counts['Constituency_Number'].astype(str)
counts['Candidate_Id'] = counts['Candidate_Id'].astype(str)
counts['Count_Number'] = counts['Count_Number'].astype(str)
counts['Candidate_First_Pref_Votes'] = counts['Candidate_First_Pref_Votes'].astype(str)
counts['Transfers'] = counts['Transfers'].astype(str)
counts['Total_Votes'] = counts['Total_Votes'].astype(str)

new_results = {"Constituency":{"countInfo":json.loads(info.to_json(orient = 'records'))[0], "countGroup":json.loads(counts.to_json(orient = 'records'))}}



with open(full_path + 'Resultsjson.json', 'w') as outfile:
    outfile.write(json.dumps(new_results, indent=4))





#print(new_results)


