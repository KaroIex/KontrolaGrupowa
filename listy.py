lista_lancuchow = ['kaczka', 'dziwaczka', 'ananas', 'grzyb', 'kosa', 'kamień']

lista_lancuchow = sorted(lista_lancuchow)

lista_lancuchow += ['kotek', 'ślimak', 'lustro', 'okno', 'yeti', 'jeż', 'mycie', 'koty', 'łupina', 'dwa']

lista_lancuchow = sorted(lista_lancuchow)

lista_lancuchow += ['kurczak', 'koń', 'lud', 'lodowiec', 'koszary', 'bagno', 'widok', 'telewizja', 'trzy', 'pięć']



class Element:
    def __init__(self, name):
        self.name = name

elements = []
elements.append(Element("A"))
elements.append(Element("B"))
elements.append(Element("C"))
elements.append(Element("D"))
elements.append(Element("E"))

elements.sort(key=lambda x: x.name)

elements.append(Element("D"))
elements.append(Element("U"))
elements.append(Element("P"))
elements.append(Element("K"))
elements.append(Element("I"))

elements.append(Element("K"))
elements.append(Element("U"))
elements.append(Element("R"))
elements.append(Element("W"))
elements.append(Element("Y"))



elements.sort(key=lambda x: x.name, reverse=True)


elements.append(Element("D"))
elements.append(Element("U"))
elements.append(Element("P"))
elements.append(Element("K"))
elements.append(Element("I"))

elements.append(Element("C"))
elements.append(Element("Y"))
elements.append(Element("C"))
elements.append(Element("K"))
elements.append(Element("I"))


lista_liczb = [2,4,]
lista_liczb.sort(reverse=True)



lista_liczb.extend([6, 7, 8, 9, 10])
lista_liczb.extend([11, 12, 13, 14, 15])

lista_liczb += [54, 324, 234, 12, 45, 71, 564, 453, 342, 56]
lista_liczb += [453, 321, 32, 432, 234, 342, 564, 6574, 34, 78421]


lista_liczb.extend([6, 7, 8, 9, 10])
lista_liczb.extend([11, 12, 13, 14, 15])
lista_liczb.extend([16, 17, 19, 20])
lista_liczb.extend([98, 97, 96])
lista_liczb = [111, 211, 311, 411, 511]
lista_liczb = [122, 222, 322, 422, 522]


lista_liczb.extend([6, 8, 10])
lista_liczb.extend([ 12, 14])
lista_liczb.extend([16, 18, 20])
lista_liczb.extend([ 22, 24])
lista_liczb.extend([26, 27, 28, 29, 30, 31, 32, 33, 34, 35])

