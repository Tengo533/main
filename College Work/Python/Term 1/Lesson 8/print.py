# Different types of print statments:

my_country = "UK"
value1 = "Individual Liberty"

# concatenation using + or , 

print("My country " + my_country + ", believes in " + value1)
print("My country " , my_country , ", believes in " , value1)

# format version, bit like c: printf("%s", my_country)

print("My country {}, believes in {}".format(my_country, value1))

# f-string py 3.6 onwards

print(f"My country {my_country}, believes in {value1}")
        