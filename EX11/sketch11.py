import itertools
d1 = {"hepititis":10,"flu":8,"cough":3,"hiv":4,"difteria":6,"measles":6}

list1 = sorted(d1, key=d1.get, reverse = True )

print(list1)

subsets_list1_3 = list(itertools.combinations(list1,3))

print(subsets_list1_3)

print(d1['mono'])