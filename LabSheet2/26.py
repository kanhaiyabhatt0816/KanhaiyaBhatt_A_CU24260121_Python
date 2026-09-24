import pandas as pd
from student_data import data

df = pd.DataFrame(data)
df["Grade"] = pd.cut(df["Marks"], bins=[-1, 59, 69, 79, 89, 100], labels=["D", "C", "B", "A", "A+"])
print(df[["Name", "Marks", "Grade"]])
