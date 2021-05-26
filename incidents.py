import csv
from pdpyras import APISession
api_token = 'u+ncmcjTu2vd_8cU_nJw' ## user_id = 'P8KLUCQ'
api_client = APISession(api_token)

my_user = api_client.find('users', 'ammaramalik@gmail.com', attribute='email')
if my_user is not None:
    my_incidents = api_client.iter_all(
        'incidents',
        params={'user_ids[]':[my_user['id']],
                'statuses[]':['triggered', 'acknowledged', 'resolved'],
                'sort_by':['incident_number:asc']},
        )

if my_incidents:
    with open('incidents.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        first = next(my_incidents)
        writer.writerow(list(first.keys()))
        writer.writerow(list(first.values()))
        for incident in my_incidents:
            writer.writerow(list(incident.values()))
