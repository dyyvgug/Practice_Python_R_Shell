from class_mendel import Pea

#green = Pea('gg')
#print(green)

class PeaStrain:
    def __init__(self, peas):
        self.peas = peas

    def __repr__(self):
        return 'strain with {} peas'.format(len(self.peas))

yellow = Pea('GG')
green = Pea('gg')
strain = PeaStrain([yellow, green])
print(strain)
print(strain.peas)