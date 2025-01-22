from Chromosome import Chromosome
from Read import read_data
import random
import math
import Read


class GeneticAlgorithm:

    # Constructor
    def __init__(self, datos_train,seed, nInd, maxIter):
        self.datos_train = Read.read_data(datos_train)
        self.seed = seed
        self.nInd = nInd
        self.maxIter = maxIter

    
    # Method to print the object
    def __repr__(self):
        return (f"GeneticAlgorithm:\n"
            f"Train data size: {len(self.datos_train)} rows\n"
            f"Population size: {self.nInd}\n"
            f"Max iterations: {self.maxIter}\n")

    # Method to generate the initial population
    def generatePopulation(self):

        n = self.nInd
        cromosomas = []
        for i in range(n):
            # Create a random chromosome with 35 attributes because we have 35 columns in the dataset
            cromosomas.append(Chromosome.create_random(35))
        return cromosomas
    
    # Method to sort the chromosomes by fitness, here best fitness is the lowest value
    def sortFitness(self,cromosomas):
        
        # cromoFitness [(fitValue1, cromosoma1),(fitValue2, cromosoma2)...]
        cromoFitness = []
        datos = self.datos_train

        for i in range(len(cromosomas)):
            cromosoma = cromosomas[i]
            # We are going to evalue the chomosome
            fitValue = Chromosome.fitnessFunction(cromosoma, datos)
            cromoFitness.append((fitValue, cromosoma))
        
        #Sort to have the chromosomes with the LOWEST fitness first (higher fitness means greater error)
        sortedCromoFitness = sorted(cromoFitness, key=lambda x: x[0])
        return sortedCromoFitness
    

    # Method to select the parents
    @staticmethod
    def parentSelection(eval,k):
        parents = []
        while(len(parents)<len(eval)):
            # Select k random chrmosomes of the population
            group = random.sample(eval, k)
            # Sort chromosomes by fitness
            group = sorted(group, key = lambda x: x[0])
            # Add only the chromosome with best fitness
            parents.append(group[0][1])
        return parents


    # Method to crossover the parents
    @staticmethod
    def crossover(pair, p):
        num = random.random()
        children = []
        # probability of crossover. If they do not crossover, the parents remain unchanged.
        if(num < p):
            # random cut in chromosome
            cut = random.randint(1, len(pair[0].attributes)-1)
            parent1 = pair[0].attributes
            parent2 = pair[1].attributes
            # new two children 
            child1 = Chromosome(parent1[:cut] + parent2[cut:])
            child2 = Chromosome(parent2[:cut] + parent1[cut:])
            children.append(child1)
            children.append(child2)

        else:
            children = pair
        return children

    # Method to mutate the children
    @staticmethod
    def mutate(chromosome, mutationProb, d = 0.3):
        cromosoma_vars = chromosome.attributes
        for i in range(len(cromosoma_vars)):
            # each number of the chromosome has probability to be mutated
            if random.random() < mutationProb:
                # the mutation is random too
                delta = random.uniform(-d, d)
                cromosoma_vars[i] += delta
        return Chromosome(cromosoma_vars)



# Test the GeneticAlgorithm class
#parameters
'''n_ind = 5 # number of chromosomes
n_iter = 10 # number of iterations
elitismRate = 0.2
sizeElite = math.floor(n_ind*elitismRate)

k = 3
#Probabilidad de cruce
p = 0.8
#Probabilidad de mutación
mutationProb = 0.1
#Brusquedad en las mutaciones (0.3 por defecto)
mutationDelta = 0.2


#test create an object type ag
ag = GeneticAlgorithm(
	# datos de entrenamiento (para el proceso del AG)
	datos_train = "data/train_updated.csv", 
	# semilla para numeros aleatorios
	seed=123, 
	# numero de individuos
	nInd = n_ind, 
	# maximo de iteraciones
	maxIter = n_iter
)
print(ag)


# Test the generatePopulation method
population = ag.generatePopulation()
print(population)
eval = ag.sortFitness(population)
print(eval)

# How many chromosome will be elite
elite = eval[:sizeElite]
print("esto es la elite", elite)

# this is the elites chromosomes
elite = [x[1] for x in elite]
#print(elite)
eval = eval[sizeElite:]
print(len(eval))

parents = GeneticAlgorithm.parentSelection(eval, k)
#print(parents)

# we are going to get pair of parents since we dont have more parents
pair = random.sample(parents, 2)
children = GeneticAlgorithm.crossover(pair, p)

# now maybe childrens can be mutate

mutateChildren = GeneticAlgorithm.mutate(children[0], mutationProb, mutationDelta)
mutateChildren = GeneticAlgorithm.mutate(children[1], mutationProb, mutationDelta)
'''









