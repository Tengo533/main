import pandas as pd
import matplotlib.pyplot as plot

df = pd.DataFrame({
"name":["William","Emma","Sofia","Markus","Edward"],
"region":["East","North","East","South","West"],
"sales":[50000,52000,90000,34000,42000],
"expenses":[42000,43000,50000,44000,38000]})

y = df.sales
x = df.name

plot.bar(x,y, label="Staff Sales")
plot.xlabel("Staff")
plot.ylabel("Sales")

plot.legend()

plot.show()

