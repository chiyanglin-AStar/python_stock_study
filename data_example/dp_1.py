# Importing pandas as pd
import pandas as pd
  
# Creating the first Dataframe using dictionary
df1 = df = pd.DataFrame({"a":[1, 2, 3, 4],
                         "b":[5, 6, 7, 8]})
  
# Creating the Second Dataframe using dictionary
df2 = pd.DataFrame({"a":[1, 2, 3],
                    "b":[5, 6, 7]})
  
# Print df1
print(df1, "\n")
print("--------------------------\n") 
# append df2 to df1 

df1.append(df2)

# Print df2
df2

print("--------------------------\n") 