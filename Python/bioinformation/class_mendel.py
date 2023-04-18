#!/usr/bin/python
# coding:utf-8

class Pea:

    def __init__(self, genotype):
        self.genotype = genotype

    def get_phenotype(self):
        if 'G' in self.genotype:
            return 'yellow'
        else:
            return 'green'

    def creat_offspring(self, other):
        offspring = []
        new_genotype = ''
        for haplo1 in self.genotype:
            for haplo2 in other.genotype:
                new_genotype = haplo1 + haplo2
                offspring.append(Pea(new_genotype))
        return offspring

    def __repr__(self):
        return '\t' + self.get_phenotype() + ' [{}]'.format(self.genotype)

yellow = Pea('GG')
green = Pea('gg')
f1 = yellow.creat_offspring(green)
f2 = f1[0].creat_offspring(f1[1])
print(f1)
print(f2)
