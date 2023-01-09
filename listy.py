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
