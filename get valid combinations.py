from itertools import permutations
import enchant
broker = enchant.Broker()
broker.describe()
broker.list_languages()
d= enchant.Dict("en_US")
op= set()

inp = "Ravi"
letter = [x.lower() for x in inp]

for n in range(3,len(inp)):
    for y in list(permutations(letter,n)):
        z="".join(y)
        if d.check(z):
            op.add(z)
print(op)
