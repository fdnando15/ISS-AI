import math
import os
import Chromosome
import GeneticAlgorithm
import random

import Read

"""def main():
    print("Hello, World! The project is working")
    
    # Number of chromosome
    n = 35
    # Numbre of generations
    numGen = 10
    # The best two individual of each generation pass to the following generation without changes:
    elitismRate = 0.05
    sizeElite = math.floor(n*elitismRate)

    #Rate k for the selecion of paretns by tournament
    k = 2

    #probability of cross
    p = 0.8

    #point of cut for the cross
    cut = 9

    #probability of mutation
    mutationProb = 0.2

    # Read data
    data_path_train = os.path.join('data', 'train_updated.csv')
    data_path_test = os.path.join('data', 'test_updated.csv')
    #Data_path uses os library to make a path valid for linux and windows machines
    cars_train = Read.read_data(data_path_train)
    cars_test = Read.read_data(data_path_test)
    
    best = train(n, numGen, sizeElite, k, p, cut, mutationProb, cars_train)
    print(best)
    test = Chromosome.fitnessFunction(best[1], cars_test)
    print("Error en test: ", test)"""

def train(n, numGen, sizeElite, k, p, mutationProb):
    # Creation of n cromosomas
    ag = GeneticAlgorithm.GeneticAlgorithm(
        datos_train="data/train_updated.csv",  # Ruta al archivo de datos de entrenamiento
        seed=123,                             # Semilla para reproducibilidad
        nInd=n,                               # Número de cromosomas (individuos)
        maxIter=numGen                        # Número de generaciones
    )
    print(ag)
    # We asses the chromosome
    population = ag.generatePopulation()

    #print("Initial population: ", population)
    

    
    #After create de initial population, we select, cross and mutate
    #one time for generation
    #in each generation we have n individuals

    for i in range(numGen):
        #We get the list of tuplas that relation (fitness, cromosoma)
        #the list is sorted lower toward higher fitness (betters individuals first)
        eval = ag.sortFitness(population)

        elite = eval[:sizeElite]
        elite = [x[1] for x in elite]
        eval = eval[sizeElite:]
        
        # if the number of individual in the population after select the elite is odd, we add another one in the elite
        if len(eval)%2 == 1:
            elite.append(eval.pop(0)[1])

        #Selecction by tournament:
        parents = GeneticAlgorithm.GeneticAlgorithm.parentSelection(eval, k)
        
        newGen = []
        newGen.append(elite[0])

        while(len(parents) > 0):
            pair = random.sample(parents, 2)
            children = GeneticAlgorithm.GeneticAlgorithm.crossover(pair, p)
            newGen.append(GeneticAlgorithm.GeneticAlgorithm.mutate(children[0], mutationProb))
            newGen.append(GeneticAlgorithm.GeneticAlgorithm.mutate(children[1], mutationProb))
            parents.remove(pair[0])
            parents.remove(pair[1])
        
        #Assess the new generation
        eval = ag.sortFitness(newGen)
        print("Generation ", i, " error: " , eval[0][0])
        
    return eval[0]


if __name__ == "__main__":

    n_ind = 10 # number of chromosomes
    n_iter = 100 # number of iterations
    elitismRate = 0.2
    sizeElite = math.floor(n_ind*elitismRate)

    k = 3
    #Probabilidad de cruce
    p = 0.8
    #Probabilidad de mutación
    mutationProb = 0.1
    #Brusquedad en las mutaciones (0.3 por defecto)
    mutationDelta = 0.2
    train(n_ind, n_iter, sizeElite, k, p, mutationProb)