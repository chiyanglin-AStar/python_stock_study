import pandas as pd
 
 
grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
 
df = pd.DataFrame(grades)
print("原來的df")
print(df)
 
print("=================================")
 
new_df = df.append({
    "name": "Henry",
    "math": 60,
    "chinese": 62
}, ignore_index=True)
 
print("新增一筆資料")
print(new_df)
