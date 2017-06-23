import csv
from collections import namedtuple , defaultdict, Counter
from pprint import pprint
import glob
from kmean import k_means,assign_data

accumulated_record = defaultdict(list)
Senator = namedtuple('Senator', ['name', 'party', 'state'])
vote_value = {'Yea': 1, 'Nay': -1 , 'Not Voting': 0}
for filename in glob.glob('modernpython-1-master\\congress_data\\*.csv'):

    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)

        for person, state, district , vote , name , party in reader:
            senator = Senator(name, party , state)
            accumulated_record[senator].append(vote_value[vote])

# transform the data 
record = { senator : tuple(votes) for senator, votes in  accumulated_record.items()}

#calc the centroid and assign data
centroids = k_means(record.values(),k=3)
clustered_votes = assign_data(centroids, record.values())

# for centroid in centroids:
#     for x in centroid:
#         print(f'{x:.2f}', end = " ")
#     print()

#build a reverse mapping
vote_to_senators = defaultdict(list)
for senator, votehistory in record.items():
    vote_to_senators[votehistory].append(senator)
assert sum(len(cluster) for cluster in vote_to_senators.values()) == 100

#display the cluster
for i , votes_in_cluser in enumerate(clustered_votes.values(), start=1):
    party_totals = Counter()
    print(f'===================Voting Cluser #{i}===========================')
    for votes in set(votes_in_cluser):
        for senator in vote_to_senators[votes]:
            party_totals[senator.party] += 1
            print(senator)
    pprint(party_totals)
