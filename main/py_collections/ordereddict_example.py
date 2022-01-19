from collections import OrderedDict

sportsTeams = [
    ("Royals", (18, 12)),
    ("Rockets", (24, 6)),
    ("Cardinals", (20, 10)),
    ("Dragons", (22, 8)),
    ("Kings", (15, 15)),
    ("Chargers", (20, 10)),
    ("Jets", (16, 14)),
    ("Warriors", (25, 5))
]

sportsTeams.sort(key=lambda item: item[1][0])
print(sportsTeams)

teams = OrderedDict(sportsTeams)
print(teams)

print(teams.popitem(False))

a = OrderedDict({"a": 1, "b": 2, "c": 3})
b = OrderedDict({"a": 1, "b": 2, "c": 3})
c = OrderedDict({"a": 1, "c": 3, "b": 2})

print(a == b)
print(a == c)

a = {"a": 1, "b": 2, "c": 3}
b = {"a": 1, "b": 2, "c": 3}

print(a == b)
