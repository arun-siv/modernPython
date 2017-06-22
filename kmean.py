from typing import Iterable,Tuple
from math import fsum, sqrt
from pprint import pprint
from collections import defaultdict
from functools import partial
from random import sample

Point = Tuple[int, ...]


#mean
def mean(data: Iterable[float]) -> float:
    'Acurate arithematic mean'
    data = list(data)
    return fsum(data) / len(data)


#distan

def dist(p: Point,q: Point, fsum=fsum, sqrt=sqrt, zip=zip):
    'Euclidean distance '
    return sqrt(fsum([(x-y) ** 2 for x,y in zip(p,q)]))

# for point in points:
#     print(point, dist(point, (9,39,20)))

def assign_data(centroids, data):
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)

def compute_centroid(groups):
    'computer centroid of each group'
    return [tuple(map(mean,zip(*group))) for group in groups]

def k_means(data,k=2):
    data = list(data) # turns into squence
    centroids = sample(data, k)
    iterations = 50
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroid(labeled.values())
    return centroids
if __name__ == '__main__':

    points = [
        (10,41,23),
        (22,30,29),
        (11,42,5),
        (20,32,4),
        (12,40,12),
        (21,36,23)
    ]

    centroids = k_means(points, k=3)
    d = assign_data(centroids, points)
    pprint(d, width=50)