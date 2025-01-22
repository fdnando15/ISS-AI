import random
import math

from Read import read_data


class Chromosome:

    # Constructor
    def __init__(self, attributes):
        self.attributes = attributes

    # String representation of the chromosome
    def __str__(self):
        res = "["
        for i in range(len(self.attributes)//2):
            res += str(self.attributes[i*2]) + "(*a" + str(i) + "^" + str(self.attributes[i*2+1]) + ") + "
        res += str(self.attributes[-1])+ "]"
        return res


    # Create a random chromosome
    @classmethod
    def create_random(cls, size):
    
        return cls(
            [random.uniform(-1, 1) for i in range(size)]
        )
    

    # Use the regression formula to calculate the value of y'
    @staticmethod
    def computeY(cromosoma, row):
        res = 0.0
        vars = list(row)
        for i in range(len(vars)-1):
            if vars[i] == 0.0:
                continue
            
            # Compute the value of y' using the regression formula, get the real part of the result
            res += cromosoma.attributes[i*2]* (float(vars[i])**cromosoma.attributes[i*2+1]).real
        
        res += cromosoma.attributes[-1]
        return res
    
    # Calculate the error between y' and real y
    @staticmethod
    def fitnessFunction(cromosoma,data):
        # We will use RMSE (Root Mean Square Error) to measure performance
        avgError = 0.0
        for row in data:
            vars = list(row)

            # For each row, compute the predicted value using the chromosome
            predicted = Chromosome.computeY(cromosoma, row)
            actualValue = vars[-1]

            # Calculate the squared error between the predicted value and the actual value
            error = (predicted - float(actualValue))**2
            avgError += error

        # Calculate the average squared error and take the square root to obtain RMSE   
        avgError = math.sqrt(avgError/len(data))
        return avgError


# Test
#data = read_data("data/train_updated.csv")
#data = [[0.1, 0.5, 1, 0, 0.8],[0.4, 0.3, 0.7 ,0 , 0.6]]
#chromosome1 = Chromosome.create_random((len(data[0])*2)+1)
#print((len(data[0])*2)+1)
#print(chromosome1)
#print(Chromosome.fitnessFunction(chromosome1,data))