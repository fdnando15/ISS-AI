import csv
from collections import namedtuple

    
data_car = namedtuple(
    "data_car",
    [
        "prod_year",
        "mileage",
        "cylinders",
        "airbags",
        "levyI",
        "manufacturerI",
        "modelI",
        "categoryI",
        "leather_interiorI",
        "fuel_typeI",
        "engine_volumeI",
        "gear_box_typeI",
        "drive_wheelsI",
        "doorsI",
        "wheelI",
        "colorI",
        "price",
    ],
)
def read_data(file):
    
    '''
    @param fichero: path of the file that we are going to read. 
    @type fichero:srt
    @return: A list of tuples of type data_car with all the values of the csv.
    '''
    
    data = []

    
    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        
        
        for row in reader:
             
            prod_year = float(row[0])  
            mileage = float(row[1])  
            cylinders = float(row[2]) 
            airbags = float(row[3])  
            levyI = float(row[4])  
            manufacturerI = float(row[5])  
            modelI = float(row[6])  
            categoryI = float(row[7])  
            leather_interiorI = float(row[8])  
            fuel_typeI = float(row[9])  
            engine_volumeI = float(row[10])  
            gear_box_typeI = float(row[11])  
            drive_wheelsI = float(row[12])  
            doorsI = float(row[13])  
            wheelI = float(row[14])  
            colorI = float(row[15])  
            price = float(row[16])  
            
            tupla = data_car(prod_year, mileage, cylinders, airbags, levyI, 
                             manufacturerI, modelI, categoryI, leather_interiorI, 
                             fuel_typeI, engine_volumeI, gear_box_typeI, drive_wheelsI, 
                             doorsI, wheelI, colorI, price)
            data.append(tupla)
        
    return data  


# Test you have to be in the root directory of the project
#data = read_data("data/train_updated.csv")
#print(data[0])