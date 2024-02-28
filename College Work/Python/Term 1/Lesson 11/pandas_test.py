import pandas as pd

test = {
   "Tests" :  [100, 44, 98],
   "Name" : ["Kalel", "Dave", "John"]
}
myvar = pd.DataFrame(test)
print(myvar)