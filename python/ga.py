#!/usr/bin/env python
"""
Code to demonstrate a genetic algorithm to identify a method to solve a simple mathematical problem. 

"""

__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2014 Bryce Himebaugh. All rights reserved. Additional copyrights may follow."
__license__ = "GPL v3"

from random import randint
from math import pow

class Chromosome:
    def __init__(self):
        self.genes = []
        state = 0
        for i in range(9):
            if state == 0:
                self.genes.append(randint(0,9))
                state = 1
            else:
                self.genes.append(randint(10,13))
                state = 0
                
    def show_genes(self):
        for i in range(len(self.genes)):
            print self.genes[i]

    def evaluate(self): 
        result = self.genes[0]
        current_gene = -1
        next_gene = -1
        state = 0

        for i in range(len(self.genes)):
            current_gene = self.genes[i] 
            if state == 0:
                state = 1
            else:
                next_gene = self.genes[i+1]
                if (current_gene == 10):
                    result = result + next_gene
                elif (current_gene == 11):
                    result = result - next_gene
                elif (current_gene == 12):
                    result = result * next_gene
                elif (current_gene == 13):
                    if (next_gene != 0):
                        result = result / next_gene
                    else:
                        return -1
                else:
                    pass
                state = 0
        return result

    def compute_fitness(self, target): 
        value = self.evaluate()
        if value != -1:
            error = float(target - value)
            if error > 1000.0:
                fitness = 1/1000.0
            elif error == 0:
                fitness = 2.0
                pass
            else:
                fitness = 1/error
        else:
            fitness = 1/1000.0
        return fitness

     
class Population:

    def __init__(self,members,target):
        self.target = target
        self.population = []
        for i in range(members):
            self.population.append(Chromosome())

    def show_population(self):
        for i in range(len(self.population)):
            if (abs(self.population[i].compute_fitness(self.target)) > 1.0):
                print "member:",i
                print "Evaluates to:",self.population[i].evaluate()
                print "Fitness:",abs(self.population[i].compute_fitness(self.target))
                for j in range(len(self.population[i].genes)):
                    print self.population[i].genes[j]

if __name__ == '__main__':
    p = Population(100000,67)
    p.show_population()
    pass
