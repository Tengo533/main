import pandas
my_dataset = {
    'Cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3,7,2]
}

myvar = pandas.DataFrame(my_dataset)
print(myvar)