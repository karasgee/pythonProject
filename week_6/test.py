import collections
d1 = {'s': {'x': 2, 'kk' : '12'}}
d2 = {'d': {'m': 5, 'jj' : '13'}}
c = collections.ChainMap(d1,d2)
c['v']=5
print(c[ 'd'])