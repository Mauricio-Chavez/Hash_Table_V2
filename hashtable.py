#23 no hay colision
#None*size
# my_hash = (my_hash + ord(letter) * 13) % len(7)

class hash:
    def __init__(self,size):
        self.size=size
        self.table = [None] * self.size

    def get_hash(self, key):

        h = 0
        i = 1
        a = 7
        b = 11
        for char in key:
            h += (h * a + ord(char) * b * i)
            i += 1
        index = h % self.size
        return index

    def add(self, key, edad):
        index = self.get_hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append([key, edad])

    def get(self,key):
        index = self.get_hash(key)
        if self.table[index] is not None:
            for i in self.table[index]:
                if i[0] == key:
                    return i[1]
        else:
            print(f"Key '{key}' no disponible")
            return False

    def print_table(self):
        for i, v in enumerate(self.table):
            print(f"Indice {i}: {v}")



h = hash(15)
print(f"mauricio: {h.get_hash('mauricio')}")
print(f"fernanda: {h.get_hash('fernanda')}")
print(f"gael: {h.get_hash('gael')}")
print(f"rafael: {h.get_hash('rafael')}")
print(f"julian: {h.get_hash('julian')}")
print(f"samantha: {h.get_hash('samantha')}")
print(f"leag: {h.get_hash('leag')}")
print(f"oiram: {h.get_hash('oiram')}")
print(f"adnanref: {h.get_hash('adnanref')}")
print(f"leafar: {h.get_hash('leafar')}")
print(f"nailuj: {h.get_hash('nailuj')}")
print(f"oiciruam: {h.get_hash('oiciruam')}")
print(f"ahtnamas: {h.get_hash('ahtnamas')}")


print("-----------------")
print(h.get("ahtnamas"))
print(h.get("gael"))
print(h.get("oiram"))
print(h.get("mauricio"))
h.get("Mau")
h.add("ahtnamas",20)
h.add("gael",19)
h.add("oiram",19)
h.add("mauricio",18)

h.print_table()





