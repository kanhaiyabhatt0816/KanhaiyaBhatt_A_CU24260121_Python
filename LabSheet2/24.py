import pandas as pd
from student_data import data

df = pd.DataFrame(data)
df["FinalMarks"] = df["Marks"] + df["Bonus"]
print(df[["Name", "Marks", "Bonus", "FinalMarks"]])
