import math
import os
import Chromosome
import GeneticAlgorithm
import random
import Read


# Function to train the genetic algorithm
def train(n, numGen, sizeElite, k, p, mutationProb):

    # Create the genetic algorithm object
    ag = GeneticAlgorithm.GeneticAlgorithm(
        datos_train="data/train_updated.csv", # Path to the training data
        seed=123,                             # Seed for the random number generator
        nInd=n,                               # Number of individuals
        maxIter=numGen                        # NNumber of iterations
    )
    print(ag)

    # Generate the initial population
    population = ag.generatePopulation()


    # We iterate over the number of generations
    for i in range(numGen):
        
        # Sort the population by fitness [(error, chromosome), ...])
        eval = ag.sortFitness(population)

        # Select the elite
        elite = eval[:sizeElite]
        elite = [x[1] for x in elite]

        # Remove the elite from the population
        eval = eval[sizeElite:]

        # Add the elite to the new generation
        newGen = []
        newGen = elite + newGen
        
        # if the number of individual in the population after select the elite is odd, we add another one in the elite
        if len(eval)%2 == 1:
            elite.append(eval.pop()[1])


        # Select the parents for the new generation
        parents = GeneticAlgorithm.GeneticAlgorithm.parentSelection(eval, k)

        # Generate the new generation
        while(len(parents) > 0):
            pair = random.sample(parents, 2)
            children = GeneticAlgorithm.GeneticAlgorithm.crossover(pair, p)
            newGen.append(GeneticAlgorithm.GeneticAlgorithm.mutate(children[0], mutationProb))
            newGen.append(GeneticAlgorithm.GeneticAlgorithm.mutate(children[1], mutationProb))
            parents.remove(pair[0])
            parents.remove(pair[1])
        
        
        # Sort the new generation by fitness [(error, chromosome), ...])
        evalNew = ag.sortFitness(newGen)
        new_population = [x[1] for x in evalNew]
        population = new_population

        print("Generation ", i, " error: " , evalNew[0])
        
    return population


if __name__ == "__main__":

    # parameters

    n_ind = 20 # number of chromosomes

    n_iter = 10 # number of iterations

    elitismRate = 0.2 # percentage of elite chromosomes

    sizeElite = math.floor(n_ind*elitismRate)

    k = 2 # probability of crossover

    p = 0.8 # cut crossover point
    
    mutationProb = 0.1 # probability of mutation (0.3 by default)


    # Train the genetic algorithm

    lastGeneration = train(n_ind, n_iter, sizeElite, k, p, mutationProb)

    # Test the genetic algorithm
   
    data_path_test = os.path.join('data', 'test_updated.csv')
    #Data_path uses os library to make a path valid for linux and windows machines
    cars_test = Read.read_data(data_path_test)
    errortest = Chromosome.Chromosome.fitnessFunction(lastGeneration[0], cars_test)
    print("Error en test: ", errortest)