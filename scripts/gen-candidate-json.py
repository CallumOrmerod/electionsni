import pandas as pd
import json

#Variables
year = 2022
folder_path = 'E:/Personal/Github/electionsni/2022/NI/'

candidates = pd.read_csv(folder_path + 'full-candidates-list.csv',encoding='UTF-8')
candidates.fillna('', inplace=True)
candidates['party_id'] = candidates['party_id'].astype(str)
candidates['constituency_number'] = candidates['constituency_number'].astype(str)
candidates['candidate_id'] = candidates['candidate_id'].astype(str)
candidates = candidates.rename(columns={"constituency_name":"Constituency_Name",
                                        "constituency_number":"Constituency_Number",
                                        "surname":"Surname",
                                        "firstname":"Firstname",
                                        "gender":"Gender",
                                        "twitter":"Twitter",
                                        "party_name":"Party_Name",
                                        "outgoing_member":"Outgoing_Member",
                                        "candidate_id":"Candidate_Id",
                                        "directory":"Directory",
                                        "party_id":"Party_Id",
                                        "email":"Email",
                                        "photo_url":"Photo_URL"})



cons_candidates = (candidates.groupby(['Constituency_Name', 'Constituency_Number'])
                             .apply(lambda x: x[['Surname','Firstname', 'Gender', 'Twitter', 'Constituency_Name', 'Constituency_Number', 'Party_Name', 'Outgoing_Member', 'Candidate_Id', 'Directory', 'Party_Id', 'Email', 'Photo_URL']].to_dict('records'))
                             .reset_index()
                             .rename(columns={0:'Candidates'})
    
                             .to_json(orient='records'))

cons_candidates_full = {'Constituencies':json.loads(cons_candidates)}

with open(folder_path + 'all-candidates.json', 'w') as outfile:
    outfile.write(json.dumps(cons_candidates_full, indent=4))
    #json.dump(cons_candidates_full, outfile)

#print (json.dumps(cons_candidates_full, indent=4))


party_candidates = (candidates.groupby(['Party_Name', 'Party_Id'])
                             .apply(lambda x: x[['Surname','Firstname', 'Gender', 'Twitter', 'Constituency_Name', 'Constituency_Number', 'Party_Name', 'Outgoing_Member', 'Candidate_Id', 'Directory', 'Party_Id', 'Email', 'Photo_URL']].to_dict('records'))
                             .reset_index()
                             .rename(columns={"Party_Id":"Party_Number",0:'Candidates'})
                             .to_json(orient='records'))

party_candidates_full = {'Parties':json.loads(party_candidates)}

with open(folder_path + 'all-party-candidates.json', 'w') as outfile:
    outfile.write(json.dumps(party_candidates_full, indent=4))
    #json.dump(party_candidates_full, outfile)


#print(candidates.to_json())