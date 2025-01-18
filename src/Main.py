import GeneticAlgorithm
import random



def train(n, numGen, sizeElite, k, p, cut, mutationProb, houses):
    # Creation of n cromosomas
    population = GeneticAlgorithm.GeneticAlgorithm(n)

    # We asses the chromosome
    eval = population.sortFitness(houses)

    
    #After create de initial population, we select, cross and mutate
    #one time for generation
    #in each generation we have n individuals

    for i in range(numGen):
        #We get the list of tuplas that relation (fitness, cromosoma)
        #the list is sorted lower toward higher fitness (betters individuals first)

        elite = eval[:sizeElite]
        elite = [x[1] for x in elite]
        eval = eval[sizeElite:]
        
        # if the number of individual in the population after select the elite is odd, we add another one in the elite
        if len(eval)%2 == 1:
            elite.append(eval.pop(0)[1])

        #Selecction by tournament:
        parents = population.parentSelection(eval, k)
        
        newGen = elite

        while(len(parents) > 0):
            pair = random.sample(parents, 2)
            children = population.crossover(pair, p, cut)
            newGen.append(population.mutate(children[0], mutationProb))
            newGen.append(population.mutate(children[1], mutationProb))
            parents.remove(pair[0])
            parents.remove(pair[1])
        population.cromosomas = newGen
        #Assess the new generation
        eval = population.sortFitness(houses)
        print("Generation ", i, " error: " , eval[0][0])
        
    return population.sortFitness(houses)[0]